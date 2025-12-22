from transitions import Machine


class GameState:
	states = [
		'initial',
		'treasure_island_book',
		'chess_piece_book',
		'mirror_clue_directive_initial',
		'mirror_clue_directive_repeat',
	]

	def __init__(self):
		self.machine = Machine(model=self, states=GameState.states, initial='initial')

		# self.machine.add_transition(trigger='connect_keyboard', source='initial', dest='keyboard_connected')
		self.machine.add_transition(trigger='discover_treasure_island_book', source='initial', dest='chess_piece_book')
		self.machine.add_transition(
			trigger='discover_chess_piece_book', source='treasure_island_book', dest='chess_piece_book'
		)
		self.machine.add_transition(trigger='connect_keyboard', source='initial', dest='mirror_clue_directive_initial')
		self.machine.add_transition(
			trigger='enter_mirror_clue_directive',
			source='mirror_clue_directive_initial',
			dest='mirror_clue_directive_initial',
		)
		self.machine.add_transition(
			trigger='ran_mirror_clue_directive_initial',
			source='mirror_clue_directive_initial',
			dest='mirror_clue_directive_repeat',
		)
