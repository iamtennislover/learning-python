"""https://www.notion.so/ammul/Recursion-5f4c4e786d5a49218e3ca26a2f806b16
"""

def fib_iteration(n):
	if n == 0 or n == 1:
		return n
	f1 = 0	# n-1
	f2 = 1	# n-2
	for i in range(2, n+1):	# we want to go from 2 to n
		f = f1 + f2	# calculate sum
		f1 = f2	# in next iteration f1 becomes previous f2
		f2 = f	# in next iteration f2 becomes sum
	return f


def fib_recursion(n):
	print(f"calling fib_recursion: {n}")
	if n<=1:
		return n
	return fib_recursion(n-1) + fib_recursion(n-2)

def fib_recursion_with_memoization(n, d=None):
	print(f"calling fib_recursion_with_memoization: {n}")
	if n<=1:
		return n

	if d == None:
		# d stores map: i:result
		d = {}	# initialize memory first time

	if n in d:
		return d[n]

	d[n] = fib_recursion_with_memoization(n-1, d) + fib_recursion_with_memoization(n-2, d)
	# NOTE: commented off option is possible and results in same time, but its too much code
	# if n-1 in d:
	# 	f1 = d[n-1]
	# else:
	# 	f1 = fib_recursion_with_memoization(n-1, d)
	# 	d[n-1] = f1
	# if n-2 in d:
	# 	f2 = d[n-2]
	# else:
	# 	f2 = fib_recursion_with_memoization(n-2, d)
	# 	d[n-2] = f2
	# return f1 + f2
	return d[n]


def pow_recursion(x,n):	# takes O(n)
	if n == 0: return 1
	return x * pow_recursion(x, n-1)


def pow_recursion_logn(x,n):	# takes O(logn)
	if n == 0: return 1
	if n % 2 == 0:
		# NOTE: This allows 
		y = pow_recursion_logn(x, n/2)
		return y * y	# NOTE: using y to avoid calling twice

	return x * pow_recursion_logn(x, n-1)


def pow_iteration(x,n):
	r = 1
	for i in range(n):
		r = r * x
	return r


def fun_tail(n):
	print(f"starting fun_tail: {n}")
	if n>0:
		print(n)
		fun_tail(n-1) # last stmt
	print(f"ending fun_tail: {n}")


def fun_head(n):
	print(f"starting fun_head: {n}")
	if n>0:
		fun_head(n-1) # 1st stmt
		print(n)
	print(f"ending fun_head: {n}")



def fun_tree(n):
	print(f"starting fun_tree: {n}")
	if n>0:
		print(n)
		fun_tree(n-1) # call1
		fun_tree(n-1) # call2
	print(f"ending fun_tree: {n}")


def gcd(m,n):
	"""Greatest Common Denominator
	https://www.notion.so/ammul/Basics-Maths-for-Interview-Preparation-ba5cdcbeb24c41f5a3990aff59edaae2
	"""
	if m < n:
		return gcd(n, m)
	# m is always greater than n
	r = m % n
	if r == 0:	# base condition
		return n
	return gcd(n,r)
	

def main():
	# assert fib_recursion(6) == 8
	# assert fib_recursion(7) == 13
	# assert fib_iteration(6) == 8
	# assert fib_iteration(7) == 13
	# d = {}
	# print(fib_recursion_with_memoization(7, d))
	# print(d)
	# assert (pow_recursion(2,3)) == 8
	# assert pow_iteration(2,3) == 8
	# assert pow_recursion_logn(2,3) == 8
	# fun_tail(3)
	# fun_head(2)
	# fun_tree(2)
	print(gcd(30,12))

main()
