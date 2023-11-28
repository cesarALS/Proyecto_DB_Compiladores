grammar Command;

/* Parser Rules*/

command
    : table_management
    | query
    ;

table_management
    : 'create table' OBJNAME 'with' tbl_attributes   #createTable
    | 'delete table' OBJNAME                         #deleteTable
    ;

tbl_attributes
    : OBJNAME TYPE (',' OBJNAME TYPE)*
    ;

query
   : '(' query ')'                              #parenExp
   | left=query LOGICAL_OPERATOR right=query    #logicalExp
   |  OBJNAME op=( EQ | NE ) value              #compareExp
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

EQ : 'eq' ;
NE : 'ne' ;

BOOLEAN
   : 'true' | 'false'
   ;

OBJNAME
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