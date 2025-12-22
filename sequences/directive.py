from sequence_types import Call, PrintLine, RabbitSay, Sleep, TerminalSequence


def directive_sequence(session) -> TerminalSequence:
	state = session.state
	state_name = getattr(state, 'state', None)

	return globals().get(state_name)(session)


def initial(session) -> TerminalSequence:
	session.state.run_mirror_clue_directive_initial()

	effects = session.effects
	console = session.console

	return TerminalSequence(
		name='Directive - Rabbit Hijack (Initial)',
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
			Sleep(3),
			# Call(lambda: effects.glitch_type_out(wrapped_text, delay=0.04, glitch_chance=0, style='bold magenta')),
			RabbitSay(
				text='The truth is framed in circles.',
			),
			RabbitSay(
				text='Even a spiral begins by turning back.',
			),
			RabbitSay(
				text='Find your round reflection.',
			),
			RabbitSay(
				text='Look behind you to see what’s right in front of you.',
			),
		],
	)


def mirror_clue_directive_initial(session) -> TerminalSequence:
	session.state.run_mirror_clue_directive_repeat()

	return mirror_clue_directive_repeat(session)


def mirror_clue_directive_repeat(session) -> TerminalSequence:
	console = session.console

	return TerminalSequence(
		name='Directive - Rabbit Hijack (Repeat)',
		steps=[
			PrintLine('[SYS] Directive cache recall...', 'green'),
			Call(console.clear),
			# Call(lambda: effects.glitch_type_out(wrapped_text, delay=0.04, glitch_chance=0, style='bold magenta')),
			RabbitSay(
				text='The truth is framed in circles.',
				after_action='stay',
			),
			RabbitSay(
				text='Even a spiral begins by turning back.',
				after_action='stay',
			),
			RabbitSay(
				text='Find your round reflection.',
				after_action='stay',
			),
			RabbitSay(
				text='Look behind you to see what’s right in front of you.',
				after_action='stay',
			),
		],
	)
