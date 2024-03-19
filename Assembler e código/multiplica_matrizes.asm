.include "macros.asm"
.globl muliplica_matrizes

muliplica_matrizes:

    save_context

    move $s0, $a0   #Início da matriz a.
    move $s1, $a1   #Início da matriz b.
    move $s2, $a2   #Início da matriz c.
    move $s3, $a3   #Tamanho das matrizes.

    li $t0, 0   #i = 0.
for_1:
    bge $t0, $s3, fimFor_1  #Compara se i < $s3.

    li $t1, 0   #j = 0.
for_2:
    bge $t1, $s3, fimFor_2  #Compara de j < $s3.

    li $s4, 0   #produto = 0
    li $t2, 0   #k = 0.
for_3:
    bge $t2, $s3, fimFor_3  #Compara se k < $s3.

    #Calcula o endereço.
    sll $t3, $t0, 4
    sll $t4, $t2, 2
    add $t3, $t3, $t4
    add $t4, $t3, $s0
    lw $s5, 0($t4)  #$s5 = a[i][k].

    #Calcula o endereço.
    sll $t3, $t2, 4
    sll $t4, $t1, 2
    add $t3, $t3, $t4
    add $t4, $t3, $s1
    lw $s6, 0($t4)  #$s6 = b[k][j].

    mul $t5, $s5, $s6   #a[i][k] * b[k][j].
    add $s4, $s4, $t5   #produto += a[i][k] * b[k][j].

    addi $t2, $t2, 1    #k++.
    j for_3

fimFor_3:

    #Calcula o endereço.
    sll $t3, $t0, 4
    sll $t4, $t1, 2
    add $t3, $t3, $t4
    add $t4, $t3, $s2
    sw $s4, 0($t4)  #c[i][j] = produto.

    addi $t1, $t1, 1    #j++.
    j for_2

fimFor_2:

    addi $t0, $t0, 1    #i++.
    j for_1

fimFor_1:

    restore_context
    jr $ra  #Retorna para execução normal do programa.
