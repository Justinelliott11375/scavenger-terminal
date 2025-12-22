# sequence_runner.py
import time
from typing import Protocol

from rabbit import Rabbit
from sequence_types import Call, Effect, OverwriteLastLine, PrintLine, PrintLines, RabbitSay, Render, Sleep
from terminal_sequence import TerminalSequence


class Console(Protocol):
	def print(self, *args, **kwargs): ...


class Effects(Protocol):
	def apply(self, name: str, params: dict): ...


class EventBus(Protocol):
	def wait(self, key: str, timeout: float | None) -> bool: ...


class SequenceRunner:
	# def __init__(self, console: Console, effects: Effects, events: EventBus,
	def __init__(self, console: Console, effects: Effects, clock=time, on_cancel=lambda: None):
		self.console = console
		self.effects = effects
		# self.events = events
		self.clock = clock
		self._cancelled = False
		self._on_cancel = on_cancel
		self.rabbit = Rabbit(self)

	def cancel(self):
		self._cancelled = True
		self._on_cancel()

	def run(self, seq: TerminalSequence) -> bool:
		for step in seq.steps:
			if self._cancelled:
				return False
			match step:
				case PrintLine(text, style):
					self.console.print(text, style=style)
				case PrintLines(lines, style):
					for ln in lines:
						self.console.print(ln, style=style)
				case Render(renderable):
					self.console.print(renderable)
				case Sleep(seconds):
					self.clock.sleep(seconds)
				case OverwriteLastLine(text, style):
					# If you use Rich Live, update the region here.
					self.console.print(text, style=style)
				case Effect(name, params):
					self.effects.apply(name, params)
				# case WaitForSignal(key, timeout):
				# if not self.events.wait(key, timeout):
				# return False
				case RabbitSay(text, delay, glitch_chance, sleep_duration, after_action):
					self.rabbit.say(text, delay, glitch_chance, sleep_duration, after_action)
				case Call(func):
					func()
				case _:
					raise ValueError(f'Unknown step: {step}')
		return True
