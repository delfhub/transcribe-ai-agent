# Transcribe AI Agent

A Python automation tool that transcribes audio/video and generates AI summaries. Uses Whisper for transcription and Ollama for intelligent summarization.

## Features

- 🎙️ **Audio Transcription** - Converts audio files to text using Faster Whisper
- 🧠 **AI Summarization** - Generates intelligent summaries using Ollama
- 📝 **Markdown Export** - Saves transcripts and summaries to structured markdown files
- ⚡ **Fast Processing** - Optimized for CPU-based processing with int8 quantization

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- For Linux: snap (optional, for Ollama)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone git@github.com:delfhub/transcribe-ai-agent.git
cd transcribe-ai-agent
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install faster-whisper ollama
```

### 4. Install Ollama

**On Linux (recommended method):**
```bash
sudo snap install ollama
```

**Or download from:** https://ollama.ai/download

### 5. Start the Ollama Service

Before running the agent, ensure Ollama is running:

```bash
ollama serve
```

(In a separate terminal, keep this running in the background)

### 6. Pull Required Ollama Models

```bash
ollama pull llama2  # Or your preferred model
```

### 7. Get a Test Sample Audio File

To test the transcription pipeline, you'll need a `test_sample.mp3` file. You can download free-to-use content from YouTube:

#### Option A: Using yt-dlp (Recommended)

1. Install yt-dlp and ffmpeg:
```bash
pip install yt-dlp
# On Linux: sudo apt-get install ffmpeg
# On macOS: brew install ffmpeg
# On Windows: Download from https://ffmpeg.org/download.html
```

2. Download from a free-to-use YouTube channel (e.g., [Free Music Archive](https://www.youtube.com/c/FreeMusicArchiveFMA), [Creative Commons Music](https://www.youtube.com/@CreativeCommonsMusic)):
```bash
yt-dlp -f bestaudio -x --audio-format mp3 -o "test_sample.mp3" "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

3. Replace `YOUR_VIDEO_ID` with an actual video ID. Example with a Creative Commons track:
```bash
yt-dlp -f bestaudio -x --audio-format mp3 -o "test_sample.mp3" "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### Option B: Manual Download

1. Find a video with free/Creative Commons licensing on YouTube
2. Use an online converter (e.g., [YT to MP3](https://ytmp3.cc/)) to download as MP3
3. Save it as `test_sample.mp3` in the project root directory

#### Recommended Free-to-Use Channels:
- [Free Music Archive](https://www.youtube.com/@FreeMusicArchiveFMA)
- [Creative Commons Music](https://www.youtube.com/@CreativeCommonsMusic)
- [Sample Focus](https://www.youtube.com/@SampleFocus)

## Usage

### Run the Main Agent

```bash
python3 agent_v1.py
```

### Test Transcription

```bash
python3 test_ears.py
```

This will transcribe the included `test_sample.mp3` file and display language detection results.

## Project Structure

```
transcribe-ai-agent/
├── agent_v1.py          # Main agent with transcription and summarization
├── test_ears.py         # Transcription test script
├── test_brain.py        # Summarization test script
├── test_sample.mp3      # Sample audio file for testing
├── .env                 # Environment variables (if needed)
└── README.md            # This file
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory if needed:

```bash
# Example configurations
WHISPER_MODEL=tiny      # tiny, base, small, medium, large
OLLAMA_MODEL=llama2     # Your preferred Ollama model
DEVICE=cpu              # cpu or cuda
COMPUTE_TYPE=int8       # int8, int16, float16, float32
```

## Model Sizes

### Whisper Models (by speed and accuracy):
- `tiny` - Fastest, good for testing
- `base` - General purpose (default in original agent)
- `small` - Better accuracy
- `medium` - High accuracy
- `large` - Best accuracy (slowest)

## Troubleshooting

### Ollama not found
```bash
# Check if installed
ollama --version

# If not installed, use snap on Linux
sudo snap install ollama
```

### Import errors for faster_whisper
```bash
# Reinstall the package
pip uninstall faster-whisper -y
pip install faster-whisper
```

### Audio file errors
Ensure your audio file is in a supported format (MP3, WAV, FLAC, OGG, etc.)

## Testing

Run the included test files to verify installation:

```bash
# Test transcription pipeline
python3 test_ears.py

# Test summarization pipeline (requires Ollama running)
python3 test_brain.py
```

## Performance Tips

1. **Use `tiny` model for testing** - Faster iteration during development
2. **Enable GPU acceleration** - If using CUDA, change `device="cuda"` and `compute_type="float16"`
3. **Batch processing** - Process multiple files in sequence to maximize throughput
4. **Keep Ollama running** - Start it once in a background terminal

## Development

### Creating a Development Branch

```bash
git checkout -b feature/your-feature-name
```

### Generating SSH Key for GitHub

If you haven't set up SSH yet:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Then add the public key to GitHub: https://github.com/settings/keys

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

## License

MIT License - Feel free to use this project for personal and commercial purposes.

## Support

For issues or questions, please open an issue on the GitHub repository.

---

**Last Updated:** March 3, 2026
