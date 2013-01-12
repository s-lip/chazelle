-module(halting_problem).
-import(lists,[seq/2]).

g(A,0) -> A;
g(A,B) -> g(B, A rem B).

p(_,0) -> 1;
p(A,B) -> A * p(A,B-1).

f(A,R,N,F) ->
	P = p(A, R div 2) rem N,
	Q = p(A, R) rem N,
	if
		R rem 2 == 1 -> ok;
		Q /=1 -> ok;
		P == N-1 -> ok;
		P == 1 -> ok;
		true -> F ! min(g(P-1,N),g(P+1,N))
	end,
	ok.

d(S,N) ->
	[ spawn(fun() -> f(A,R,N,S) end) || A <- seq(2,N-2), R <- seq(1,N-1) ].

main(_) ->
	S = self(),
	spawn(fun() -> d(S,1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413) end),
	receive
		X -> io:format("~p~n",[X])
	end.
