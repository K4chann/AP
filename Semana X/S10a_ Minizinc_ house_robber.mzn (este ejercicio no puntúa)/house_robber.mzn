int: n;
array[1..n] of int: value;

array[1..n] of var 0..1: taken;

constraint forall (i in 1..n - 1) (taken[i] + taken [i + 1] <= 1);

var int: total = sum(i in 1..n) (taken[i] * value[i]);
solve maximize total;

output ["taken = ", show(taken)];
output ["Total Value = \(total)\t"];