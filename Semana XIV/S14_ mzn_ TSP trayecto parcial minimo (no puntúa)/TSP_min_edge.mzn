%TSP trayecto parcial mínimo

include "globals.mzn";
int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

% distancia entre ciudades 
% -1 significa que no hay conexión directa
array[City,City] of int: distance; 

% Introducir el codigo a partir de aqui ------------------------------------------
array[1..numCities] of var 1..numCities: succ;
var 0..maxAllowedEdge: maxEdge;

constraint circuit(succ);
constraint forall(city in 1..numCities) (distance[city, succ[city]] <= maxEdge);
constraint forall(i in 1..numCities, j in 1..numCities) (distance[i, j] == -1 -> succ[i] != j);

solve minimize maxEdge;