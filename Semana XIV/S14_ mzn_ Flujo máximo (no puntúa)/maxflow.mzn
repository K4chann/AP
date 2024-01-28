int: num_nodes;                          % número de nodos del grafo
int: num_edges;                          % número de aristas del grafo

1..num_nodes:source;                     % nodo fuente
1..num_nodes:sink;                       % nodo sumidero

array[1..num_edges, 1..2] of int: edges; % aristas del grafo (origen->destino)
array[1..num_edges] of int: capacity;    % capacidad de cada arista

var int: max_flow;                       % variable de decision para el valor
                                         % del flujo máximo
array[1..num_edges] of var int: flow;    % variable de decisión para el flujo
                                         % final de cada arista

output
[ 
  "max flow =" ++ show(max_flow)
];

% Escribir el código a partir de aquí-----------------------------------------


constraint forall(edge in 1..num_edges) (flow[edge] >= 0);

constraint forall(i in 1..num_nodes where i != sink /\ i != source) 
    (sum(edge in 1..num_edges where edges[edge, 1] == i) (flow[edge]) == sum(edge in 1..num_edges where edges[edge, 2] == i) (flow[edge]));
constraint forall(edge in 1..num_edges) (flow[edge] <= capacity[edge]);

constraint max_flow = sum(edge in 1..num_edges where edges[edge, 2] == sink) (flow[edge]);

solve maximize max_flow;