all:
	flex clang.l
	gcc lex.yy.c -lfl
run:
	./a.out demo.c
clean:
	rm lex.yy.c
	rm ./a.out
	rm tokens.txt
