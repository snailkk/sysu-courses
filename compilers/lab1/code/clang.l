/*开启行号*/
%option yylineno
/*禁用默认主函数*/
%option noyywrap
/*不要添加默认规则*/
%option nodefault
/*定义部分*/
%{
    #include "stdio.h"
    #include "stdlib.h"
    #include "string.h"
    #include "stdarg.h"
    int yycolumn = 1;
    enum yytokentype{
        INT = 258, FLOAT , CHAR, BREAK, CONTINUE, 
        IF , ELSE , RETURN, DO , WHILE , FOR,

        CONST_INT,CONST_FLOAT,CONST_CHAR,

        IDN,

        LP , RP , SLP , SRP , BLP , BRP , SEMI , COMMA

        REL_OP , AR_OP , LOGIC_OP
    };
    typedef union{
        int type_int;
        float type_float;
        char type_char;
        char type_id[32];
    }YYLVAL;
    #define ECHO fwrite(yytext,yyleng,1,yyout)
%}
/*辅助定义*/
id [A-Za-z][A-Za-z0-9]*
int [0-9]+
float ([0-9]*\.[0-9]+)|([0-9]+\.)

%%
 /*注释处理 单行+多行*/
\/\/[^\n]*  {;}
\/\*(\s|.)*?\*\/ {;}

"int" {return INT;}
"float" {return FLOAT;}
"char" {return CHAR;}
"break" {return BREAK;}
"continue" {return CONTINUE;}
"if" {return IF;}
"else" {return ELSE;}
"return" {return RETURN;}
"do" {return DO;}
"while" {return WHILE;}
"for" {return FOR;}

{id} {strcpy(yylval.type_id,yytext); return IDN;}
{int} {yylval.type_int=atoi(yytext);return CONST_INT;}
{float} {yylval.type_float=atof(yytext); return CONST_FLOAT;}

">"|"<"|">="|"<="|"=="|"!=" {strcpy(yylval.type_id,yytext); return REL_OP;}
"+"|"-"|"+="|"-="|"++"|"--"|"*"|"/" {strcpy(yylval.type_id,yytext); return REL_OP;}
"&&"|"||"|"!" {strcpy(yylval.type_id,yytext); return LOGIC_OP;}

";" {return SEMI;}
"," {return COMMA;}
"=" {return ASSIGN;}
"(" {return LP;}
")" {return RP;}
"[" {return SLP;}
"]" {return SRP;}
"{" {return BLP;}
"}" {return BRP;}

[\n] {yycolumn=1;}
[ \r\t] {;}
.   {printf("Error type A: Mysterious character\"%s\" at line %d,column %d\n",yytext,yylineno,yycolumn);}


%%
int  main(int argc,char *argv[]){
    if(argc > 1){
        if(!(yyin = fopen(argv[1],"r"))){
            perror(argv[1]);
            return (1);
        }
    }
    char out_file[100] = "tokens.txt";
    FILE *f_o;
    if(f_o = fopen(out_file,"a+") == NULL){
        fprintf(stderr,"Can't open %s\n",out_file);
        return 0;
    }

    int tok;
    while(tok == yylex()){
        printf("%d",tok);
        if(tok == CONST_INT) printf(" = %d\n",yylval.type_int);
        else printf("\n");
    }
    fclose(f_o);
    return 0;
}

