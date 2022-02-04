"""
https://www.notion.so/ammul/2-7-1-3-Merge-Sort-90c875dc3fc548eeb42c0f600a273343
"""

def merge_two_sorted_lists(A, B, m, n):
  """Example in python with 0 indexed
  to sort two lists and return sorted result
  A = lista
  B = listb
  m = size of A
  n = size B
  """
  # print("running merge_two_sorted_lists.input", A, B, m, n)
  i=0;j=0;k=0
  C = [None] * (m+n)
  # print(m, n, len(C))
  while (i<m and j<n):
    print(i,j,k)
    if A[i] < B[j]:
      C[k] = A[i]
      k = k + 1
      i = i + 1
    else:
      C[k] = B[j]
      k = k + 1
      j = j + 1
  
  # NOTE: not intializing i to continue
  # to copy leftover elems
  for e in A[i:]:
    C[k] = e
    k = k + 1
  for e in B[j:]:
    C[k] = e
    k = k + 1
  
  # print("running merge_two_sorted_lists.output", C)
  return C


def _merge(l,m,h,A,B):
  print("Merging", l,m,h,A,B)
  if A[l] < A[m]:
    pass
  pass

def merge_sort_recursive1(A,l,h):
  """merge sort a given list recursively using merge_two_sorted_lists

  A: list to sort
  l: first index: 0
  h: last index: len(A)-1
  Returns: None, since it inplace modifies A as sorted list
  """
  # print(A,l,h)
  if l<h:
    m = int((l+h)/2) # break the list into half
		# perform merge sorting now on both the half lists
    print(f"l,m,h: {l},{m},{h} A[l],A[m]: [{A[l]},{A[m]}], A[m+1],A[h]: [{A[m+1]},{A[h]}]")
    merge_sort_recursive1(A,l,m)
    merge_sort_recursive1(A,m+1,h)
    # merge the two sorted half lists
    a = A[l:m+1]
    b = A[m+1:h+1]
    print(f"a: {a}; b: {b}")
    sizea = len(a)
    sizeb = len(b)
    c = merge_two_sorted_lists(a, b, sizea, sizeb)
    print(f"c: {c}")
    A[l:h+1] = c


def main():
  print("running merge sort main")
  # A = [2,8,15,18]
  # B = [5,9,12,17,19,25,30]
  # print("merge_two_sorted_lists",
  #   merge_two_sorted_lists(A, B, len(A), len(B)))
  
  A = [9,3,7,5,6,4,8,2]
  print("merge_sort_recursive before", A)
  merge_sort_recursive1(A, 0, len(A)-1)
  print("merge_sort_recursive after", A)

main()