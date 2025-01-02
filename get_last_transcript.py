import os
import sys
import argparse
import requests
import pyperclip
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('FIREFLIES_API_KEY')
BASE_URL = 'https://api.fireflies.ai/graphql'

if not API_KEY:
    print("Error: FIREFLIES_API_KEY not found in .env file")
    sys.exit(1)

def get_latest_transcript_id():
    """Get the ID of the latest transcript."""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    list_query = """
    query {
        transcripts(limit: 1) {
            title
            id
        }
    }
    """

    response = requests.post(BASE_URL, json={'query': list_query}, headers=headers)
    response.raise_for_status()
    data = response.json()

    if not data.get('data', {}).get('transcripts'):
        return None, None

    transcripts = data['data']['transcripts']
    if not isinstance(transcripts, list) or len(transcripts) == 0:
        return None, None

    return transcripts[0]['id'], transcripts[0]['title']

def get_transcript_info(transcript_id):
    """Get transcript info and summary."""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    info_query = """
    query Transcript($transcriptId: String!) {
        transcript(id: $transcriptId) {
            dateString
            meeting_link
            user {
                name
            }
            summary {
                keywords
                action_items
                outline
                shorthand_bullet
                overview
                bullet_gist
                gist
                short_summary
            }
        }
    }
    """
    
    variables = {'transcriptId': transcript_id}
    response = requests.post(
        BASE_URL,
        json={'query': info_query, 'variables': variables},
        headers=headers
    )
    response.raise_for_status()
    return response.json()

def get_transcript_text(transcript_id):
    """Get only the transcript text content."""
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    text_query = """
    query Transcript($transcriptId: String!) {
        transcript(id: $transcriptId) {
            sentences {
                text
            }
        }
    }
    """
    
    variables = {'transcriptId': transcript_id}
    response = requests.post(
        BASE_URL,
        json={'query': text_query, 'variables': variables},
        headers=headers
    )
    response.raise_for_status()
    return response.json()

def display_info(transcript_data, title):
    """Display formatted transcript information."""
    transcript = transcript_data.get('data', {}).get('transcript', {})
    
    print("\nTranscript Details:")
    print("=" * 50)
    print(f"Title: {title}")
    print(f"Date: {transcript.get('dateString', 'Not available')}")
    print(f"Meeting Link: {transcript.get('meeting_link', 'Not available')}")
    print(f"User: {transcript.get('user', {}).get('name', 'Not available')}")
    
    summary = transcript.get('summary', {})
    if summary:
        print("\nSummary:")
        print("=" * 50)
        print(f"\nOverview:")
        print(summary.get('overview', 'Not available'))
        
        action_items = summary.get('action_items')
        if action_items:
            print(f"\nAction Items:")
            print(action_items)
        
        print(f"\nKey Points:")
        print(summary.get('bullet_gist', 'Not available'))
        
        keywords = summary.get('keywords')
        if keywords:
            print(f"\nKeywords:")
            print(keywords)
    
    print("=" * 50)

def copy_to_clipboard(transcript_data):
    """Extract and copy transcript text to clipboard."""
    sentences = transcript_data.get('data', {}).get('transcript', {}).get('sentences', [])
    if not sentences:
        print("No transcript text available.")
        return False
    
    full_text = '\n'.join(sentence['text'] for sentence in sentences)
    pyperclip.copy(full_text)
    return True

def main():
    parser = argparse.ArgumentParser(description='Fireflies.ai Transcript Downloader')
    parser.add_argument('mode', choices=['info', 'clipboard'],
                      help='Operation mode: "info" for summary or "clipboard" to copy text')
    args = parser.parse_args()

    try:
        # Get the latest transcript ID
        transcript_id, title = get_latest_transcript_id()
        if not transcript_id:
            print("No transcripts found.")
            return

        if args.mode == 'info':
            # Get and display transcript info
            transcript_data = get_transcript_info(transcript_id)
            display_info(transcript_data, title)
        else:  # clipboard mode
            # Get and copy transcript text
            transcript_data = get_transcript_text(transcript_id)
            if copy_to_clipboard(transcript_data):
                print(f"Successfully copied transcript '{title}' to clipboard!")
            else:
                print("Failed to copy transcript to clipboard.")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing Fireflies.ai API: {str(e)}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Error details: {e.response.text}")
    except KeyError as e:
        print(f"Error parsing API response: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main() 
