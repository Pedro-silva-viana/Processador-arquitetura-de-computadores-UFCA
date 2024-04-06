main:

    #ALoca a matriz a.
    addi $sp, $sp, -64
    move $s0, $sp

    #ALoca a matriz b.
    addi $sp, $sp, -64
    move $s1, $sp

    #ALoca a matriz c.
    addi $sp, $sp, -64
    move $s2, $sp

    li $a1, 4

    #Gera a matriz a.
    move $a0, $s0
    jal gera_matriz

    #Gera a matriz b.
    move $a0, $s1
    jal gera_matriz

    #Multiplica as matrizes a e b, guardando o resultado em c.
    move $a0, $s0
    move $a1, $s1
    move $a2, $s2
    li $a3, 4
    jal muliplica_matrizes

    #Imprime a matriz a.
    move $a0, $s0
    li $a1, 4
    jal print_matriz

    li $v0, 11
    li $a0, 10
    syscall

    #Imprime a matriz b.
    move $a0, $s1
    li $a1, 4
    jal print_matriz

    li $v0, 11
    li $a0, 10
    syscall

    #Imprime a matriz c.
    move $a0, $s2
    li $a1, 4
    jal print_matriz

    #Desaloca as matrizes.
    addi $sp, $sp, 64
    addi $sp, $sp, 64
    addi $sp, $sp, 64

    li $v0, 10
    syscall
