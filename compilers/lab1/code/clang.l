/*开启行号*/
%option yylineno
/*禁用默认主函数*/
%option noyywrap
/*不要添加默认规则*/
%option nodefault
/*定义部分*/
%{
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include "stdarg.h"
    int yycolumn = 1;
    enum yytokentype{
        INT = 258, FLOAT , CHAR, BREAK, CONTINUE, 
        IF , ELSE , RETURN, DO , WHILE , FOR,

        CONST_INT,CONST_FLOAT,CONST_CHAR,

        IDN,

        LP , RP , SLP , SRP , BLP , BRP , SEMI , COMMA , ASSIGN,

        REL_OP , AR_OP , LOGIC_OP
    };

    typedef union{
        int type_int;
        float type_float;
        char type_char;
        char type_id[32];
    }YYLVAL;
    #define ECHO fwrite(yytext,yyleng,1,yyout)
    YYLVAL yylval;
%}
/*辅助定义*/
idn [A-Za-z][A-Za-z0-9]*
int [0-9]+
float ([0-9]*\.[0-9]+)|([0-9]+\.)

%%
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

{idn} {strcpy(yylval.type_id,yytext); return IDN;}
{int} {yylval.type_int=atoi(yytext);return CONST_INT;}
{float} {yylval.type_float=atof(yytext); return CONST_FLOAT;}

">"|"<"|">="|"<="|"=="|"!=" {strcpy(yylval.type_id,yytext); return REL_OP;}
"+"|"-"|"+="|"-="|"++"|"--"|"*"|"/" {strcpy(yylval.type_id,yytext); return AR_OP;}
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
    if((f_o = fopen(out_file,"a+")) == NULL){
        fprintf(stderr,"Can't open %s\n",out_file);
        return (1);
    }

    int tok;
    while(tok = yylex()){
        switch(tok){
            case INT:{
                fprintf(f_o,"< INT%d, - >\n",tok);
                break;
            }
            case FLOAT:{
                fprintf(f_o,"< FLOAT%d, - >\n",tok);
                break;
            }
            case CHAR:{
                fprintf(f_o,"< CHAR%d, - >\n",tok);
                break;
            }
            case BREAK:{
                fprintf(f_o,"< BREAK%d, - >\n",tok);
                break;
            }
            case CONTINUE:{
                fprintf(f_o,"< CONTINUE%d, - >\n",tok);
                break;
            }
            case IF:{
                fprintf(f_o,"< IF%d, - >\n",tok);
                break;
            }
            case ELSE:{
                fprintf(f_o,"< ELSE%d, - >\n",tok);
                break;
            }
            case RETURN:{
                fprintf(f_o,"< RETURN%d, - >\n",tok);
                break;
            }
            case DO:{
                fprintf(f_o,"< DO%d, - >\n",tok);
                break;
            }
            case WHILE:{
                fprintf(f_o,"< WHILE%d, - >\n",tok);
                break;
            }
            case FOR:{
                fprintf(f_o,"< FOR%d, - >\n",tok);
                break;
            }
            case CONST_INT:{
                fprintf(f_o,"< CONST_INT%d, %d >\n",tok,yylval.type_int);
                break;
            }
            case CONST_FLOAT:{
                fprintf(f_o,"< CONST_FLOAT%d, %f >\n",tok,yylval.type_float);
                break;
            }
            case CONST_CHAR:{
                fprintf(f_o,"< CONST_CHAR%d, %c >\n",tok,yylval.type_char);
                break;
            }
            case IDN:{
                fprintf(f_o,"< IDN%d, %s >\n",tok,yylval.type_id);
                break;
            }
            case LP:{
                fprintf(f_o,"< LP%d, - >\n",tok);
                break;
            }
            case RP:{
                fprintf(f_o,"< RP%d, - >\n",tok);
                break;
            }
            case SLP:{
                fprintf(f_o,"< SLP%d, - >\n",tok);
                break;
            }
            case SRP:{
                fprintf(f_o,"< SRP%d, - >\n",tok);
                break;
            }
            case BLP:{
                fprintf(f_o,"< BLP%d, - >\n",tok);
                break;
            }
            case BRP:{
                fprintf(f_o,"< BRP%d, - >\n",tok);
                break;
            }
            case SEMI:{
                fprintf(f_o,"< SEMI%d, - >\n",tok);
                break;
            }
            case COMMA:{
                fprintf(f_o,"< COMMA%d, - >\n",tok);
                break;
            }
            case ASSIGN:{
                fprintf(f_o,"< ASSIGN%d, - >\n",tok);
                break;
            }
            case REL_OP:{
                fprintf(f_o,"< REL_OP%d, %s >\n",tok,yylval.type_id);
                break;
            }
            case AR_OP:{
                fprintf(f_o,"< AR_OP%d, %s >\n",tok,yylval.type_id);
                break;
            }
            case LOGIC_OP:{
                fprintf(f_o,"< LOGIC_OP%d, %s >\n",tok,yylval.type_id);
                break;
            }
        }
        //fprintf(f_o,"%d",tok);
        //if(tok == CONST_INT){
        // fprintf(f_o," = %d\n",yylval.type_int);
        //}
        //else fprintf(f_o,"\n");
    }
    fclose(f_o);
    return 0;
}

