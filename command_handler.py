from time import sleep

from rich.panel import Panel
from rich.progress import BarColumn, Progress
from rich.table import Table

from audio_utils import play_audio
from assets.boot_log_sequence_steps import chess_piece_book_log, treasure_island_book_log
from sequence_types import Call, PrintLine, TerminalSequence, Sleep
from sequences.directive import directive_sequence
from terminal_output import TerminalOutput
from usb_watcher import detect_generic_usb


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
		elif command == 'directive':
			# return self.handle_directive()
			return directive_sequence(self.terminal_session)
		# Figure out a better name for this
		elif command == 'audio':
			return self.handle_audio()
		elif command == 'play':
			return self.handle_play_audio()
		else:
			return TerminalOutput(
				lines=["[yellow]Unknown command.[/yellow] Type 'help' for a list of valid commands."],
				scrollable=False,
			)

	def handle_help(self):
		table = Table(show_header=True, header_style='bold green')
		table.add_column('Command', style='cyan', no_wrap=True)
		table.add_column('Description', style='dim')

		# TODO: will need a refactor here to make the list of commands dynamic
		table.add_row('help', 'List core commands')

		if self.terminal_session.state.is_audio_clue():
			table.add_row('audio', 'list audio commands')
		table.add_row('scan', 'Scan connected hardware')
		table.add_row('directive', 'Summarize current objective')
		# table.add_row('clear', 'Clear terminal screen')
		# table.add_row('exit', 'Terminate session')

		# self.console.print(table)
		return TerminalOutput(renderable=table)

	def handle_audio(self):
		table = Table(show_header=True, header_style='bold green')
		table.add_column('Command', style='cyan', no_wrap=True)
		table.add_column('Description', style='dim')

		table.add_row('play', 'play audio clue fragments')
		table.add_row('reverse', 'play audio fragments in reverse')
		table.add_row('boost', 'Signal boost for faint audio fragments')
		table.add_row('clean', 'Noise reduction for audio fragments')

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

		usb_white_king_detected = detect_generic_usb()

		if usb_white_king_detected:
			self.terminal_session.state.insert_white_king_usb()

			return TerminalSequence(name='Scan Results', steps=[
				Sleep(1),
				PrintLine('DEVICE DETECTED: KEYBOARD', 'green'),
				Sleep(1),
				PrintLine('MODEL: WR-NIVENS-K3YBRD', 'green'),
				Sleep(1),
				PrintLine('DEVICE DETECTED: USB STORAGE', 'green'),
				Sleep(1),
				PrintLine('verifying token...', 'green'),
				Sleep(1),
				PrintLine('signature match: MONARCH//DELTA_Ξ', 'green'),
				Sleep(1),
				# Put more stuff here
				PrintLine('[SYS] New audio utilities available', 'green'),
				Sleep(1),
				PrintLine('[SYS] Type "audio" to list available audio commands', 'green'),
				Sleep(1),
				PrintLine('[SYS] Type "directive" for a trace to missing ears', 'green'),
				Sleep(1),
				PrintLine('[SYS] Monarch USB token can be safely removed', 'green'),

			])

		return TerminalSequence(name='Scan Results', steps=[
			Sleep(1),
			PrintLine('DEVICE DETECTED: KEYBOARD', 'green'),
			Sleep(1),
			PrintLine('MODEL: WR-NIVENS-K3YBRD', 'green')
		])

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

	def handle_directive(self):
		# TODO: look into a cleaner way to word states and transitions, this feels weird
		log = treasure_island_book_log if self.terminal_session.state.is_initial() else chess_piece_book_log

		return TerminalOutput(
			renderable=Panel.fit(
				'\n'.join(log),
				title='/// Current Objective ///',
				border_style='green',
			)
		)

	def handle_play_audio(self) -> TerminalSequence:
		return TerminalSequence(name='Audio - Play Raw Fragment',
			steps=[
				PrintLine("[SYS] Playing audio fragment ALICE-07...", "cyan"),
            	Sleep(0.5),
            	Call(lambda: play_audio("morpheus_audio_clean.wav")),
            	Sleep(0.2),
            	PrintLine("[SYS] Playback complete.", "cyan"),
			])
