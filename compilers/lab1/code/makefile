all:
	flex clang.l
	gcc -o clang.out lex.yy.c -lfl
run:
	./clang.out demo.c
clean:
	rm lex.yy.c
	rm tokens.txt
	rm ./clang.out
