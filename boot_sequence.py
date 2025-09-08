from time import sleep

from rich.live import Live
from rich.panel import Panel

from assets.boot_language_variants import boot_language_variants
from assets.boot_log_sequence_steps import (
	initial_boot_log_with_interrupt,
	missing_keyboard_trace_log,
	restored_diagnostics_log,
)
from effects import Effects


# TODO: I don't think this file is being used anymore
def run_boot_sequence(console):
	effects = Effects(console)
	console.clear()

	print_language_banner_cycle()
	print_initial_boot_log_with_interrupt(console, effects)
	print_initial_white_rabbit_interrupt_message(console, effects)

	effects.test_chaotic_flash()

	print_log_with_sleeps(console=console, log=restored_diagnostics_log, sleep_between=1, sleep_after=3)
	print_trace_log_panel(console)
	# console.print(
	# 	'[green]Awaiting input device retrieval and connection...[/green]',
	# )

	# sleep(10)


def print_language_banner_cycle():
	with Live(refresh_per_second=4) as live:
		for step in boot_language_variants:
			header = f'[bold green]{step["header"]}[/bold green]'

			body = f'[dim][italic]{step["sample"]}[/italic][/dim]'
			live.update(Panel(f'{header}\n\n{body}', expand=False))
			sleep(1.5)


def print_initial_boot_log_with_interrupt(console, effects):
	for step in initial_boot_log_with_interrupt:
		console.print(step)

		if step == '[red]ECHO PATH BREACH[green]⠛⠃⠛[/green] DETECT[green]⠛⠃[/green]ED[/red]':
			effects.test_chaotic_flash()
		elif step.startswith('[red]'):
			effects.flash_noise_burst(center=False)
		else:
			sleep(2)


def print_initial_white_rabbit_interrupt_message(console, effects):
	console.clear()
	sleep(3)
	effects.print_white_rabbit_message(text='Pay attention...')
	effects.print_white_rabbit_message(text='The rabbit hole goes deeper...', glitch_chance=0)
	effects.print_white_rabbit_message(text='Find the keyboard...', delay=0.2)


def print_log_with_sleeps(console, log, sleep_between=2, sleep_after=3):
	for step in log:
		console.print(step)
		sleep(sleep_between)
	sleep(sleep_after)


def print_trace_log_panel(console):
	trace_log_panel = Panel(
		'\n'.join(missing_keyboard_trace_log),
		border_style='bold green',
		padding=(1, 2),
		title='Trace Log: WR-NIVENS-KEYBOARD',
		title_align='left',
	)
	console.print(trace_log_panel)
