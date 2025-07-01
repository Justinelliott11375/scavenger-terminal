from transitions import Machine

class GameState:
	states = ['initial', 'keyboard_connected']

	def __init__(self):
		self.machine = Machine(model=self, states=GameState.states, initial='initial')

		self.machine.add_transition(trigger='connect_keyboard', source='initial', dest='keyboard_connected')
