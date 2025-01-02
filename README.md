# Fireflies.ai Transcript Downloader

A simple Python application that downloads the transcription of your last uploaded recording from Fireflies.ai.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file by copying the example:
```bash
cp .env.example .env
```

3. Edit the `.env` file and add your Fireflies.ai API key:
```
FIREFLIES_API_KEY=your_api_key_here
```

You can find your API key in your Fireflies.ai account settings.

## Usage

The script supports two modes of operation:

### 1. Info Mode
Displays detailed information about the latest transcript, including summary and metadata:
```bash
python get_last_transcript.py info
```

This will show:
- Basic transcript details (title, date, meeting URL, user)
- Overview
- Action items
- Key points
- Keywords

### 2. Clipboard Mode
Copies the entire transcript text to your system clipboard:
```bash
python get_last_transcript.py clipboard
```

This is useful when you want to quickly paste the transcript content into another application.

## Error Messages

- If you see "No transcripts found", it means there are no recordings in your account
- If you see "Error: FIREFLIES_API_KEY not found", check your .env file configuration
- If you see "Failed to copy transcript to clipboard", there might be an issue with clipboard access 