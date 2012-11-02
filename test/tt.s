#-*-coding:utf-8-*-
.section .data
a: .int 4
.section .bss
.lcomm b, 2
.section .text
.globl    _start
_start:
movl $1, %eax
movl $0, %ebx
int $0x80
