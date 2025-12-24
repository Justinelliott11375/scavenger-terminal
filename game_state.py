from transitions import Machine


class GameState:
	states = [
		'initial',
		'treasure_island_book',
		'chess_piece_book',
		'mirror_clue_directive',
		'audio_clue',
	]

	def __init__(self):
		self.machine = Machine(model=self, states=GameState.states, initial='initial')

		# self.machine.add_transition(trigger='connect_keyboard', source='initial', dest='mirror_clue_directive_initial')
		self.machine.add_transition(
			trigger='run_mirror_clue_directive',
			source='initial',
			dest='mirror_clue_directive',
		)
		# self.machine.add_transition(
		# 	trigger='run_mirror_clue_directive_repeat',
		# 	source='mirror_clue_directive_initial',
		# 	dest='mirror_clue_directive_repeat',
		# )
		self.machine.add_transition(
			trigger='insert_white_king_usb',
			source='mirror_clue_directive',
			dest='audio_clue'
		)
