from rich.console import Console
from rich.panel import Panel

from boot_sequence import run_boot_sequence

console = Console()


# Refactor this to handle commands as they get added further through the game
# probably want this to be its own thing at some point
def handle_command(command: str) -> str:
	command = command.strip().lower()

	if command == 'help':
		return 'Available commands:\n  help\n  status\n  enhance\n  exit'
	elif command == 'status':
		return 'Subsystem status:\n- Audio: OK\n- Visual: Calibrated\n- Lock: Standby'
	elif command == 'enhance':
		return 'Enhancing signal...\n[green]Signal clarity improved by 37%[/green]'
	elif command == 'exit':
		return '[red]Session terminated.[/red]'
	else:
		return "[yellow]Unknown command.[/yellow] Type 'help' for a list of valid commands."


def main():
	run_boot_sequence(console)
	console.print(Panel('[bold green]Interactive Secure Shell Ready[/bold green]', expand=False))

	while True:
		command = console.input('[green]>> [/green]')
		result = handle_command(command)
		console.print(result)
		if command.strip().lower() == 'exit':
			break


if __name__ == '__main__':
	main()
