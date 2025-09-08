from time import sleep

from rich.panel import Panel
from rich.progress import BarColumn, Progress
from rich.table import Table

from assets.boot_log_sequence_steps import chess_piece_book_log, treasure_island_book_log
from terminal_output import TerminalOutput


class CommandHandler:
	def __init__(self, terminal_session):
		self.terminal_session = terminal_session
		self.console = terminal_session.console

	def handle_command(self, command: str) -> str:
		command = command.strip().lower()

		# This is gross, refactor to handle the ever-growing list of commands more gracefully
		# TODO: maybe switch/case or a dictionary mapping commands to methods
		if command == 'help':
			return self.handle_help()
		elif command == 'scan':
			return self.handle_scan()
		elif command == 'status':
			return 'Subsystem status:\n- Audio: OK\n- Visual: Calibrated\n- Lock: Standby'
		elif command == 'enhance':
			return 'Enhancing signal...\n[green]Signal clarity improved by 37%[/green]'
		elif command == 'dev-test-hub':
			if self.terminal_session.state.is_initial():
				self.terminal_session.state.discover_treasure_island_book()
			return TerminalOutput(lines=['[green]Treasure Island book discovered.[/green]'], scrollable=False)
		elif command == 'exit':
			return TerminalOutput(
				lines=['[red]Session terminated.[/red]'],
				scrollable=False,
			)
		elif command == 'quest':
			return self.handle_quest()
		# Figure out a better name for this
		elif command == 'audio clue deciphered':
			return
		else:
			return ["[yellow]Unknown command.[/yellow] Type 'help' for a list of valid commands."]

	def handle_help(self):
		table = Table(show_header=True, header_style='bold green')
		table.add_column('Command', style='cyan', no_wrap=True)
		table.add_column('Description', style='dim')

		table.add_row('help', 'Display the list of available commands')
		table.add_row('scan', 'Show system status')
		table.add_row('quest', 'Summarize current objective')
		table.add_row('clear', 'Clear the terminal screen')
		# table.add_row('exit', 'Terminate session')

		# self.console.print(table)
		return TerminalOutput(renderable=table)

	def handle_scan(self):
		with Progress(
			'[progress.description]{task.description}',
			BarColumn(bar_width=None),
			'[progress.percentage]{task.percentage:>3.0f}%',
			console=self.console,
			transient=True,
		) as progress:
			task = progress.add_task('[cyan]Scanning subsystems...', total=100)

			for i in range(0, 100, 2):
				sleep(0.1)  # optional: longer delay based on stage
				progress.update(task, advance=2)

		# Extract this to somewhere else
		# self.console.print(
		return TerminalOutput(
			renderable=Panel.fit(
				'\n'.join(
					# This will either need to be a lot of separate blobs, or dynamically generated
					[
						'[green]System scan complete',
						'Restoration progress: [bold green]11%[/bold green]',
						'Online subsystems: [bold green]CORE, INTERFACE[/bold green]',
						# TODO: check these as we move forward, don't know what memory and signal are atm
						'Offline subsystems: [bold red]AUDIO, MEMORY, SIGNAL[/bold red]',
						'[dim]Unread fragments detected: 1[/dim][/green]',
					]
				),
				title='SCAN RESULTS',
				border_style='green',
			)
		)

	def handle_quest(self):
		# TODO: look into a cleaner way to word states and transitions, this feels weird
		log = treasure_island_book_log if self.terminal_session.state.is_initial() else chess_piece_book_log

		return TerminalOutput(
			renderable=Panel.fit(
				'\n'.join(log),
				title='/// Current Objective ///',
				border_style='green',
			)
		)
