# https://atcoder.jp/contests/abc217/submissions/25633011

# paste SortedSet here

import sys
input = sys.stdin.readline

L, Q = map(int, input().split())
s = SortedSet([0, L])
for i in range(Q):
	c, x = map(int, input().split())
	if c == 1:
		s.add(x)
	else:
		print(s.gt(x) - s.lt(x))
