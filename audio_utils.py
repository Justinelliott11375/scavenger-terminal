import subprocess
from pathlib import Path

# Adjust this to match your repo layout
AUDIO_DIR = Path(__file__).parent / "assets" / "audio"


def play_audio(filename: str) -> None:
	"""
	Play a WAV file using 'aplay'.
	Blocks until playback finishes.
	"""
	print('playing audio')
	path = AUDIO_DIR / filename
	print(f'audio_dir: {AUDIO_DIR}')
	print(f'filename: {filename}')

	if not path.exists():
		print(f"[AUDIO] File not found: {path}")
		return
	print(f"[AUDIO] Playing file: {path}")
	try:
		# -q = quiet (no extra ALSA spam)
		subprocess.run(["aplay", "-q", str(path)], capture_output=True, text=True, check=False)
	except FileNotFoundError:
		print("[AUDIO] 'aplay' not found. Install 'alsa-utils' or adjust player command.")
