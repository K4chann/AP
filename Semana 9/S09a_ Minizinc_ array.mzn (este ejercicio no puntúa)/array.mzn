int: n = 5;

%Introduzca el código a partir de esta línea

array[1..n] of var 1..9: x;

constraint sum(x) == product(x);

constraint forall (i in 2..n) (x[i] >= x[i - 1]);

var int: obj = sum(x);

solve maximize obj;

output ["x = array1d(1..\(n)\t, \([x[i] | i in 1..n])\t"];