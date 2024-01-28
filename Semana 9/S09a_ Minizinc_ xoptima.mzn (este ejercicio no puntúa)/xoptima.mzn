var 1..10: x;

constraint x mod 4 == 0;

var int: obj = (x - 7)^2;

solve minimize obj;

output ["x= \(x)\t\nobj=\(obj)\t"];