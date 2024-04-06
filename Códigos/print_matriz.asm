.include "macros.asm"
.globl print_matriz

print_matriz:
    save_context

    move $s0, $a0   #Endereço do começo da matriz.
    move $s1, $a1   #Tamanho da matriz.

    li $t0, 0   #i = 0.
for_1:
    bge $t0, $s1, fimFor_1  #Compara se i < $s1.

    li $t1, 0   #j = 0.
for_2:
    bge $t1, $s1, fimFor_2  #Compara se j < $s1.

    sll $t2, $t0, 4 #De antemão já sei que o tamanho da matriz é quatro.
    sll $t3, $t1, 2
    add $t2, $t2, $t3
    add $t2, $t2, $s0
    lw $s2, 0($t2)  #$s2 = matriz[i][j].

    #Imprime um inteiro.
    move $a0, $s2
    li $v0, 1
    syscall

    #Imprime um espaço.
    li $a0, 32
    li $v0, 11
    syscall

    addi $t1, $t1, 1    #j++.
    j for_2

fimFor_2:

    #Pula a linha.
    li $a0, 10
    li $v0, 11
    syscall

    addi $t0, $t0, 1    #i++;
    j for_1

fimFor_1:

    restore_context
    jr $ra  #Retorna para execução normal do programa.
