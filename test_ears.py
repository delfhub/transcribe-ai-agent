from faster_whisper import WhisperModel
import time

def test_transcription():
    # We use 'tiny' because it's the fastest way to verify the pipe is working
    model = WhisperModel("tiny", device="cpu", compute_type="int8")
    
    print("--- Starting Transcription ---")
    start_time = time.time()
    
    # beam_size=1 is faster but less accurate; good for a quick test
    segments, info = model.transcribe("test_sample.mp3", beam_size=1)
    
    print(f"Detected Language: {info.language} (Probability: {info.language_probability:.2f})")
    
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s]: {segment.text}")
    
    end_time = time.time()
    print(f"--- Finished in {end_time - start_time:.2f} seconds ---")

if __name__ == "__main__":
    test_transcription()