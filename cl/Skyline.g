grammar Skyline;

root: expr EOF;

expr : LPAR expr RPAR
	| MINUS expr
	| expr MULT expr
	| expr PLUS expr
	| expr MINUS expr
	| expr ASSIGNMENT expr
	| SIMPLE
	| LIST
	| RANDOM
	| IDENTIFIER
	| INTEGER
;



IDENTIFIER : [a-zA-Z][0-9a-zA-Z]*;
MINUS : '-';
MULT : '*';
PLUS : '+';
LPAR : '(';
RPAR : ')';
INTEGER : '-'?[0-9][0-9]*;
ASSIGNMENT : ':=';
SIMPLE : '(' INTEGER ','' '? INTEGER ','' '? INTEGER ')';
LIST : ('[' (SIMPLE','' '?)* SIMPLE ']') | '[]';
RANDOM : '{' INTEGER ','' '? INTEGER ','' '? INTEGER ','' '? INTEGER ','' '? INTEGER '}'; 
WS : [ \n] + -> skip;
