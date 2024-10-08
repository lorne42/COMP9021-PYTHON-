You will design and implement a program that will

extract and analyse the various characteristics of (simple) polygons, their contours being coded and stored in a file, and
– either display those characteristics: perimeter, area, convexity, number of rotations that keep the polygon invariant, and depth 
(the length of the longest chain of enclosing polygons)
– or output some Latex code, to be stored in a file, from which a pictorial representation of the polygons can be produced, coloured in a way 
which is proportional to their area.

Call encoding any 2-dimensional grid of size between between 2×2 and 50×50 (both dimensions can be different) all of whose elements are either 0 or 1.

Call neighbour of a member m of an encoding any of the at most eight members of the grid whose value is 1 and each of both indexes differs from
m’s corresponding index by at most 1. Given a particular encoding, 
we inductively define for all natural numbers d the set of polygons of depth d (for this encoding) as follows. Let a natural number d be given, 
and suppose that for all d0 < d, the set of polygons of depth d0 has been defined. Change in the encoding all 1’s that determine those polygons to 0. 
Then the set of polygons of depth d is defined as the set of polygons which can be 
obtained from that encoding by connecting 1’s with some of their neighbours in such a way that we obtain a maximal polygon 
(that is, a polygon which is not included in any other polygon obtained from that encoding by connecting 1’s with some of their neighbours).
