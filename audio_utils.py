import subprocess
from pathlib import Path
from time import sleep

# Adjust this to match your repo layout
AUDIO_DIR = Path(__file__).parent / "assets" / "audio"
APLAY_DEVICE = 'plughw:1,0'
AUDIO_CARD_INDEX = 1
AUDIO_CONTROL = 'PCM'

_current_proc: subprocess.Popen | None = None
audio_files_by_state = {
	'audio_clue': 'morpheus_audio_reverse.wav',
	'audio_unreversed': 'morpheus_audio_static.wav',
	'audio_denoised': 'morpheus_audio_delay.wav',
	'audio_cleaned': 'morpheus_audio_clean.wav',
}
def play_audio(state: str) -> None:
	"""
	Play a WAV file using 'aplay'.
	Blocks until playback finishes.
	"""
	global _current_proc

	filename = audio_files_by_state.get(state)
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

	_current_proc.terminate()

	try:
		_current_proc.wait(timeout=2)
	except Exception:
		pass
	_current_proc = None
	return True


def set_output_volume(volume: int = 100) -> None:
	"""
	Set the output volume using 'amixer'.
	Volume should be an integer between 0 and 100.
	"""
	try:
		cmd = [
			'amixer',
			'-c',
			str(AUDIO_CARD_INDEX),
			'sset',
			AUDIO_CONTROL,
			f'{volume}%',
		]

		subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	except Exception as e:
		print(f"[AUDIO] Failed to set volume: {e}")
