include "globals.mzn";

int: min_energy;
int: min_protein;
int: max_salt;
int: max_fat;

set of FOOD: desserts;
set of FOOD: mains;
set of FOOD: sides;
enum FEATURE = { name, energy, protein, salt, fat, cost};
enum FOOD;
array[FOOD, FEATURE] of int: dd;

set of FOOD: special_foods;
int: max_special_foods;
int: num_main;                                 % Número de platos principales

array[FEATURE, 1..num_main] of var int: main;  % Ahora es una matriz
array[FEATURE] of var int: side;
array[FEATURE] of var int: dessert;
var 0..infinity: budget;

output [
  if i = 1 then "main= " else ", " endif ++
    show(to_enum(FOOD, main[name,i]))
  | i in 1..num_main
];

output [" side = ", show(to_enum(FOOD,side[name])),
        ", dessert = ", show(to_enum(FOOD,dessert[name])),
        ", cost = ", show(budget), "\n"];

% Escribe el código a partir de aquí ---------------------------------------
constraint forall(i in 1..num_main) (table(main[..,i], dd));
constraint table(side, dd);
constraint table(dessert, dd);

constraint forall(i in 1..num_main) (main[name, i] in mains);
constraint side[name] in sides;
constraint dessert[name] in desserts;

constraint sum(i in 1..num_main) (main[energy, i]) + side[energy] + dessert[energy] >= min_energy;
constraint sum(i in 1..num_main) (main[protein, i]) + side[protein] + dessert[protein] >= min_protein;
constraint sum(i in 1..num_main) (main[salt, i]) + side[salt] + dessert[salt] <= max_salt;
constraint sum(i in 1..num_main) (main[fat, i]) + side[fat] + dessert[fat] <= max_fat;

constraint sum(i in 1..num_main) (main[name, i] in special_foods) +
(side[name] in special_foods) +
(dessert[name] in special_foods)
<= max_special_foods;

constraint alldifferent(main[name, ..]);

budget = sum(i in 1..num_main) (main[cost, i]) + side[cost] + dessert[cost];

solve minimize budget;