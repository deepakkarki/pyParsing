import ll_gramtools

class parser:
    
    def __init__(self, grammar=None, table=None):
        if table:
            self.table = table
        else:
            self.table = {}

        self.grammar = grammar
        self.stack = []


    def set_table(self, table):
        self.table = table

    def set_grammar(self, grammar):
        self.grammar = grammar

    def parse(self, input, verbose=False):
        self.stack = []
        stack = self.stack
        grammar = self.grammar
        table = self.table
        stack.append('$')
        stack.append(grammar.start)
        input.append('$')
        next = input.pop(0)
        
        while stack and next:
            if verbose : print input, 'next :', next
            tos = stack.pop()
            if verbose : print stack, 'tos : ', tos
            
            if tos in grammar.variables:
                p = table[tos].get(next, None)
                if p == None:
                    return False
                if p != '':
                    stack.extend(p.split(" ")[::-1])
            else:
                if next == tos:
                    if input:
                        next = input.pop(0)

                else:
                    print "String does not belong to the Grammar"
                    return False

        return True



