"""
Covers topics from

https://www.notion.so/ammul/Queues-c6eafab37eb7480da05607c89c4e28f2
https://www.notion.so/ammul/2-6-3-Heap-Heap-Sort-2f398aa1d4d34ecf923ca2deaddc7599#96b4e496656543beb18567aef7f24b4d

around priority queue using binary heap
"""
import math

def example1_binary_tree():
	"""
	"Example1-BT"

	"""
	g = "a,b,c,d,e,f,g".split(",")
	n = len(g)
	print(g, n)
	print([str(i) for i in range(n)])
	for i in range(n):
		e = g[i]
		parenti = math.floor((i-1)/2)
		parent = g[parenti] if parenti >= 0 else None
		leftchildi = 2*i + 1
		leftchild = g[leftchildi] if leftchildi < n else None
		rightchildi = 2*i + 2
		rightchild = g[rightchildi] if rightchildi < n else None
		print(f"g[{i}]={e}; parent: {parent}; leftchild: {leftchild}; rightchild: {rightchild}")



def main():
	example1_binary_tree()

main()
