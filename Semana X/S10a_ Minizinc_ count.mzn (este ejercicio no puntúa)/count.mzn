var 100..500: army;

constraint army mod 5 = 2;
constraint army mod 7 = 2;
constraint army mod 12 = 1;

solve satisfy;

output ["army = \(army)\t"];