
def _partition_practice(l, n, li, hi):
	pi = li
	pivot = l[pi]
	print(f"pivot start l[{pi}]={pivot} {l}")
	while li<hi:
		while li < n and l[li] <= pivot:	# scan left->right until we find scanned elem > pivot
			li += 1
		print(f"scanned l->r until li l[{li}]={l[li] if li<n else -1}")
		while hi < n and l[hi] > pivot:	# scan right->left until we find scanned elem < pivot
			hi -= 1
		print(f"scanned l<-r until hi l[{hi}]={l[hi] if hi<n else -1}")
		if li<hi:
			print(f"swapping {li} -> {hi}")
			l[li],l[hi] = l[hi],l[li]

	l[pi],l[hi] = l[hi],l[pi]
	print(f"pivot end l[{hi}]={l[hi]}")
	return hi


def quicksortpractice(l, n=None, li=None, hi=None):
	if hi==None:
		n = len(l)
		hi = n - 1
		li = 0
		print(f"starting {l} li={li} hi={hi}")
	
	pi = li
	print(f"{pi} recursing l[{li}]={l[li] if li<n else -1} to l[{hi}]={l[hi] if hi<n else -1}")
	if li<hi:
		pi = _partition_practice(l,n,li,hi)
		quicksortpractice(l,n,li,pi)
		quicksortpractice(l,n,pi+1,hi)
	return l
	


def main():
  A = [10,16,8,12,15,6,3,9,5,float("inf")]
  # print(_partition1(A, 0, len(A) - 1))
  # print("quicksort1:", quicksort1(A, 0, len(A) - 1))
  l = [60,50,40,30]
  # l = [10,16,8,12,15]
  print("quicksort1:", quicksortpractice(l))

main()