% Facts
father(terach, abraham).
father(terach, nachor). 
father(terach, haran).
father(nachor, bethuel).
father(bethuel, laban).
father(haran, lot).
father(haran, milcah).
father(haran, yiscah).
father(lot, moab).
father(lot, ban_ammi).
father(abraham, isaac).
father(abraham, ishmael).
father(abraham, zimran).
father(abraham, jokshan).
father(abraham, medan).
father(abraham, midian).
father(abraham, ishbak).
father(abraham, shuah).
father(jokshan, sheba).
father(jokshan, dedan).
father(dedan, asshurim).
father(dedan, letushim).
father(dedan, leummim).
father(midian, ephah).
father(midian, epher).
father(midian, hanoch).
father(midian, abidah).
father(midian, eldaah).
father(ishmael, nebajoth).
father(ishmael, kedar).
father(ishmael, adbeel).
father(ishmael, mibsam).
father(ishmael, mishma).
father(ishmael, dumah).
father(ishmael, massa).
father(ishmael, hadar).
father(ishmael, tema).
father(ishmael, jetur).
father(ishmael, naphish).
father(ishmael, kedemah).
father(isaac, jacob).
father(isaac, esau).
father(jacob, reuben).
father(jacob, simeon).
father(jacob, levi).
father(jacob, naphtali).
father(jacob, issachar).
father(jacob, asher).
father(jacob, dan).
father(jacob, zebulun).
father(jacob, gad).
father(jacob, benjamin).
father(jacob, judah).
father(jacob, joseph).
father(esau, eliphaz).
father(esau, reuel).
father(esau, jeush).
father(esau, jaalam).
father(esau, korah).
father(joseph, ephraim).
father(joseph, manasseh).
father(reuben, hanoch).
father(reuben, pallu).
father(reuben, hezron).
father(reuben, carmi).
father(simeon, jemuel).
father(simeon, jamin).
father(simeon, ohad).
father(simeon, jachin).
father(simeon, zohar).
father(simeon, shaul).
father(levi, gershon).
father(levi, kohath).
father(levi, merari).
father(judah, er).
father(judah, onan).
father(judah, shelah).
father(judah, perez).
father(judah, zerah).
father(perez, hezron).
father(perez, hamul).
father(issachar, tola).
father(issachar, puvah).
father(issachar, job).
father(issachar, shimron).
father(zebulun, sered).
father(zebulun, elon).
father(zebulun, jahleel).
father(gad, ziphion).
father(gad, haggi).
father(gad, shuni).
father(gad, ezbon).
father(gad, eri).
father(gad, arodi).
father(gad, areli).
father(asher, jimnah).
father(asher, ishuah).
father(asher, isui).
father(asher, beriah).
father(asher, serah).
father(beriah, heber).
father(beriah, malchiel).
father(benjamin, belah).
father(benjamin, becher).
father(benjamin, ashbel).
father(benjamin, gera).
father(benjamin, naaman).
father(benjamin, ehi).
father(benjamin, rosh).
father(benjamin, muppim).
father(benjamin, huppim).
father(benjamin, ard).
father(dan, hushim).
father(naphtali, jahzeel).
father(naphtali, guni).
father(naphtali, jezer).
father(naphtali, shillem).

mother(sarah, isaac).
mother(rebekah, jacob).
mother(rebekah, esau).

male(terach).
male(abraham).
male(nachor).
male(haran).
male(isaac).
male(lot).
male(asher).
male(benjamin).
male(beriah).
male(bethuel).
male(dan).
male(dedan).
male(esau).
male(gad).
male(ishmael).
male(issachar).
male(jacob).
male(jokshan).
male(joseph).
male(judah).
male(levi).
male(midian).
male(naphtali).
male(perez).
male(reuben).
male(simeon).
male(zebulun).

female(sarah).
female(milcah).
female(yiscah).
female(rebekah).

% Rules
son(X,Y) :- parent(Y, X), male(X).
daughter(X,Y) :- parent(Y, X), female(X).
grandparent(X,Y) :- parent(X, Z), parent(Z, Y).

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \== Y.
sister(X,Y) :- parent(Z,X), parent(Z,Y), X \== Y, female(X). 
brother(X,Y) :- parent(Z,X), parent(Z,Y), X \== Y, male(X). 
aunt(X,Y) :- parent(Z,Y), sibling(X,Z), female(X).
uncle(X,Y) :- parent(Z,Y), sibling(X,Z), male(X).
cousin(X,Y) :- grandparent(Z,X), grandparent(Z,Y), X \== Y.
cousin_b(X,Y) :- parent(Z,X), parent(W,Y), sibling(Z,W).

grandmother(X,Y) :- grandparent(X,Y), female(X).
grandfather(X,Y) :- grandparent(X,Y), male(X).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).


