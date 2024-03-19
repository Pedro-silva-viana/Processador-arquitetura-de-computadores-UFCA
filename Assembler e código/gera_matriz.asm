.include "macros.asm"
.globl gera_matriz

gera_matriz:

    save_context
    
    move $s0, $a0   #Endereço de início da matriz.
    move $s1, $a1   #Tamanho da matriz.

    li $t0, 0   #i = 0.
for_1:
    bge $t0, $s1, fimFor_1  #Compara se i < $s1.

    li $t1, 0   #j = 0.
for_2:
    bge $t1, $s1, fimFor_2  #Compara se j < $s1.
    li $v0, 42  #Sortear número.
    li $a1, 128 #Limite superior do número.
    syscall
    move $s2, $a0   #Move o resultado para $s2.

    #Calcula a posição.
    sll $t2, $t0, 4 #De antemão já sei que o tamanho da matriz é quatro.
    sll $t3, $t1, 2
    add $t2, $t2, $t3

    add $s3, $t2, $s0
    sw $s2, 0($s3)  #matriz[i][j] = num.

    addi $t1, $t1, 1    #j++.
    j for_2

fimFor_2:
    
    addi $t0, $t0, 1    #j++.
    j for_1

fimFor_1:
    restore_context
    jr $ra  #Retorna para execução normal do programa.
