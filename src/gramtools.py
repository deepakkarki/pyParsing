#############################
#This is the gramtools library
#Helps to work with the Grammar class, like find first/follow set, parse input to create Grammar objects
#This library is not intended to be a tool-set FOR the Grammar class, 
#rather a tool to help USE the Grammar class
#############################

from grammar import Grammar

def first_set_elem(G):
    '''
    Defines the first set for every non terminal and terminal
    returns {S: [...], A : [...], B : [...]}
    
    Algorithm:
    For every terminal in the grammar G, add it to firsts, key and value as terminal itself
    Then for every non terminal in G, add its first set to the dict firsts.
    do this by calling first_r(.,.,non terminal) which adds the n_term's first set to dict
    remove duplicates in the first set of every n_term
    '''
    firsts = {}
    
    def first_r(firsts, n_term):
        '''
        when called adds the first set of the n_term to the dict firsts
        '''
        if n_term in firsts:
            return None
            #exit since n_term already exists in the dictionary

        rules = G.productions[n_term]
        firsts[n_term] = []
        for prod in rules:
            elems = prod.split(" ")
            for i in elems:
	            first_r(firsts, i)
	            firsts[n_term].extend(firsts[i])
	            if i in G.terminals or '' not in G.productions[i]:
	            	#if first non-term is nullable then we also have to include the next symbols first set
	            	#but if it is not nullable then, break
	            	break
            
    for t in G.terminals:
        firsts[t] = [t]

    for n_term in G.variables:
        if n_term not in firsts:
            first_r(firsts, n_term)

    for i in firsts:
        firsts[i] = list(set(firsts[i]))
    return firsts


def first_set_exp(G, s, firsts):
	'''
	This function takes in Grammar and a string (RHS of a production) as its paramaters
	returns a list of first set for the particular RHS
	'''
	elems = s.split(" ")
	next = True
	tup = []
	for i in elems:
		tup.extend(firsts[i])
		if i in G.terminals or '' not in G.productions[i]:
			break
	return tup



def follow_set(G):
    '''
    Takes in Grammar as paramater 
    returns the follow  set for each non terminal in G.variables
    '''
    follows = {}
    #this is the dict which will contain the mappings for n_term to the corresponding follow set (viz a list)
    firsts = first_set_elem(G)
    #dict of first set
    g_prods = G.productions
    #production rules of the grammar
    def follow_r(G, n_term, follows):
        '''
        This is the recursive follow set function, pass the Grammar G, non terminal n_term (string) and  the follows set (dict) of the grammar
        if the follow set is already present in the follows dict, then this will just return
        else it will recursively find all the elements in the follow set for the given n_term, and updates follows
        '''
        #if n_term in follows.keys():#problem
            #return None
            #if n_term already exists in follows, nothing to update. end function.
        
        follows[n_term] = []
        #n_term does not exist in follows, create an entry for it and populate it.
        if n_term == G.start:
            follows[n_term] = ['$']

        for lhs in g_prods:
            #this for loop takes every non term in the lhs of G.productions, and runs the following operations on it.

            for rule in g_prods[lhs]:
                #for every production of the lhs (non terminal) in question
                symbols = rule.split(" ")
                #split the rhs of the production into list of individual symbols (non terminals and tokens)
                l = [i for i,x in enumerate(symbols) if x == n_term]
                #l is the list of indices where n_term appears in the production rule
                for pos in l:
                    if pos == len(symbols)-1:
                        #if n_term has appeared in the end of the production
                        if lhs not in follows.keys():
                            follow_r(G, lhs, follows)
                        follows[n_term].extend(follows[lhs])
                        #then the follow of lhs is subset of follow of n_term, 
                        #before this we updated follows with follow set of lhs
                    else:
                        #lhs has occured somewhere in between the production 
                        s = " ".join(symbols[pos+1:])
                        #get the part of the production which occurs after n_term
                        f = first_set_exp(G, s, firsts)
                        #find the first set of that part of production
                        if '' in f:
                            #if lambda production exists
                            f.remove('')
                            follows[n_term].extend(f)
                            #then also add follow of lhs to follows of n_term
                            if lhs not in follows.keys():
                                follow_r(G, lhs, follows)
                            follows[n_term].extend(follows[lhs])
                        else:
                            #else just add the first set to the follows of n_term
                            follows[n_term].extend(f)
        follows[n_term] = list(set(follows[n_term]))
        #remove any repeating symbols in the follow set of n_term


    for n_term in G.variables:
        follow_r(G, n_term, follows)

    return follows


def get_grammar(string):
    '''
    function takes in lines of the grammar rules as input
    returns a Grammar instance initialized with as per given grammar rules. 
    '''
    G = Grammar()
    string = string.split('\n')
    #This loop reads every line for rules
    for line in string:
        line = line.split(" : ")
        #n_term is non terminal symbol for the rule in particular line
        n_term = line[0]
        #add the non terminal to the set of non-terminals in G
        G.add_V(n_term)
        #line contains list of possble right hand productions for the n_term
        line = line[1].split("|")
        #remove leading-trailing whitespaces
        line = map(str.strip, line)
        for p in line:
        #for each possible production of n_term
            #add the production to the grammar
            G.add_P(n_term, p)
            p = p.split(" ")
                
            for t in p:
            #for every term in the production
            #if term is not a non termianl, add it to the set of terminals for G
                if t not in G.variables:
                    G.add_T(t)
                    
            #above does not ensure that all added term is not a non terminal, 
            #so this func below will ensure correctness
        for i in G.variables:
            if i in G.terminals:
                G.terminals.remove(i)
        G.start = G.variables[0]
    return G


if __name__ == '__main__':
    g = '''S : E + E | E - E | T
E : T * T | T / T | T
T : int | ( S )'''
    g = \
'''E : T X
X : + E X | 
T : F Y
Y : * T Y | 
F : int | ( E )'''
    g = get_grammar(g)
    print(g)
    fr = first_set_elem(g)
    print''
    print "First set : "
    print fr
    print ''
    fl = follow_set(g)
    print "Follow Set : "
    print fl
    
