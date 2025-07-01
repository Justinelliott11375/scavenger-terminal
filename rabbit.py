import sys
from time import sleep
from typing import Literal


class Rabbit:
	def __init__(self, session):
		self.session = session
		self.console = session.console
		self.effects = session.effects
		self.prefix = 'ДД: '

	def say(
		self,
		text: str,
		delay: float = 0.03,
		glitch_chance: float = 0.05,
		sleep_duration: float = 3.0,
		after_action: Literal['clear', 'backspace'] = 'clear',
	) -> None:
		self.effects.glitch_type_out(self.prefix + text, delay=delay, glitch_chance=glitch_chance)
		sleep(sleep_duration)

		if after_action == 'clear':
			self.console.clear()
		elif after_action == 'backspace':
			for _ in range(len(self.prefix) + len(text)):
				sys.stdout.write('\b \b')
				sys.stdout.flush()
				sleep(0.015)

	def nudge(self) -> None:
		message = "Try typing 'help'. It won't bite."

		self.say(message, glitch_chance=0, sleep_duration=1, after_action='backspace')
