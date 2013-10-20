#This is the extended gramtools library to work with the LL parser requirements

import gramtools
from ll_grammar import ll_grammar

def get_ll_grammar(string):
    '''returns a fully initialized ll_grammar object'''
    ll_g = ll_grammar()
    G = gramtools.get_grammar(string)
    ll_g.start = G.start
    ll_g.terminals = G.terminals
    ll_g.variables = G.variables
    ll_g.productions = G.productions
    ll_g.set_first(first_set_ll(G))  
    ll_g.set_follow(follow_set_ll(G))
    return ll_g

def first_set_ll(G):
    '''
    This function takes a Grammar object as its only paramater
    returns the dictionary { S : {S1 : [a,b], S2 : [c,d] }, A : {A1 :(..) ,A2 :(..), etc}
    where S -> S1 | S2 and [a,b] is first of S1 and [c,d] is first of S2
    and S, A etc are the non-terminals of Grammar G
    '''
    first_set = {}
    firsts = gramtools.first_set_elem(G)
    for n_term in G.variables:
    	first_set[n_term] = {}
    	for prod in G.productions[n_term]:
    		first_set[n_term][prod] = gramtools.first_set_exp(G, prod, firsts)

    return first_set

def follow_set_ll(G):
	'''
	just a wrapper function to maintain uniformity between first and follow set functions
	'''
	return gramtools.follow_set(G)

if __name__ == '__main__':
    g = '''S : E + E | E - E | T
E : T * T | T / T | T
T : int | ( S )'''
    g = '''E : T X
X : + E X | 
T : F Y
Y : * T Y | 
F : int | ( E )'''
    g = get_ll_grammar(g)
    print g

