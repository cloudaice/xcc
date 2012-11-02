	.file	"test.c"
	.section	.rodata
	.align 4
.LC0:
	.string	"please input your student number:"
.LC1:
	.string	"%d"
	.align 4
.LC4:
	.string	"the score of student number %d is %f higher than 60.\n"
	.align 4
.LC5:
    .string	"the score of student number %d is %f lower than 60.\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$112, %esp
	movl	$76, 44(%esp)
	movl	$82, 48(%esp)
	movl	$90, 52(%esp)
	movl	$86, 56(%esp)
	movl	$79, 60(%esp)
	movl	$62, 64(%esp)
	movl	$2, 68(%esp)
	movl	$2, 72(%esp)
	movl	$1, 76(%esp)
	movl	$2, 80(%esp)
	movl	$2, 84(%esp)
	movl	$3, 88(%esp)
	movl	$.LC0, %eax
	movl	%eax, (%esp)
	call	printf
	movl	$.LC1, %eax
	leal	92(%esp), %edx
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	__isoc99_scanf
	movl	$0x00000000, %eax
	movl	%eax, 96(%esp)
	movl	$0, 100(%esp)
	movl	$0, 104(%esp)
	jmp	.L2
.L3:
	movl	104(%esp), %eax
	movl	44(%esp,%eax,4), %edx
	movl	104(%esp), %eax
	movl	68(%esp,%eax,4), %eax
	imull	%edx, %eax
	movl	%eax, 28(%esp)
	fildl	28(%esp)
	flds	96(%esp)
	faddp	%st, %st(1)
	fstps	96(%esp)
	movl	104(%esp), %eax
	movl	68(%esp,%eax,4), %eax
	addl	%eax, 100(%esp)
	addl	$1, 104(%esp)
.L2:
	cmpl	$5, 104(%esp)
	jle	.L3
	fildl	100(%esp)
	flds	96(%esp)
	fdivp	%st, %st(1)
	fstps	108(%esp)
	flds	108(%esp)
	flds	.LC3
	fxch	%st(1)
	fucomip	%st(1), %st
	fstp	%st(0)
	setae	%al
	testb	%al, %al
	je	.L4
	flds	108(%esp)
	flds	.LC3
	fsubrp	%st, %st(1)
	fstps	108(%esp)
	flds	108(%esp)
	movl	92(%esp), %edx
	movl	$.LC4, %eax
	fstpl	8(%esp)
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	printf
	jmp	.L5
.L4:
	flds	.LC3
	fsubs	108(%esp)
	fstps	108(%esp)
	flds	108(%esp)
	movl	92(%esp), %edx
	movl	$.LC5, %eax
	fstpl	8(%esp)
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	printf
.L5:
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.section	.rodata
	.align 4
.LC3:
	.long	1114636288
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits
