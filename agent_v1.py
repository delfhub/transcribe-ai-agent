import ollama
from faster_whisper import WhisperModel
import datetime
import os
from pathlib import Path

def save_to_markdown(url, transcript, summary):
    # Create a filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"summary_{timestamp}.md"
    
    with open(filename, "w") as f:
        f.write(f"# AI Video Summary\n\n")
        f.write(f"**Source URL:** {url}\n")
        f.write(f"**Date:** {datetime.datetime.now().strftime('%B %d, %Y')}\n\n")
        f.write(f"--- \n\n")
        f.write(f"## Summary\n{summary}\n\n")
        f.write(f"--- \n\n")
        f.write(f"## Raw Transcript (Snippet)\n> {transcript[:500]}...\n")
        
    print(f"--- Successfully saved to {filename} ---")

def transcribe_sample(audio_path):
    # Using 'tiny' for quick iteration
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    print(f"--- transcribing {audio_path} ---")
    
    segments, _ = model.transcribe(audio_path)
    # List comprehension to join the text from all segments
    full_text = " ".join([segment.text for segment in segments])
    return full_text

def summarize_text(raw_text):
    print("--- sending to ollama ---")
    
    # This is the "Data Contract" we discussed
    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'system',
            'content': 'You are a pop-culture historian. Even if the text is short or musical, describe the mood and identify the theme of the lyrics provided.',
        },
        {
            'role': 'user',
            'content': f"Here is a snippet of text from a video: {raw_text}",
        },
    ])
    return response['message']['content']

###### print to console test
# if __name__ == "__main__":
#     # 1. The Ears
#     transcript = transcribe_sample("tech_sample.mp3")
#     print(f"Raw Transcript: {transcript[:100]}...") # Verification
    
#     # 2. The Brain
#     summary = summarize_text(transcript)
#     print("\n--- Summary Result ---")
#     print(summary)

if __name__ == "__main__":
    # The data we've gathered so far
    target_url = "https://www.youtube.com/watch?v=kqtD5dpn9C8"
    audio_file = "tech_sample.mp3"
    
    if os.path.exists(audio_file):
        # A. Transcribe (Ears)
        raw_text = transcribe_sample(audio_file)
        
        # B. Summarize (Brain)
        final_summary = summarize_text(raw_text)
        
        # C. Persist (Disk)
        saved_file = save_to_markdown(target_url, raw_text, final_summary)
        
        print(f"\n✅ Done! Summary saved to: {saved_file}")
        
        # D. Cleanup
        os.remove(audio_file)
        print(f"🗑️  Removed temporary file: {audio_file}")
    else:
        print(f"❌ Error: {audio_file} not found. Did you run the yt-dlp command?")