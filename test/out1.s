.section .data
tmp0: .int 0
tmp1: .int 0
tmp2: .int 0
tmp3: .int 0
tmp4: .int 0
tmp5: .int 0
tmp6: .int 0
tmp7: .int 0
tmp8: .int 0
.section .text
.globl main
main:
pushl %ebp
movl %esp, %ebp
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
pushl $LC0
call printf
addl $4,%esp
leal -52(%ebp),%eax
pushl %eax
pushl $LC1
call scanf
addl $8,%esp
movl $0,-60(%ebp)
movl $0,-64(%ebp)
movl $0,-68(%ebp)
start_for:
movl -68(%ebp), %eax
movl $6,%ebx
cmp %ebx,%eax
jae end_for
movl -68(%ebp),%edx
movl -24(%ebp,%edx,4), %eax
movl %eax, tmp0
movl -68(%ebp),%edx
movl -48(%ebp,%edx,4), %eax
movl %eax, tmp1
movl tmp0,%eax
movl tmp1,%ebx
mull %ebx
movl %eax,tmp2
movl -60(%ebp),%eax
movl tmp2,%ebx
addl %ebx,%eax
movl %eax,tmp3
movl tmp3,%eax
movl %eax,-60(%ebp)
movl -68(%ebp),%edx
movl -48(%ebp,%edx,4), %eax
movl %eax, tmp4
movl -64(%ebp),%eax
movl tmp4,%ebx
addl %ebx,%eax
movl %eax,tmp5
movl tmp5,%eax
movl %eax,-64(%ebp)
addl $1,-68(%ebp)
jmp start_for
end_for:
movl -60(%ebp),%eax
movl -64(%ebp),%ebx
divl %ebx
movl %eax,tmp6
movl tmp6,%eax
movl %eax,-56(%ebp)
movl -56(%ebp),%eax
movl $60, %ebx
cmp %ebx, %eax
jb else
movl -56(%ebp),%eax
movl $60,%ebx
subl %ebx,%eax
movl %eax,tmp7
movl tmp7,%eax
movl %eax,-56(%ebp)
pushl -52(%ebp)
pushl -56(%ebp)
pushl $LC2
call printf
addl $12,%esp
jmp end
else:
movl $60,%eax
movl -56(%ebp),%ebx
subl %ebx,%eax
movl %eax,tmp8
movl tmp8,%eax
movl %eax,-56(%ebp)
pushl -52(%ebp)
pushl -56(%ebp)
pushl $LC3
call printf
addl $12,%esp
jmp end
end:
movl $1, %eax
movl $0, %ebx
int $0x80
LC0: .asciz "please input your student number:"
LC1: .asciz "%d"
LC2: .asciz "the score of student number %d is %d higher than 60.\n"
LC3: .asciz "the score of student number %d is %d lower than 60.\n"
