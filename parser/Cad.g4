grammar Cad;

// Parser rules
start_ : cmd (';' cmd)* EOF;
cmd : FILL WS COLOR                     #fillCommand
    | BORDER WS COLOR                   #borderCommand
    | WIDTH WS INT                      #widthCommand
    | CLEAR WS COLOR                    #clearCommand

    | LINE WS position WS position      #lineCommand
    | RECTANGLE WS position WS size     #rectangleCommand
    | ELLIPSE WS position WS size       #ellipseCommand
    ;

position : INT WS INT ;
size : INT WS INT ;
color : COLOR;

// Lexer rules
COLOR : '#' HEX HEX HEX HEX HEX HEX ;
HEX : [0-9a-fA-F] ;
INT : [0-9]+ ;

WS : ' ';
NL : [\n\r]+ -> skip ;

// Commands
FILL : 'FILL' ;
BORDER : 'BORDER' ;
WIDTH : 'WIDTH' ;
CLEAR : 'CLEAR' ;
LINE : 'LINE' ;
RECTANGLE : 'RECTANGLE' ;
ELLIPSE : 'ELLIPSE' ;
EXIT : 'EXIT' ;