include "globals.mzn";

enum Women;
enum Men;

array[Women, Men] of int: wrank;
array[Men, Women] of int: mrank;

array[Men] of var Women: wife;
array[Women] of var Men: husband;

constraint inverse(wife, husband);
constraint forall (m in Men, w in Women)(mrank[m, w] < mrank[m, wife[m]] -> wrank[w, husband[w]] < wrank[w, m]);
constraint forall (m in Men, w in Women)(wrank[w, m] < wrank[w, husband[w]] -> mrank[m, wife[m]] < mrank[m, w]);
 
var int: obj_men = sum(m in Men) (mrank[m, wife[m]] == 1);
var int: obj_women = sum(w in Women) (wrank[w, husband[w]] == 1);

solve maximize obj_women;

output ["wife = ", show(wife), "\n"];
output ["husband = ", show(husband), "\n"];
output ["obj_men = ", show(obj_men), "\n"];
output ["obj_women = ", show(obj_women)];