# cat>>demo.l
'''%{ 
int n = 0 ; 
%} 
%% 
"while"|"if"|"else" {n++;printf("\t keywords : %s", yytext);} 
"int"|"float" {n++;printf("\t keywords : %s", yytext);} 
[a-zA-Z_][a-zA-Z0-9_]* {n++;printf("\t identifier : %s", yytext);} 
"<="|"=="|"="|"++"|"-"|"*"|"+" {n++;printf("\t operator : %s", yytext);} 
[(){}|, ;] {n++;printf("\t separator : %s", yytext);} 
[0-9]*"."[0-9]+ {n++;printf("\t float : %s", yytext);} 
[0-9]+ {n++;printf("\t integer : %s", yytext);}						 
"end" {printf("\n total no. of token = %d\n", n);} 
%% 
int main() 
{ 
	yylex(); 
}
int yywrap () {
	return 1;
}
'''
# sudo apt install flex
# flex demo.l
# gcc lex.yy.c 
# ./a.out
# -------------------------------------------------------------------------------------

# cat>>demo.l
'''%{
#define Number 1
#define Key 2
#define Header 3
#define ID 4
#define Symbol 5
%}

%%
[0-9]+|[0-9]+\.[0-9]+ { return Number; }
auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while { return Key; }
#include\s*<([a-zA-Z0-9]+\.[a-zA-Z0-9]+)> { return Header; }
[a-zA-Z]+[a-zA-Z0-9]* { return ID; }
[+*/=%;-] { return Symbol; }

%%

#include <stdio.h>

int main(int argc, char *argv[]) {
    int val;
    while ((val = yylex()) != 0) { // Check for non-zero return (valid token)
        switch (val) {
            case Number:
                printf("\n %s: Number", yytext);
                break;
            case Key:
                printf("\n %s: Keyword", yytext);
                break;
            case Header:
                printf("\n %s: Header", yytext);
                break;
            case ID:
                printf("\n %s: Identifier", yytext);
                break;
            case Symbol:
                printf("\n %s: Symbol", yytext);
                break;
        }
    }
    return 0; // Indicate successful program termination
}
'''
# sudo apt install flex
# flex demo.l
# gcc lex.yy.c 
# ./a.out

# 0r-------------------------
# Follow this below flow:->
# 1. gedit demo.l
# 2. flex demo.l
# 3. gcc lex.yy.c
# 4. ./a.out (in ubuntu)
# 4. a.exe (in windows)
# 5. int i = 1000;