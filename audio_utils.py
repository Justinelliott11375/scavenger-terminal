import subprocess
from pathlib import Path

# Adjust this to match your repo layout
AUDIO_DIR = Path(__file__).parent / "assets" / "audio"
APLAY_DEVICE = 'plughw:1,0'

_current_proc: subprocess.Popen | None = None

def play_audio(filename: str) -> None:
	"""
	Play a WAV file using 'aplay'.
	Blocks until playback finishes.
	"""

	global _current_proc

	path = AUDIO_DIR / filename

	if not path.exists():
		print(f"[AUDIO] File not found: {path}")
		return

	if _current_proc is not None and _current_proc.poll() is None:
		print("[AUDIO] Another audio is currently playing, terminating it.")
		# If another audio is playing, terminate it
		_current_proc.terminate()
		try:
			_current_proc.wait(timeout=2)
		except Exception:
			pass
		_current_proc = None

	cmd = ['aplay', '-q', '-D', APLAY_DEVICE, str(path)]
	try:
		_current_proc = subprocess.Popen(
			cmd,
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL,
		)

	except FileNotFoundError:
		print("[AUDIO] 'aplay' not found. Install 'alsa-utils' or adjust player command.")
		_current_proc = None

		# subprocess.run(cmd, capture_output=True, text=True, check=False)

def stop_audio() -> None:
	"""
	Stop any currently playing audio.
	"""

	global _current_proc

	if _current_proc is None:
		print("[AUDIO] No audio is currently playing.")
		return False

	if _current_proc.poll() is not None:
		print("[AUDIO] Audio process has already finished.")
		_current_proc = None
		return False

	print("[AUDIO] Stopping audio playback.")
	_current_proc.terminate()

	try:
		_current_proc.wait(timeout=2)
	except Exception:
		pass
	_current_proc = None
	return True
