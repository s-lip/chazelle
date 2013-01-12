#include <stdint.h>
#include <iostream>

typedef int64_t Z;

#define START(w,h) P<0,(1L<<((w)*(h)))-1L,w,h>
#define END(w,h) V<START(w,h)>::value

template<Z _pos, Z _mask, Z _w, Z _h>
struct P {
	static const Z pos = _pos;
	static const Z mask = _mask;
	static const Z w = _w;
	static const Z h = _h;
};

template<typename p,Z x, Z y>
struct N {
	typedef P<~(p::pos|(1L<<(p::h*x+y))),p::mask&~(1L<<(p::h*x+y)),p::w,p::h> value;
};

template<typename p, Z c, Z x, Z y>
struct D {
	static const Z value = ((p::pos&~p::mask)>>(p::h*x+y))&1L; 
};

template<typename p, Z x, Z y>
struct D<p,0,x,y> {
	static const Z value = 0;
};

template<typename p, Z x, Z y>
struct C {
	static const Z value = D<p,(x>=0&&x<p::w&&y>=0&&y<p::h),x,y>::value;
};

template<typename p, Z c, Z x, Z y>
struct L {
	static const Z value = ((~p::mask)>>(p::h*x+y))&1;
};

template<typename p, Z x, Z y>
struct L<p,0,x,y> {
	static const Z value = 0;
};

template<typename p, Z x, Z y>
struct M {
	static const Z value = L<p,(x>=0&&x<p::w&&y>=0&&y<p::h),x,y>::value;
};

template<typename p,Z c,Z x, Z y>
struct S {
	static const Z value;
};

template<typename p,Z x,Z y>
struct S<p,0,x,y> {
	static const Z value = y;
};

template<typename p, Z x, Z y>
struct R {
	static const Z value = S<p,M<p,x,y>::value,x,y>::value;
};

template<typename p,Z c,Z x, Z y>
const Z S<p,c,x,y>::value = R<p,x,y+1>::value;

template<typename p, Z x, Z y>
struct W {
	
	static const Z value = (y>=p::h)?-1:
		(C<p,x+1,y>::value&C<p,x+2,y>::value&C<p,x+3,y>::value)|
		(C<p,x-1,y>::value&C<p,x+1,y>::value&C<p,x+2,y>::value)|
		(C<p,x-2,y>::value&C<p,x-1,y>::value&C<p,x+1,y>::value)|
		(C<p,x-3,y>::value&C<p,x-2,y>::value&C<p,x-1,y>::value)|
		(C<p,x,y+1>::value&C<p,x,y+2>::value&C<p,x,y+3>::value)|
		(C<p,x,y-1>::value&C<p,x,y+1>::value&C<p,x,y+2>::value)|
		(C<p,x,y-2>::value&C<p,x,y-1>::value&C<p,x,y+1>::value)|
		(C<p,x,y-3>::value&C<p,x,y-2>::value&C<p,x,y-1>::value)|
		(C<p,x+1,y+1>::value&C<p,x+2,y+2>::value&C<p,x+3,y+3>::value)|
		(C<p,x-1,y-1>::value&C<p,x+1,y+1>::value&C<p,x+2,y+2>::value)|
		(C<p,x-2,y-2>::value&C<p,x-1,y-1>::value&C<p,x+1,y+1>::value)|
		(C<p,x-3,y-3>::value&C<p,x-2,y-2>::value&C<p,x-1,y-1>::value)|
		(C<p,x+1,y-1>::value&C<p,x+2,y-2>::value&C<p,x+3,y-3>::value)|
		(C<p,x-1,y+1>::value&C<p,x+1,y-1>::value&C<p,x+2,y-2>::value)|
		(C<p,x-2,y+2>::value&C<p,x-1,y+1>::value&C<p,x+1,y-1>::value)|
		(C<p,x-3,y+3>::value&C<p,x-2,y+2>::value&C<p,x-1,y+1>::value);
};

template<typename p, Z x>
struct A {
	static const Z value;
};

template<typename p>
struct A<p,0> {
	static const Z value;
};

template<typename p, Z c>
struct U {
	static const Z value = A<p,p::w-1>::value;
};

template<typename p>
struct U<p,0> {
	static const Z value = 0;
};

template<typename p>
struct V {
	static const Z value = U<p,p::mask>::value;
};

template<typename p, Z c, Z x, Z y>
struct F {
	static const Z value = c;
};

template<typename p, Z x, Z y>
struct F<p,0,x,y> {
	static const Z value = -V<typename N<p,x,y>::value>::value;
};

template<typename p, Z x, Z y>
struct E {
	static const Z value = F<p,W<p,x,y>::value,x,y>::value;
};

template<Z x, Z y>
struct X {
	static const Z value = x>y?x:y;
};

template<typename p, Z x>
const Z A<p,x>::value = X<E<p,x,R<p,x,0>::value>::value,A<p,x-1>::value>::value;

template<typename p>
const Z A<p,0>::value = E<p,0,R<p,0,0>::value>::value;

template<Z w, Z s>
class H {
	static const Z value = END(w,s-w)+3*H<w,s+1>::value;
};

template<Z w>
class H<w,15> {
	static const Z value = END(w,15-w)+3*H<w+1,w+5>::value;
};

template<>
class H<11,15> {
	static const Z value = END(11,4);
};

int main() {
	std::cout << H<4,8>::value << std::endl;
	return 0;
}
