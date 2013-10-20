from grammar import Grammar

class ll_grammar(Grammar):

	def __init__(self, V=None, T=None, S=None, P=None):
		'''specific grammar for ll parser, comes with first and follow set'''
		Grammar.__init__(self, V, T, S, P)
		self.first = {}
		self.follow = {}

	def set_first(self, f_set):
		'''Sets the first set for the ll_grammar'''
		self.first = f_set

	def set_follow(self, f_set):
		'''Sets the follow set for the ll_grammar'''
		self.follow = f_set

	def __str__(self):
		'''returns grammar in printable format'''
		s = 'Grammar \n'
		s = s + 'Start Symbol \n' + str(self.start) + '\n'
		s = s + 'Terminals \n' + str(self.terminals) + '\n'
		s = s + 'Variables \n' + str(self.variables) + '\n'
		s = s + 'Productions \n' + str(self.productions) + '\n'
		s = s + 'First set \n' + str(self.first) + '\n'
		s = s + 'Follow set \n' + str(self.follow) + '\n'
		return s


		



