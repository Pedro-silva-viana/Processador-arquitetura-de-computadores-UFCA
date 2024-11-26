li £00, 4 _ li £08, 0           //Tamanho do vetor, i  = 0
li £01, 1 _ li £09, 0           //valor de incremento, Endereço da matriz A
li £02, 16 _ li £10, 32         //Endereço da matriz B, Endereço da matriz C
bubble _ bubble
equals £08, £00, 19 _ li £13, 0
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
equals £00, £13, 9 _ bubble
bubble _ bubble
random £04 _ random £11
mul £05, £08, £00 _ mul £12, £08, £00
addH £05, £09 _ addH £12, £02
addH £05, £13 _ addH £12, £13
writeH £04 _ bubble
bubble _ add £13, £13, £01         //j += 1
bubble _ bubble
jump 9 _ bubble
write £11, £12 _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
jump 4 _ add £08, £08, £01
bubble _ li £15, 0
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
equals £15, £00, 36 _ li £11, 0
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
equals £11, £00, 25 _ li £12, 0
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ li £13, 0
equals £12, £00, 13 _ bubble
mul £03, £15, £00 _ mul £14, £12, £00
addH £03, £12 _ addH £14, £11
addH £03, £09 _ addH £14, £02
readH £03 _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
read £04, £14 _ add £12, £12, £01
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
jump 39 _ mul £14, £04, £03 
bubble _ addH £13, £13
bubble _ bubble
mul £03, £15, £00 _ bubble
addH £03, £11 _ bubble
addH £03, £10 _ add £11, £11, £01
writeH £13 _ bubble
jump 34 _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ add £15, £15, £01
jump 29 _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble
bubble _ bubble