from time import sleep

from rich.panel import Panel
from rich.progress import BarColumn, Progress
from rich.table import Table


class CommandHandler:
	def __init__(self, console):
		self.console = console

	def handle_command(self, command: str) -> str:
		command = command.strip().lower()

		# This is gross, refactor to handle the ever-growing list of commands more gracefully
		# TODO: maybe switch/case or a dictionary mapping commands to methods
		if command == 'help':
			self.handle_help()
		elif command == 'scan':
			self.handle_scan()
		elif command == 'status':
			return 'Subsystem status:\n- Audio: OK\n- Visual: Calibrated\n- Lock: Standby'
		elif command == 'enhance':
			return 'Enhancing signal...\n[green]Signal clarity improved by 37%[/green]'
		elif command == 'exit':
			return ['[red]Session terminated.[/red]']
		elif command == 'quest':
			# TODO: this is test output for pagination, clean up and extract
			# TODO: also, this will need to be dynamic and change over the course of the game
			return  [
				"//// CURRENT OBJECTIVE ////",
				# "",
				# "Status: Peripheral input missing",
				# "",
# 				ДД: “Fragments remain. Voices caught in static...
# I remember questions. Three of them. I wrote them down once. Somewhere real.”
				'[HINT] ARCHIVE NODE v014-C marked for physical containment',
				'Classification: FRAGMENTED TEXTUAL MEMORY',
				'Storage Medium: Hardcopy (Local)',
				'Recovery Method: Manual Retrieval',
			]
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

		self.console.print(table)

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
		self.console.print(
			Panel.fit(
				'\n'.join(
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
				border_style='white',
			)
		)
