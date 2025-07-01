import random
import shutil
import sys
import time
from time import sleep

from rich.console import Console

from assets.noise_lines import noise_lines


class Effects:
	RABBIT_MESSAGE_PREFIX = 'ДД: '

	def __init__(self, console: Console):
		self.console = console

	def test_chaotic_flash(self):
		self.chaotic_flash_burst(count=8, flicker_duration=0.4, pulse=True, center=False)

	def chaotic_flash_burst(self, count=6, flicker_duration=0.4, pulse=True, center=True):
		cols = shutil.get_terminal_size().columns

		for _ in range(count):
			line = random.choice(noise_lines)
			line = self.pixel_scale_sim(line)
			if center:
				line = line.center(cols)

			self.flicker_line(line, duration=flicker_duration)
			if pulse:
				self.color_pulse(line, pulses=3, interval=0.08)

	def pixel_scale_sim(self, text):
		if random.random() < 0.5:
			return self.amplify(text, factor=2)
		return self.fullwidth(text)

	@staticmethod
	def amplify(text, factor=2):
		return ''.join(c * factor for c in text)

	@staticmethod
	def fullwidth(text):
		return ''.join(chr(ord(c) + 0xFEE0) if '!' <= c <= '~' else c for c in text)

	def flicker_line(self, text, duration=0.6, interval=0.1):
		width = shutil.get_terminal_size().columns
		padded = text.ljust(width)
		end_time = time.time() + duration
		while time.time() < end_time:
			style = random.choice(['bold red', 'dim cyan', 'yellow', 'bold magenta', 'green'])
			self.console.print(padded, style=style, end='\r', highlight=False)
			sys.stdout.flush()
			time.sleep(interval)
		self.console.print(' ' * width, end='\r')

	def print_white_rabbit_message(self, text: str, delay: float = 0.05, glitch_chance=0.05):
		self.glitch_type_out(text, delay, glitch_chance)
		sleep(3)
		self.console.clear()

	def glitch_type_out(self, text: str, delay: float = 0.075, glitch_chance=0.05, style='bold magenta'):
		"""Type out text with occasional glitched characters and optional styling."""
		# for char in f'{self.RABBIT_MESSAGE_PREFIX}{text}':
		for char in text:
			# Randomly replace character
			if random.random() < glitch_chance and char not in [' ', '.', ':', 'Д']:
				glitched_char = chr(random.randint(33, 126))
			else:
				glitched_char = char

			if glitched_char == 'Д':
				self.console.print(glitched_char, end='', style='bold white', soft_wrap=True)
			else:
				self.console.print(glitched_char, end='', style=style, soft_wrap=True)
			sys.stdout.flush()
			time.sleep(delay)

	def flash_noise_burst(self, count=15, delay=0.2, center=True):
		cols = shutil.get_terminal_size().columns
		for _ in range(count):
			line = random.choice(noise_lines)

			if center:
				line = line.center(cols)

			self.flash_and_clear(line, delay)

	def color_pulse(self, text, pulses=5, interval=0.1):
		colors = ['red', 'yellow', 'green', 'cyan', 'magenta']
		width = shutil.get_terminal_size().columns
		padded = text.ljust(width)
		for _ in range(pulses):
			style = random.choice(colors)
			self.console.print(padded, style=style, end='\r')
			sys.stdout.flush()
			time.sleep(interval)
		self.console.print(' ' * width, end='\r')

	@staticmethod
	def flash_and_clear(text, delay=0.4):
		sys.stdout.write(f'\r{text}')
		sys.stdout.flush()
		time.sleep(delay)
		sys.stdout.write('\r' + ' ' * len(text) + '\r')
		sys.stdout.flush()
