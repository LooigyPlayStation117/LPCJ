#!/bin/bash

echo "CREADOR DE TABLAS DE MULTIPLICAR"
echo "* Introdue un numero: "
read tabla

if [ $tabla -gt 100 ]
then
 echo "Ese es un numero muy grande"
fi

for i in 1 2 3 4 5 6 7 8 9 10
 do
  echo "$tabla x $i= `expr $tabla \* $i`"
 done