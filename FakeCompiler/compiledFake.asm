.data
es42I: .asciiz "Insert digit for es42: "
es42O: .asciiz "The value in es42 is: "
orden_66I: .asciiz "Insert digit for orden_66: "
orden_66O: .asciiz "The value in orden_66 is: "
ornitorrincoI: .asciiz "Insert digit for ornitorrinco: "
ornitorrincoO: .asciiz "The value in ornitorrinco is: "
.text
main:
li $v0, 4
la $a0, es42I
syscall
li $v0, 5
syscall
move $s0, $v0
li $v0, 4
la $a0, orden_66I
syscall
li $v0, 5
syscall
move $s1, $v0
li $v0, 4
la $a0, ornitorrincoI
syscall
li $v0, 5
syscall
move $s2, $v0
li $v0, 4
la $a0, es42O
syscall
li $v0, 1
move $a0, $s0
syscall
li $v0, 4
la $a0, ornitorrincoO
syscall
li $v0, 1
move $a0, $s2
syscall
li $v0, 4
la $a0, orden_66O
syscall
li $v0, 1
move $a0, $s1
syscall
li $v0, 10
syscall
