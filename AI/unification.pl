% Facts: Addition and multiplication predicates
add(X, 0, X).
add(X, Y, Z) :-
    Z is X + Y.

multiply(X, 0, 0).
multiply(X, Y, Z) :-
    Z is X * Y.

% Rule: Equality of expressions
equal(X, X).

% Rule: Expression unification
unify(A, B) :-
    equal(A, B).
unify(A + B, C + D) :-
    unify(A, C),
    unify(B, D).
unify(A * B, C * D) :-
    unify(A, C),
    unify(B, D).


?- unify(2, 2).
% true
?- unify(X + 3, 5 + Y).
% X = 5,
% Y = 3
?- unify(2 * X, Y * 3).
% X = 3,
% Y = 2
?- unify((2 * A) + (B + 1), (C * 2) + (D + 1)).
% A = C,
% B = D
