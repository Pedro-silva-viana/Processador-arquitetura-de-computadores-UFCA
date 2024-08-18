pega £03, 4     //Tamanho da matriz
pega £04, 0     //i = 0
pega £05, 1     //Valor de salto do for
pega £00, 0     //Começo da matriz A
pega £01, 16    //Começo da matriz B
pega £02, 32    //Começo da matriz C
igual £04, £03, 26      //Compara de i == 4
pega £06, 0     //j = 0
aMimir
aMimir
aMimir
aMimir
igual £06, £03, 14      //Compara de j == 4
aMimir
aMimir
fodaSe £07      //Guarda aleatório em £07
fodaSe £08      //Guarda aleatório em £08
multiplica £09, £04, £03        //£08 = i * 4
somaFoda £09, £06               //£08 += j
somaFoda £10, £00
escreverFoda £07        //Esreve na matriz A
aMimir
aMimir
soma £11, £01, £09
escreverFoda £08        //Escreve na matriz B
soma £06, £06, £05      //j++
vai 12
aMimir
aMimir
aMimir
aMimir
soma £04, £04, £05      //i++
vai 6
aMimir
aMimir
aMimir
aMimir
pega £04, 0     //i = 0
aMimir
aMimir
aMimir
aMimir
igual £04, £03, 47      //Compara se i == 4
pega £06, 0     //j = 0
aMimir
aMimir
aMimir
aMimir
igual £06, £03, 34      //Compara se j == 4
pega £07, 0     //k = 0
aMimir
aMimir
aMimir
pega £08, 0     //Produto = 0
igual £07, £03, 18
aMimir
aMimir
aMimir
multiplica £09, £04, £03
somaFoda £09, £07
somaFoda £09, £00
lerFoda £09
multiplica £10, £07, £03
somaFoda £10, £06
somaFoda £10, £01
lerFoda £10
aMimir
aMimir
aMimir
soma £07, £07, £05      //k++
multiplica £09, £09, £10
somaFoda £08, £08
vai 54
aMimir
aMimir
aMimir
aMimir
multiplica £09, £04, £03
somaFoda £09, £06
somaFoda £09, £02
escreverFoda £08
soma £06, £06, £05      //j++
vai 48
aMimir
aMimir
aMimir
aMimir
soma £04, £04, £05      //i++
vai 42
aMimir
aMimir
aMimir
aMimir