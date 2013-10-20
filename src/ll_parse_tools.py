import ll_gramtools
import ll_parser
import re

def ll_table(ll_g):
    '''
    returns the ll_parsing table, given the ll_grammar as param
    '''
    table = {}
    prods = ll_g.first
    #filling in the table with first sets
    for n_term in prods:
        table[n_term] = {}
        #row entery of the non terminal
        for rule in prods[n_term]:
            for term in prods[n_term][rule]:
                #if the corresponding column is filled, raise error 
                if term in table[n_term]:
                    print "Not LL(1) Grammar"
                    #raise Exception
                if rule != '':
                    table[n_term][term] = rule

    #using the follow set
    foll = ll_g.follow
    for n_term in foll:
        if '' in prods[n_term]:
            for term in foll[n_term]:
                if not table[n_term].get(term, None):
                    table[n_term][term] = ''

    return table

def get_parser(rules):
    '''rules is the string that contains all grammar rules'''
    g = ll_gramtools.get_ll_grammar(rules)
    par = ll_parser.parser(g)
    par.set_table(ll_table(g))
    return par


def get_input(scanner, text):
	'''
	puts input in acceptable form for the parser
	'''
	tokens, remainder = scanner.scan(text)
	return tokens


if __name__ == '__main__':
    g = \
'''E : T X
X : + E X | 
T : F Y
Y : * T Y | 
F : int | ( E )'''
    p = get_parser(g)
    input = '( int + int ) * int + ( int * int )'
    input = input.split(" ")
    print '\n'+ str(p.table)+ '\n'
    v = p.parse(input)
    print v