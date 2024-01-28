int: n = 5;

array[1..n] of var 0..3: arr;

constraint arr[1] = 0;
constraint arr[n] = 3;
constraint forall(i in 1..n - 1) (arr[i] + arr[i + 1] <= 3);

constraint forall(i in 1..n where i mod 3 == 0) (arr[i] >= 2);

solve maximize sum(arr);

output ["x = ", show(arr)];