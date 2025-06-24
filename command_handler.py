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
		if command == 'help':
			self.handle_help()
		elif command == 'scan':
			self.handle_scan()
		elif command == 'status':
			return 'Subsystem status:\n- Audio: OK\n- Visual: Calibrated\n- Lock: Standby'
		elif command == 'enhance':
			return 'Enhancing signal...\n[green]Signal clarity improved by 37%[/green]'
		elif command == 'exit':
			return '[red]Session terminated.[/red]'
		else:
			return "[yellow]Unknown command.[/yellow] Type 'help' for a list of valid commands."

	def handle_help(self):
		table = Table(show_header=True, header_style='bold green')
		table.add_column('Command', style='cyan', no_wrap=True)
		table.add_column('Description', style='dim')

		table.add_row('help', 'Display this command list')
		table.add_row('scan', 'Scan system memory and environment for actionable data')
		table.add_row('quest', 'Review current objectives')
		table.add_row('clear', 'Clear the terminal screen')
		table.add_row('exit', 'Terminate session')

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

			for i in range(0, 101, 10):
				sleep(0.1)  # optional: longer delay based on stage
				progress.update(task, advance=5)

		self.console.print(
			Panel.fit(
				'\n'.join(
					[
						'[bold green]✔[/bold green] Core system: Stable',
						'[bold yellow]▲[/bold yellow] External interface: Partial functionality',
						'[bold red]✖[/bold red] Subnet 04: No response',
						'[bold cyan]...[/bold cyan] Location triangulation pending...',
						'',
						'[dim]Hint: Clarity improves with signal strength.[/dim]',
						'[dim]Hint: Noise reduction may reveal intent.[/dim]',
					]
				),
				title='SCAN RESULTS',
				border_style='white',
			)
		)
