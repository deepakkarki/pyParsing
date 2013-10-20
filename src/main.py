##############
##  Expected layout of main file
##	 - import re and ll_parse_tools
##   	 - scanner (lexical) specs
##   	 - Grammar specs
##	Now to make it work
##	 - call get_parser, get a LL(1) parser object
##	 - call get_input, get input in desired form
##	 - call parse on the parser, feed it the input
##############

#import statements
from ll_parse_tools import *

#scanner (lexical) specs
scanner = re.Scanner([
    (r"[a-zA-Z_]\w*", lambda x, y: 'ID'),
    (r"\+", lambda x, y: 'PLUS'),
    (r"\*", lambda x, y: 'TIMES'),
    (r"\(", lambda x, y: '('),
    (r"\)", lambda x, y: ')'),
    (r"[0-9]+", lambda x, y: 'INT'),
    (r"\s+", None),
    ])

#Grammar specs 
g = \
'''E : T X
X : PLUS E X | 
T : F Y
Y : TIMES T Y | 
F : INT | ( E ) | ID'''


#making it work
data = '(1+2)*3+x'
parser = get_parser(g)
input = get_input(scanner, data)
result = parser.parse(input)
print result
