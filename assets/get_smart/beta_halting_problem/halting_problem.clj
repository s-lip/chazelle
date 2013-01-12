(defn uh [f] ((f (fn [x] (+ x 1))) 0))
(defn sr [n] (fn [f] (fn [x] (f ((n f) x)))))
(defn ps [m n] ((n sr) m))
(defn ep [m n] (n m))
(defn zo [f] (fn [x] x))
(defn oe [f] (fn [x] (f x)))
(defn pd [n] (fn [f] (fn [x] (((n (fn [g] (fn [h] (h (g f))))) (fn [y] x)) (fn [z] z)))))
(defn st [m n] ((m pd) n))
(defn ae [m n] (ps (st m n) (st n m)))
(defn il [m n a b] (((ae m n) (fn [x] b)) a))
(defn el [m n] (il m n oe zo))
(defn ft [a b c n] (el (ps (ep a n) (ep b n)) (ep c n)))
(defn fd [x y z] x)
(defn sd [x y z] y)
(defn td [x y z] z)
(defn mm [g]
	(let
		[
			a (g fd)
			b (g sd)
			c (g td)
		]
		(fn [h] (h a (sr b) (ps c (a b))))
	))
(defn sv [n f] (((n mm) (fn [g] (g f zo zo))) td))
(def to (ps oe oe))
(def te (ps to oe))
(def tn (ep te te))
(def lt (ep tn tn))
(def tm
	(sv lt (fn[a]
		(sv lt (fn[b]
			(sv lt (fn[c]
				(sv lt (fn[d] (ft a b c (ps d te)))))))))))
(println (uh tm))
