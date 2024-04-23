OBJS = Linux_asm_squarewave.o
ifdef DEBUG
DEBUGFLGS = -g
else
DEBUGFLGS =
endif

%.o : %.s
	as $(DEBUGFLGS) $< -o $@
GPIO: $(OBJS)
	gcc -o GPIO $(OBJS)

clean:
	rm *.o GPIO

