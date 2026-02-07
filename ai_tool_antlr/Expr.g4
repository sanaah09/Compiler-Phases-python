grammar Expr;

program : statement+ ;

statement : ID '=' expr ';' ;

expr
    : expr ('+'|'-') expr
    | INT
    | ID
    ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
