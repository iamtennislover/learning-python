"""
https://www.notion.so/ammul/Abdul-Bari-Algorithm-883de30416e14358bfdca940a2c4980f#b5353bf52e644de18a8e51b886195a3b
"""

def binary_search(A, n, x) -> int:
	"""
	x = element to be found
	A = sorted list
	n = size of elem
	return the index where its found
	"""
	l = 1; h = n
	while (l<h):
		m = int((l+h)/2)
		print(f"m: {m}, A[m]: {A[m]}, {(l+h)/2}, l:{l}, h:{h}")
		if A[m] == x:
			return m
		if A[m] > x: # find left hand side, since x is smaller
			h = m - 1
		else:  # find right hand size, since x is larger
			l = m + 1
	return -1


def binary_search_0_indexed(A, n, x) -> int:
	"""Improved version that works for 0 indexed"""
	l = 0; h = n-1  # main change is here
	while (l<=h): # main change is here
		m = int((l+h)/2);
		print(f"m: {m}, A[m]: {A[m]}, {(l+h)/2}, l:{l}, h:{h}")
		if A[m] == x:
			return m
		if A[m] > x: # find left hand side, since x is smaller
			h = m - 1
		else:  # find right hand size, since x is larger
			l = m + 1
	print("final", l, h)
	return -1


def binary_search_recursive(A, l, h, x):
	if l==h: # single elem
		if (A[l] == x):
			return l
		else:
			return -1
	else:
		m = int((l+h)/2)
		if x == A[m]:
			return m
		else:
			if (x < A[m]):
				return binary_search_recursive(A, l, m-1, x)
			else:
				return binary_search_recursive(A, m+1, h, x)


def main():
  A = [3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
  x = 42
  n = len(A)
  print(f"lenght: {n}")
  print([str(i).zfill(2) for i in A])
  print([str(i).zfill(2) for i in range(n)])
  # print([str(i).zfill(2) for i in range(1, n+1)])
  # print(list(zip(A, list(range(1, n+1)))))
  # r = binary_search(A, n, x)
  # print(f"r is: {r}")

  l = 0; h = n;
  r = binary_search_recursive(A, l, h, x)
  print(f"r using recursive is: {r}")
  assert binary_search_recursive(A, l, h, A[0]) == 0

  # print(binary_search(A, n, 3))
  # print(binary_search(A, n, x))
  # assert binary_search_0_indexed(A, n, A[0]) == 0
  # assert binary_search_0_indexed(A, n, x) == 10

main()