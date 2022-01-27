"""
https://www.notion.so/ammul/2-8-QuickSort-e0ad6016225147be8e6f54fca3dd1385
"""

def _partition1(A, l,h):
  pivot = A[l]
  i = l
  j = h

  while i<j:
    # iterate from l->h until i elem is smaller than pivot
    # so that we can place smaller ith elem left side of pivot
    while A[i] <= pivot:
      i = i + 1
    print(f"i: {i}")
    # iterate from h->l until j elem is greater than pivot
    # so that we can place larger jth elem right side of pivot
    while A[j] > pivot:
      j = j - 1
    print(f"j: {j}")
    if i < j:
      # swap i with j
      print(f"swapped i->j: {i}->{j} A[i]->A[j]: {A[i]}->{A[j]}")
      tmp = A[i]
      A[i] = A[j]
      A[j] = tmp
  
  # after j>=i, swap pivot with j
  tmp = pivot
  A[l] = A[j]
  A[j] = tmp
  print(f"swapped l->j: {l}->{j} pivot->A[j]: {pivot}->{A[j]}")
  print(f"final: {A}")
  return j


def quicksort1(A,l,h):
  if l<h:
    j = _partition1(A,l,h)
    quicksort1(A,l,j)
    quicksort1(A,j+1,h)
  return A


def main():
  A = [10,16,8,12,15,6,3,9,5,float("inf")]
  # print(_partition1(A, 0, len(A) - 1))
  print("quicksort1:", quicksort1(A, 0, len(A) - 1))

main()
