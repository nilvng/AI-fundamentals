%facts
% me(i). % i is me
% daughter(d,i,w). % d is stepdaughter of i and w

% wife(w,i). % w is my wife
% wife(d,f). % stepdaughter d is my father f's wife

% son(s1,i,w). % s1 is my son and w
% son(s2,f,d). % s2 is son of my father f and stepdaughter
% son(f,i,w). % father is my son-in-law
% son(i,f,d). % Im stepson of my father and my step daughter

% parent(d,i).
parent(i,f).

% rules
% parent(X,Y) :- son(Y,X,Z), wife(Z).
% son(Y,X,Z), wife(Z) :- parent(X,Y).
% parent(X,Y) :- daughter(Y,X,Z), wife(Z).
parent(X,Y) :- child(Y,X).

child(i,f).
child(d,i).
child(s1,i).
child(s2,f).

child(Y,X) :- parent(X,Y).


grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
% parent(X,Z), parent(Z,Y) :- grandparent(X,Y).