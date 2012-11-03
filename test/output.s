.section .data
cpma: .int 0
.section .text
.globl   main
main:
pushl %ebp
movl %esp,%ebp
subl $24,%esp
movl $0,%ebx
movl $76, -24(%ebp,%ebx,4)
movl $1,%ebx
movl $82, -24(%ebp,%ebx,4)
movl $2,%ebx
movl $90, -24(%ebp,%ebx,4)
movl $3,%ebx
movl $86, -24(%ebp,%ebx,4)
movl $4,%ebx
movl $79, -24(%ebp,%ebx,4)
movl $5,%ebx
movl $62, -24(%ebp,%ebx,4)
subl $24,%esp
movl $0,%ebx
movl $2, -48(%ebp,%ebx,4)
movl $1,%ebx
movl $2, -48(%ebp,%ebx,4)
movl $2,%ebx
movl $1, -48(%ebp,%ebx,4)
movl $3,%ebx
movl $2, -48(%ebp,%ebx,4)
movl $4,%ebx
movl $2, -48(%ebp,%ebx,4)
movl $5,%ebx
movl $3, -48(%ebp,%ebx,4)
subl $4,%esp
subl $4,%esp
subl $4,%esp
subl $4,%esp
subl $4,%esp
pushl $msg0
call printf
addl $4,%esp
leal -52(%ebp),%eax
pushl %eax
pushl $msg1
call scanf
addl $8,%esp
movl $0,-56(%ebp)
movl $0,-64(%ebp)
movl $0,-68(%ebp)
for_start0:
movl -68(%ebp),%eax
movl $6,%ebx
cmp %ebx,%eax
jae for_end0
movl -68(%ebp),%ecx
movl -24(%ebp,%ecx,4),%eax
movl -68(%ebp),%ecx
movl -48(%ebp,%ecx,4),%ebx
mull %ebx
movl %eax,cpma
movl -56(%ebp),%eax
movl cpma,%ebx
addl %ebx,%eax
movl %eax,cpma
movl cpma,%ecx
movl %ecx,-56(%ebp)
movl -64(%ebp),%eax
movl -68(%ebp),%ecx
movl -48(%ebp,%ecx,4),%ebx
addl %ebx,%eax
movl %eax,cpma
movl cpma,%ecx
movl %ecx,-64(%ebp)
addl $1,-68(%ebp)
jmp for_start0
for_end0:
movl -56(%ebp),%eax
movl -64(%ebp),%ebx
divl %ebx
movl %eax,cpma
movl cpma,%ecx
movl %ecx,-60(%ebp)
movl -60(%ebp),%eax
movl $60,%ebx
cmp %ebx,%eax
jb else_start1
movl -60(%ebp),%eax
movl $60,%ebx
subl %ebx,%eax
movl %eax,cpma
movl cpma,%ecx
movl %ecx,-60(%ebp)
pushl -60(%ebp)
pushl -52(%ebp)
pushl $msg2
call printf
addl $12,%esp
jmp else_end1
else_start1:
movl $60,%eax
movl -60(%ebp),%ebx
subl %ebx,%eax
movl %eax,cpma
movl cpma,%ecx
movl %ecx,-60(%ebp)
pushl -60(%ebp)
pushl -52(%ebp)
pushl $msg3
call printf
addl $12,%esp
else_end1:
movl $1,%eax
movl $0,%ebx
int $0x80
msg0: .asciz "please input your student number:"
msg1: .asciz "%d"
msg2: .asciz "the score of student number %d is %d higher than 60.\n"
msg3: .asciz "the score of student number %d is %d lower than 60.\n"
