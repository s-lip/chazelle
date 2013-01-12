#load "nums.cma";;
open Big_int;;
open List;;

let p l = match l with [] -> (0,[]) | x::xs -> (x,xs);;

let g (l,m,r,s) = let (mn,ln) = p l in (ln,mn,m::r,s);;

let d (l,m,r,s) = let (mn,rn) = p r in (m::l,mn,rn,s);;

let rec f (l,m,r,s) = match (m,s) with
	(0,0) -> f (d (l,1,r,1)) |
	(0,1) -> f (d (l,1,r,2)) |
	(0,2) -> f (g (l,1,r,3)) |
	(0,3) -> f (d (l,1,r,4)) |
	(0,4) -> f (g (l,1,r,0)) |
	(1,0) -> f (g (l,1,r,4)) |
	(1,1) -> f (d (l,1,r,5)) |
	(1,2) -> f (d (l,0,r,1)) |
	(1,3) -> f (g (l,0,r,2)) |
	(1,4) -> f (d (l,0,r,3)) |
	(1,5) -> f (d (l,1,r,2)) |
	(_,_) -> (l,1,r);;

let u = fold_right add_int_big_int;;

let a = let (l,m,r) = f ([],0,[],0) in u r (u l (big_int_of_int m));;

print_endline (string_of_big_int a);;
