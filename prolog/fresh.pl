parent(f,i).
parent(X,Y) :- child(Y,X).

child(f,i).
child(Y,X) :- parent(X,Y).

% rules

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
% parent(X,Z), parent(Z,Y) :- grandparent(X,Y). % weird error