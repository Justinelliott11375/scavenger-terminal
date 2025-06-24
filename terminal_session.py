from time import sleep

from readchar import readkey
from rich.console import Console
from rich.live import Live
from rich.panel import Panel

from assets.boot_language_variants import boot_language_variants

# TODO:rename this file to something more appropriate
from assets.boot_log_sequence_steps import (
	initial_boot_log_with_interrupt,
	keyboard_handshake_log,
	missing_keyboard_trace_log,
	restored_diagnostics_log,
)
from command_handler import CommandHandler
from effects import Effects
from rabbit import Rabbit


class TerminalSession:
	def __init__(self):
		self.console = Console()
		self.effects = Effects(self.console)
		self.rabbit = Rabbit(self)
		self.command_handler = CommandHandler(self.console)
		self.state = {'keyboard_connected': False, 'available_commands': ['help', 'status', 'exit']}

	def run(self):
		self.run_boot_sequence()
		self.wait_for_keyboard_input()
		self.start_interactive_session()

	def run_boot_sequence(self):
		self.console.clear()

		self.print_language_banner_cycle()
		self.print_initial_boot_log_with_interrupt()
		self.print_initial_white_rabbit_interrupt_message()

		self.effects.test_chaotic_flash()

		self.print_log_with_sleeps(log=restored_diagnostics_log, sleep_between=1, sleep_after=3)
		self.print_keyboard_trace_log_panel()

	@staticmethod
	def print_language_banner_cycle():
		with Live(refresh_per_second=4) as live:
			for step in boot_language_variants:
				header = f'[bold green]{step["header"]}[/bold green]'

				body = f'[dim][italic]{step["sample"]}[/italic][/dim]'
				live.update(Panel(f'{header}\n\n{body}', expand=False))
				sleep(1.5)

	def print_initial_boot_log_with_interrupt(self):
		for step in initial_boot_log_with_interrupt:
			self.console.print(step)

			if step == '[red]ECHO PATH BREACH[green]⠛⠃⠛[/green] DETECT[green]⠛⠃[/green]ED[/red]':
				self.effects.test_chaotic_flash()
			elif step.startswith('[red]'):
				self.effects.flash_noise_burst(center=False)
			else:
				sleep(2)

	def print_initial_white_rabbit_interrupt_message(self):
		self.console.clear()
		sleep(3)
		self.rabbit.say(text='Pay attention...')
		self.rabbit.say(text='The rabbit hole goes deeper...', glitch_chance=0)
		self.rabbit.say(text='Find the keyboard...', delay=0.2)

	def print_log_with_sleeps(self, log, sleep_between=2, sleep_after=3):
		for step in log:
			self.console.print(step)
			sleep(sleep_between)
		sleep(sleep_after)

	def print_keyboard_trace_log_panel(self):
		trace_log_panel = Panel(
			'\n'.join(missing_keyboard_trace_log),
			border_style='bold green',
			padding=(1, 2),
			title='Trace Log: WR-NIVENS-KEYBOARD',
			title_align='left',
		)
		self.console.print(trace_log_panel)

	def wait_for_keyboard_input(self):
		self.console.print('[cyan]:: Awaiting input device handshake...[/cyan]')

		while True:
			key = readkey()
			self.console.print(f'[blue]:: Received input: "{key}"[/blue]')
			if key is not None:
				sleep(1)
				break
			sleep(0.1)

		self.print_log_with_sleeps(keyboard_handshake_log, sleep_between=1, sleep_after=1.5)

	def start_interactive_session(self):
		header = '[bold green]Interactive Secure Shell Ready[/bold green]'
		body = '[dim]Type "help" for available commands.[/dim]'
		self.console.print(Panel(f'{header}\n\n{body}', expand=False))
		has_prompt_nudged = False
		while True:
			if not has_prompt_nudged:
				self.rabbit.nudge()
				has_prompt_nudged = True
			else:
				command = self.console.input('[green]>> [/green]')
				print(f'Command entered: {command}')
				result = self.command_handler.handle_command(command)
				if result:
					self.console.print(result)
				if command.strip().lower() == 'exit':
					break
