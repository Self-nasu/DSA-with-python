% Check if a number is even
even(X) :-
    0 is X mod 2.

% Check if a number is odd
odd(X) :-
    1 is X mod 2.

% Find the greater of two numbers
greater(X, Y, X) :-
    X >= Y.
greater(X, Y, Y) :-
    Y > X.

% Calculate the factorial of a number
factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Result1),
    Result is N * Result1.

and(A,B) :- A,B.
or(A,_) :- A.
or(_,B) :- B.
not(A) :- \+A.

human(naman).
ranker(X) :- human(X).
toper(X) :- human(X). 