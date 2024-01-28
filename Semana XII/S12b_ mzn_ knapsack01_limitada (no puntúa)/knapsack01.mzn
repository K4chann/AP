int:n;                    % numero maximo de items
int: capacity;            % capacidad de la mochila

set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

set of ITEMS: limitation;
int:m;                    % Numero maximo de items a elegir dentro del 
                          % conjuto limitation

% Escribe el código a partir de aquí ----------------------------------
var set of ITEMS: taken;
var int: total_weight = sum(item in taken)(weight[item]);
var int: benefit = sum(item in taken)(value[item]);

constraint total_weight <= capacity;
constraint card(taken intersect limitation) <= m;

solve maximize benefit;

output [show(taken), "\n", show(benefit)];