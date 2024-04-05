pega £00, 15    //Endereço da matriz A.
pega £01, 31   //Endereço da matriz B.
pega £02, 47   //Endereço da matriz C.
pega £03, 4     //Dimensão da matriz.
pega £05, 0     //i = 0.
pega £04, 1     //Valor de salto do for.
aMimir
aMimir
igual £05, £03, 36      //Compara se i == 4.
pega £06, 0     //j = 0.
aMimir
aMimir
aMimir
aMimir
igual £06, £03, 24      //Compara se j == 4.
aMimir
aMimir
fodaSe £07
fodaSe £10
multiplica £08, £05, £03    //£08 = i * 4.
aMimir
aMimir
aMimir
aMimir
soma £08, £08, £06          //£08 = £08 + j.
aMimir
aMimir
aMimir
aMimir
subtrai £11, £00, £08
subtrai £09, £01, £08
aMimir
aMimir
aMimir
aMimir
escrever £07, £11
escrever £10, £09
soma £06, £06, £04
vai 14
aMimir
aMimir
aMimir
aMimir
soma £05, £05, £04
vai 8
aMimir
aMimir
aMimir
aMimir
pega £05, 0
aMimir
aMimir
aMimir
aMimir
igual £05, £03, 72
pega £06, 0
aMimir
aMimir
aMimir
aMimir
igual £06, £03, 59
pega £07, 0     //k = 0.
aMimir
aMimir
aMimir
pega £08, 0     //produto = 0.
igual £07, £03, 31
aMimir
aMimir
aMimir
multiplica £09, £05, £03    //£09 = k * 4?
multiplica £10, £07, £03
aMimir
aMimir
aMimir
soma £09, £09, £07
soma £10, £10, £06
aMimir
aMimir
aMimir
subtrai £09, £00, £09
subtrai £10, £01, £10
aMimir
aMimir
aMimir
ler £09, £09
ler £10, £10
aMimir
aMimir
aMimir
aMimir
multiplica £09, £09, £10
aMimir
aMimir
aMimir
soma £07, £07, £04
soma £08, £08, £09
vai 66
aMimir
aMimir
aMimir
aMimir
multiplica £09, £05, £03
aMimir
aMimir
aMimir
aMimir
soma £09, £09, £06
aMimir
aMimir
aMimir
aMimir
subtrai £09, £02, £09
aMimir
aMimir
aMimir
aMimir
escrever £08, £09
soma £06, £06, £04      //j++.
vai 60
aMimir
aMimir
aMimir
aMimir
soma £05, £05, £04
vai 54
aMimir
aMimir
aMimir
aMimir
aMimir
aMimir
aMimir