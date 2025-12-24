import subprocess
from pathlib import Path

# Adjust this to match your repo layout
AUDIO_DIR = Path(__file__).parent / "assets" / "audio"


def play_audio(filename: str) -> None:
    """
    Play a WAV file using 'aplay'.
    Blocks until playback finishes.
    """
    path = AUDIO_DIR / filename

    if not path.exists():
        print(f"[AUDIO] File not found: {path}")
        return

    try:
        # -q = quiet (no extra ALSA spam)
        subprocess.run(["aplay", "-q", str(path)], check=False)
    except FileNotFoundError:
        print("[AUDIO] 'aplay' not found. Install 'alsa-utils' or adjust player command.")
