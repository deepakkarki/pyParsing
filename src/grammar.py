class Grammar():

    def __init__(self, V=None, T=None, S=None, P=None):
        '''
        self : Grammar Object G
        V    : G.variables, list of non terminal symbols held as strings
        T    : G.terminals, list of terminal symbols held as strings
        S    : G.startSymbol, symbol which is a start symbol, stored as string
        P    : G.productions, dict of lists of production rules for the given Grammar
        '''
        if V:
            self.variables = V
        else: 
            self.variables = []

        if S:
            self.start = S
        else:
            self.start = ''

        if T:
            self.terminals = T
        else:
            self.terminals = []

        if P:
            self.productions = P
        else:
            self.productions = {}



    def add_V(self, symbol):
        '''Add a new symbol to the set of non terminals'''
        if symbol not in self.variables:
            self.variables.append(str(symbol))

        
    def add_T(self, symbol):
        '''Add a new terminal to the current set of terminals'''
        if symbol not in self.terminals:
            self.terminals.append(str(symbol))


    def add_P(self, lval, rval):
        '''Add a new production rule'''
        if lval in self.productions:
            self.productions[lval].append(rval)
        else:
            self.productions[lval] = [rval]


    def set_S(self, symbol):
        '''set the start symbol for the grammar'''
        self.start = symbol

    def __str__(self):
        '''Prints out G(V, T, S, P)'''
        s = 'Grammar \n'
        s = s + 'Start Symbol \n' + str(self.start) + '\n'
        s = s + 'Terminals \n' + str(self.terminals) + '\n'
        s = s + 'Variables \n' + str(self.variables) + '\n'
        s = s + 'Productions \n' + str(self.productions) + '\n'
        return s

'''
Example grammar:
make sure all spacing is appropriate
******
S : E + E | E - E | T
E : T * T | T / T | T
T : int | ( S )
******
'''
