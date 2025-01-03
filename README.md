# Fireflies.ai Transcript Downloader

This is a productivity app. Imagine how many times you thought about recording your thoughts on Fireflies.ai and then using the transcription for something else. Or maybe you wanted to summarize your thoughts using ChatGPT, not fireflies.ai, but you wanted to use fireflies.ai to record your thoughts.

This is the answer. With this app, you can capture your transcription from fireflies.ai to your clipboard with a single click! The application has been tested on Linux and MacOS. I am not sure if it works on Windows.

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

4. Preferably, add the path to this project to your PATH.

## Usage

The script supports two modes of operation:

### 1. Info Mode
Displays detailed information about the latest transcript, including summary and metadata:

```bash
ftc-info.sh
```

or if you are using Windows and do not have bash installed:

```cmd
cd /path/to/fireflies-to-clipboard
.\venv\Scripts\activate
python get_last_transcript.py info
```

(you can also automate it with a Windows script, but I am not an expert here)


This will show:
- Basic transcript details (title, date, meeting URL, user)
- Overview
- Action items
- Key points
- Keywords

### 2. Clipboard Mode
Copies the entire transcript text to your system clipboard:

```bash
ftc-clipboard.sh
```

or if you are using Windows and do not have bash installed:

```cmd
cd /path/to/fireflies-to-clipboard
.\venv\Scripts\activate
python get_last_transcript.py clipboard
```

(you can also automate it with a Windows script, but I am not an expert here)


This is useful when you want to quickly paste the transcript content into another application.

## Error Messages

- If you see "No transcripts found", it means there are no recordings in your account
- If you see "Error: FIREFLIES_API_KEY not found", check your .env file configuration
- If you see "Failed to copy transcript to clipboard", there might be an issue with clipboard access 
