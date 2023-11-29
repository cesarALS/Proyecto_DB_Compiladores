/* Lexer y parser del lenguaje del DBMS */

grammar Command;

/* Parser Rules*/

/* Esta es la producción de entrada */
command
    : table_management
    | query
    ;

table_management
    : 'CREAR TABLA'    OBJNAME 'CON' '{' tbl_attributes '}'  #createTable
    | 'ELIMINAR TABLA' OBJNAME                               #deleteTable
    | 'INSERTAR EN'    OBJNAME '{' value (',' value)* '}'    #insertRegister
    ;

tbl_attributes
    : OBJNAME TYPE (',' OBJNAME TYPE)*              #attrDeclaration
    ;

query
   : 'CONSULTAR' OBJNAME ('DONDE' left=atomic_query)?        #logicalQuery
   ;

atomic_query
    : '(' atomic_query ')'                                  #parenQuery
    | OBJNAME COMPARISON_OPERATOR value                     #compareQuery
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
    : 'CAD' | 'ENT' | 'BOOL' | 'DEC'
    ;

//LOGICAL_OPERATOR
//   : 'Y' | 'O'
//   ;

COMPARISON_OPERATOR
    : '=='
    | '!='
    ;


BOOLEAN
   : 'CIERTO' | 'FALSO'
   ;

NULL
    : 'NULO'
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
   | '\'' (ESC | ~ ["\\])* '\''
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

