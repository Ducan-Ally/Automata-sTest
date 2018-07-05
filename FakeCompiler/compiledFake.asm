.data
peI: .asciiz "\nInsert digit for pe: "
peO: .asciiz "\nThe value in pe is: "
pI: .asciiz "\nInsert digit for p: "
pO: .asciiz "\nThe value in p is: "
perroI: .asciiz "\nInsert digit for perro: "
perroO: .asciiz "\nThe value in perro is: "
gatyI: .asciiz "\nInsert digit for gaty: "
gatyO: .asciiz "\nThe value in gaty is: "
patoI: .asciiz "\nInsert digit for pato: "
patoO: .asciiz "\nThe value in pato is: "
.text
main:
li $v0, 4
la $a0, peI
syscall
li $v0, 5
syscall
move $s0, $v0
li $v0, 4
la $a0, pI
syscall
li $v0, 5
syscall
move $s1, $v0
li $v0, 4
la $a0, perroI
syscall
li $v0, 5
syscall
move $s2, $v0
li $v0, 4
la $a0, gatyI
syscall
li $v0, 5
syscall
move $s3, $v0
li $v0, 4
la $a0, patoI
syscall
li $v0, 5
syscall
move $s4, $v0
li $v0, 4
la $a0, patoO
syscall
li $v0, 1
move $a0, $s4
syscall
li $v0, 4
la $a0, pO
syscall
li $v0, 1
move $a0, $s1
syscall
li $v0, 4
la $a0, perroO
syscall
li $v0, 1
move $a0, $s2
syscall
li $v0, 4
la $a0, peO
syscall
li $v0, 1
move $a0, $s0
syscall
li $v0, 4
la $a0, gatyO
syscall
li $v0, 1
move $a0, $s3
syscall
li $v0, 10
syscall
