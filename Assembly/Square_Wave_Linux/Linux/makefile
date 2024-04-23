OBJS = linux.o
ifdef DEBUG
DEBUGFLGS = -g
else
DEBUGFLGS =
endif

%.o : %.s
	as $(DEBUGFLGS) $< -o $@
GPIO_ON_OFF: $(OBJS)
	gcc -o GPIO_ON_OFF $(OBJS)

clean:
	rm *.o GPIO_ON_OFF
