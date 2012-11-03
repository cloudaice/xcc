.section .data
temp0: .int 0
temp1: .int 0
temp2: .int 0
temp3: .int 0
temp4: .int 0
temp5: .int 0
temp6: .int 0
temp7: .int 0
temp8: .int 0
temp9: .int 0
temp10: .int 0
.section .text
.globl   main
main:
pushl %ebp
movl %esp,%ebp
L0:
subl $24, %esp
movl $0, %edx
L1:
movl $0, %edx
movl $76, -24(%ebp, %edx, 4)
L2:
movl $1, %edx
movl $82, -24(%ebp, %edx, 4)
L3:
movl $2, %edx
movl $90, -24(%ebp, %edx, 4)
L4:
movl $3, %edx
movl $86, -24(%ebp, %edx, 4)
L5:
movl $4, %edx
movl $79, -24(%ebp, %edx, 4)
L6:
movl $5, %edx
movl $62, -24(%ebp, %edx, 4)
L7:
subl $24, %esp
movl $0, %edx
L8:
movl $0, %edx
movl $2, -48(%ebp, %edx, 4)
L9:
movl $1, %edx
movl $2, -48(%ebp, %edx, 4)
L10:
movl $2, %edx
movl $1, -48(%ebp, %edx, 4)
L11:
movl $3, %edx
movl $2, -48(%ebp, %edx, 4)
L12:
movl $4, %edx
movl $2, -48(%ebp, %edx, 4)
L13:
movl $5, %edx
movl $3, -48(%ebp, %edx, 4)
L14:
subl $4, %esp
L15:
subl $4, %esp
L16:
subl $4, %esp
L17:
subl $4, %esp
L18:
subl $4, %esp
L19:
pushl $msg0
call printf
addl $4, %esp
L20:
leal -52(%ebp), %eax
pushl %eax
pushl $msg1
call scanf
addl $8, %esp
L21:
movl $0,%eax
movl %eax,-60(%ebp)
L22:
movl $0,%eax
movl %eax,-64(%ebp)
L23:
movl $0,%eax
movl %eax,-68(%ebp)
L24:
movl -68(%ebp), %eax
movl $6, %ebx
cmp %eax, %ebx
ja L26
L25:
jmp L37
L26:
movl -68(%ebp), %eax
movl $1, %ebx
addl %ebx, %eax
movl %eax, temp0
L27:
movl -68(%ebp), %edx
movl -24(%ebp, %edx, 4), %eax
movl %eax, temp1
L28:
movl -68(%ebp), %edx
movl -48(%ebp, %edx, 4), %eax
movl %eax, temp2
L29:
movl temp1, %eax
movl temp2, %ebx
mull %ebx
movl %eax, temp3
L30:
movl -60(%ebp), %eax
movl temp3, %ebx
addl %ebx, %eax
movl %eax, temp4
L31:
movl temp4,%eax
movl %eax,-60(%ebp)
L32:
movl -68(%ebp), %edx
movl -48(%ebp, %edx, 4), %eax
movl %eax, temp5
L33:
movl -64(%ebp), %eax
movl temp5, %ebx
addl %ebx, %eax
movl %eax, temp6
L34:
movl temp6,%eax
movl %eax,-64(%ebp)
L35:
movl temp0,%eax
movl %eax,-68(%ebp)
L36:
jmp L24
L37:
movl $0, %edx
movl -60(%ebp), %eax
movl -64(%ebp), %ebx
divl %ebx
movl %eax, temp7
L38:
movl temp7,%eax
movl %eax,-56(%ebp)
L39:
movl -56(%ebp), %eax
movl $60, %ebx
cmp %eax, %ebx
jbe L41
L40:
jmp L50
L41:
movl -56(%ebp), %eax
movl $70, %ebx
cmp %eax, %ebx
jb L43
L42:
jmp L45
L43:
pushl -56(%ebp)
pushl $msg2
call printf
addl $8, %esp
L44:
jmp L46
L45:
pushl -56(%ebp)
pushl $msg3
call printf
addl $8, %esp
L46:
movl -56(%ebp), %eax
movl $60, %ebx
subl %ebx, %eax
movl %eax, temp8
L47:
movl temp8,%eax
movl %eax,-56(%ebp)
L48:
pushl -56(%ebp)
pushl -52(%ebp)
pushl $msg4
call printf
addl $12, %esp
L49:
jmp L53
L50:
movl $60, %eax
movl -56(%ebp), %ebx
subl %ebx, %eax
movl %eax, temp9
L51:
movl temp9,%eax
movl %eax,-56(%ebp)
L52:
pushl -56(%ebp)
pushl -52(%ebp)
pushl $msg5
call printf
addl $12, %esp
L53:
movl -68(%ebp), %eax
movl $11, %ebx
cmp %eax, %ebx
jae L55
L54:
jmp L59
L55:
pushl -68(%ebp)
pushl $msg6
call printf
addl $8, %esp
L56:
movl -68(%ebp), %eax
movl $2, %ebx
addl %ebx, %eax
movl %eax, temp10
L57:
movl temp10,%eax
movl %eax,-68(%ebp)
L58:
jmp L53
L59:
movl $1, %eax
movl $0, %ebx
int $0x80
msg0: .string "please input your student number:"
msg1: .asciz "%d"
msg2: .asciz "mean is%d > 70\n"
msg3: .asciz "mean is%d\n < 70"
msg4: .asciz "the score of student number %d is %d higher than 60.\n"
msg5: .asciz "the score of student number %d is %d lower than 60.\n"
msg6: .asciz "i is %d\n"
