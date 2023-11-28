grammar Command;

/* Parser Rules*/

command
    : table_management
    | query
    ;

table_management
    : 'create' ATTRNAME 'with' tbl_attributes   #createTable
    | 'delete' ATTRNAME                         #deleteTable
    ;

tbl_attributes
    : ATTRNAME TYPE (',' ATTRNAME TYPE)*
    ;

query
   : '(' query ')'                              #parenExp
   | left=query LOGICAL_OPERATOR right=query    #logicalExp
   |  ATTRNAME op=( EQ | NE ) value             #compareExp
   ;

value
   : BOOLEAN           #boolean
   | NULL              #null
   | STRING            #string
   | DOUBLE            #double
   | '-'? INT EXP?     #long
   ;

/* Lexer Rules*/

TYPE
    : 'STRING' | 'INT' | 'BOOLEAN' | 'DOUBLE'
    ;

LOGICAL_OPERATOR
   : 'and' | 'or'
   ;

ATTRNAME
   : ALPHA ATTR_NAME_CHAR* ;

fragment ATTR_NAME_CHAR
   : '-' | '_' | ':' | DIGIT | ALPHA
   ;

fragment DIGIT
   : ('0'..'9')
   ;

fragment ALPHA
   : ( 'A'..'Z' | 'a'..'z' )
   ;

EQ : 'eq' ;
NE : 'ne' ;

BOOLEAN
   : 'true' | 'false'
   ;

STRING
   : '"' (ESC | ~ ["\\])* '"'
   ;
fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
DOUBLE
   : '-'? INT '.' [0-9] + EXP?
   ;
// INT no leading zeros.
INT
   : '0' | [1-9] [0-9]*
   ;
// EXP we use "\-" since "-" means "range" inside [...]
EXP
   : [Ee] [+\-]? INT
   ;
WS : [ \t]+ -> skip ;