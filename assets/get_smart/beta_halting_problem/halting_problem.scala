import scala.collection.immutable._

val s = Stream.iterate(HashSet[AnyRef]()) { x => x + x }

def r(t : HashSet[AnyRef]) : Boolean = {
	val p = t.subsets(2).toSet.subsets.toList
	val c = t.subsets(5).map { _.subsets(2).toSet }.toList
	p.forall(x => {
		c.exists(y => {
			val i = x & y;
			i.size==0||i.size==10})})
}

println(s.indexWhere(r))
