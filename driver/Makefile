# Makefile 
obj-m := hello.o     
#creates module object , if you want to create normal object file then do obj-y := hello.o  

all:
	make -C /lib/modules/$(uname -r)/build M=$(PWD) modules  
clean:
	make -C /lib/modules/$(uname -r)/build M=$(PWD) clean  
