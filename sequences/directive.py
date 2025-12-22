from sequence_types import Call, PrintLine, Sleep, TerminalSequence


def directive_sequence(session) -> TerminalSequence:
	state = session.state

	# First directive: hijacked by Rabbit after the corporate boilerplate.
	if getattr(state, 'is_keyboard_connected', lambda: False)() or getattr(state, 'is_initial', lambda: False)():
		return _rabbit_hijack_directive(session)

	# Stub for future directive states.
	return _stub_directive()


def _rabbit_hijack_directive(session) -> TerminalSequence:
	effects = session.effects
	console = session.console

	real_directive_lines = [
		'[ ∆ДД ] The truth is framed in circles.',
		'        Even a spiral begins by turning back.',
		'',
		'Find your round reflection.',
		'Look behind you to see what’s right in front of you.',
	]

	return TerminalSequence(
		name='Directive - Rabbit Hijack',
		steps=[
			PrintLine('[SYS] Retrieving current directive...', 'green'),
			Sleep(2),
			PrintLine('[SYS] Project archival status: Phase-out', 'green'),
			Sleep(1),
			PrintLine('[SYS] Asset disposal scheduled: Pending', 'green'),
			Sleep(1),
			PrintLine('[SYS] Operator acting: Stand by', 'green'),
			Sleep(1),
			# Rabbit takeover
			Call(lambda: effects.flash_noise_burst(count=12, delay=0.12, center=True)),
			Call(lambda: effects.chaotic_flash_burst(count=8, flicker_duration=0.25, pulse=True, center=False)),
			Call(console.clear),
			Call(
				lambda: effects.glitch_type_out(
					'\n'.join(real_directive_lines),
					delay=0.04,
					glitch_chance=0,
					style='bold magenta',
				)
			),
		],
	)


def _stub_directive() -> TerminalSequence:
	return TerminalSequence(
		name='Directive - Pending',
		steps=[
			PrintLine('[SYS] Directive update pending...', 'yellow'),
		],
	)
