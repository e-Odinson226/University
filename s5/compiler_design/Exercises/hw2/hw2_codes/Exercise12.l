%{
#include<stdio.h>
#include<string.h>
  
char replace_with [] = "double";
char replace [] ="float";
%}

%%
[a-zA-Z]+    { if(strcmp(yytext, replace)==0)
                   fprintf(yyout, "%s", replace_with);
                else
                    fprintf(yyout, "%s", yytext);}

[ \n\t]+    {fprintf(yyout, " ");}
.           fprintf(yyout, "%s", yytext);
%%

int yywrap()
{
    return 1;
}
int main()
{
   extern FILE *yyin, *yyout;
   yyin=fopen("inputCode.c", "r");
   yyout=fopen("outputCode.c", "w");     
      yylex();
}