% these are facts
loves(romeo, juliet). % romeo loves juliet
% rules
loves(juliet, romeo) :- loves(romeo, juliet). % juliet loves romeo if...

% facts
happy(nil).
undisciplined(nil).

buy(nil,coffee) :-
    happy(nil),
    undisciplined(nil).
