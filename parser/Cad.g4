grammar Cad;

// Parser rules
start_ : cmd (';' cmd)* ';'? EOF;
cmd : FILL WS color                                                 #fillCommand
    | BORDER WS color                                               #borderCommand
    | WIDTH WS int                                                  #widthCommand
    | CLEAR WS color                                                #clearCommand

    | LINE WS position WS position                                  #lineCommand
    | RECTANGLE WS position WS size                                 #rectangleCommand
    | ELLIPSE WS position WS size                                   #ellipseCommand
    | POLYGON WS position WS position (WS position)+                #polygonCommand

    | UNDO                                                          #undoCommand
    ;

position : int WS int ;
size : int WS int ;

color : COLOR;
int : INT;

// Lexer rules
COLOR : '#' HEX HEX HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;
INT : [0-9]+ ;

WS : ' ';
NL : [\n\r]+ -> skip ;

// Commands
FILL : 'FILL' ;
BORDER : 'BORDER' ;
WIDTH : 'WIDTH' ;
CLEAR : 'CLEAR' ;
LINE : 'LINE' ;
RECTANGLE : 'RECT' ;
ELLIPSE : 'ELLIPSE' ;
POLYGON : 'POLY' ;
UNDO : 'UNDO' ;