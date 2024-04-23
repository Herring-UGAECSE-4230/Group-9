@ Constants for GPIO22
@ GPFSEL2 [Offset: 0x08] responsible for GPIO Pins 20 to 29
@ GPCLR0 [Offset: 0x28] responsible for GPIO Pins 0 to 31
@ GPSET0 [Offset: 0x1C] responsible for GPIO Pins 0 to 31

@ Sleep control variables
.equ    On_time,   228           @ 2MHz
.equ    Off_time,  228 

@ GPIO22 Related
.equ    GPFSEL2, 0x08   @ function register offset
.equ    GPCLR0, 0x28    @ clear register offset
.equ    GPSET0, 0x1c    @ set register offset
.equ    GPFSEL2_GPIO22_MASK, 0b111000000   @ Mask for fn register (bit 7-6)
.equ    MAKE_GPIO22_OUTPUT, 0b001000000     @ use pin for output (bit 7)
.equ    PIN, 22                          @ Used to set PIN high / low

@ Args for mmap
.equ    OFFSET_FILE_DESCRP, 0   @ file descriptor
.equ    mem_fd_open, 3
.equ    BLOCK_SIZE, 4096        @ Raspbian memory page
.equ    ADDRESS_ARG, 3          @ device address

@ Misc
.equ    SLEEP_IN_S, 1            @ sleep one second

@ The following are defined in /usr/include/asm-generic/mman-common.h:
.equ    MAP_SHARED, 1    @ share changes with other processes
.equ    PROT_RDWR, 0x3   @ PROT_READ(0x1)|PROT_WRITE(0x2)

@ Constant program data
.section .rodata
device:
    .asciz  "/dev/gpiomem"

@ The program
.text
.global main
main:
@ Open /dev/gpiomem for read/write and syncing
    ldr     r1, O_RDWR_O_SYNC   @ flags for accessing device
    ldr     r0, mem_fd          @ address of /dev/gpiomem
    bl      open
    mov     r4, r0              @ use r4 for file descriptor

@ Map the GPIO registers to a main memory location so we can access them
@ mmap(addr[r0], length[r1], protection[r2], flags[r3], fd[r4])
    str     r4, [sp, #OFFSET_FILE_DESCRP]   @ r4=/dev/gpiomem file descriptor
    mov     r1, #BLOCK_SIZE                 @ r1=get 1 page of memory
    mov     r2, #PROT_RDWR                  @ r2=read/write this memory
    mov     r3, #MAP_SHARED                 @ r3=share with other processes
    mov     r0, #mem_fd_open                @ address of /dev/gpiomem
    ldr     r0, GPIO_BASE                   @ address of GPIO
    str     r0, [sp, #ADDRESS_ARG]          @ r0=location of GPIO
    bl      mmap
    mov     r5, r0           @ save the virtual memory address in r5

@ Set up the GPIO pin function register in programming memory
    add     r0, r5, #GPFSEL2            @ calculate address for GPFSEL2
    ldr     r2, [r0]                    @ get entire GPFSEL2 register
    bic     r2, r2, #GPFSEL2_GPIO22_MASK@ clear pin field for GPIO22
    orr     r2, r2, #MAKE_GPIO22_OUTPUT @ enter function code for GPIO22
    str     r2, [r0]                    @ update register

loopOn:
@ Turn GPIO22 on 
    add     r0, r5, #GPSET0 @ calc GPSET0 address

    mov     r3, #1          @ turns on bit
    lsl     r3, r3, #PIN    @ shift bit to pin position
    orr     r2, r2, r3      @ sets bit
    str     r2, [r0]        @ update register

    ldr     r6, =On_time


@Turn GPIO22 off
    add     r0, r5, #GPCLR0 @ calc GPSET0 address

    mov     r3, #1          @ turns off bit
    lsl     r3, r3, #PIN    @ shift bit to pin position
    orr     r2, r2, r3      @ sets bit
    str     r2, [r0]        @ update register

    ldr     r6, =Off_time

delayOff:
    subs    r6,r6, #1
    bne     delayOff
    b       loopOn          @ branching to on loop after delay 
     
delayOn:
    subs    r6,r6, #1
    bne     delayOn
    b       loopOff         @ branching to off loop after delay 
  

GPIO_BASE:
    .word   0xfe200000  @ GPIO Base address Raspberry Pi 4
mem_fd:
    .word   device
O_RDWR_O_SYNC:
    .word   2|256       @ O_RDWR (2)|O_SYNC (256)
