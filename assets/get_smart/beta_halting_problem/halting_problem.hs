import Data.List
import Data.Maybe

s = map (\(_,_,_,_,x) -> x) $ iterate r (0,1,1,1,Nothing)
	where r (a,b,c,d,e) =
		let
			g = a * d + 4 * b * c
			h = b * d
			i = g `div` h
		in if Just i == e
			then (10000000000 * (g `mod` h),h,(-10000000000)*c,d+2,Nothing)
			else (g,h,-c,d+2,Just i)
			
d = [ fromJust $ genericIndex s i | i <- [0..], isNothing $ genericIndex s (i+1)]

main = print (d!!2)
