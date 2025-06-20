from rich.console import Console

from effects import Effects


class TerminalSession:
	def __init__(self):
		self.console = Console()
		self.effects = Effects(self.console)
		self.state = {'keyboard_connected': False, 'available_commands': ['help', 'status', 'exit']}
