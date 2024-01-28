int: presupuesto = 10000;

var 0..1000: F;
var 0..400: L;
var 0..500: Z;
var 0..150: J;

constraint 13 * F + 21 * L + 17 * Z + 100 * J <= presupuesto;

var int: objetive = 6 * F + 10 * L + 8 * Z + 40 * J;

solve maximize(objetive);

output["F = \(F)\n"];
output["L = \(L)\n"];
output["Z = \(Z)\n"];
output["J = \(J)\n"];