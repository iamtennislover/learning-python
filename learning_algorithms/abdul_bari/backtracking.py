from pprint import pprint


def nqueen():
    q = [10, 20, 30, 40]  # queens
    chess_board_size = 4
    cn = chess_board_size + 1  # make 1 index, use 0,0 as 0s
    # make 1 indexed
    q = [None] + q
    # represent a chess board
    c = [[None] * cn for _ in range(cn)]

    """
    for loop doesn't work since we have to work on this until we find a result
      # using 1 index hence starting with range(1)
      for i in range(1, cn):
          for j in range(1, cn):
    """
    i = 1; j = 1
    while True:
      # if i == cn:
      #     i = 1 # reset
      # if j == cn:
      #   j = 1
      pprint(c)
      print(i, j, c[i][j], q[i])
      if i == 1:  # if 1st row, skip checking diagonal
        no_q_in_diag = True
      elif j == 1:  # if 1st col, skip left diagonal
        top_right_diag = c[i - 1][j + 1]
        no_q_in_diag = top_right_diag == None
      elif j == chess_board_size:  # if last col, skip right diagonal
        top_left_diag = c[i - 1][j - 1]
        no_q_in_diag = top_left_diag == None
      else:
        top_left_diag = c[i - 1][j - 1]
        top_right_diag = c[i - 1][j + 1]
        no_q_in_diag = top_left_diag == None and top_right_diag == None
      
      no_q_in_same_col = all([c[r][j] == None for r in range(1, cn) if r!=i])
      print(i,j, no_q_in_same_col, no_q_in_diag)
      if (no_q_in_same_col and no_q_in_diag):
          c[i][j] = q[i]
          i = i + 1
          j = 1
          continue
      
      all_queens_placed = [q[i] in c[i] for i in range(1, len(q))]
      print(all_queens_placed)
      if all(all_queens_placed):
        break
      
      i = i + 1
      j = j + 1


    pprint(c)


def hamilton(k=2, x=None, G=None, n=None, R=[]):
  """
  k: index of x (1-index)
  x: holds hamilton cycle, with x[k] holding vertices
  G: a nxn matrix holding 1/0, 1=connected, 0=non-connected
  and matrix indexes represent vertices
  n: no. of nodes
  R: matrix to hold list of cycles found

  Usage:
    R = []
    hamilton(R=R)
    pprint(R)
  """
  print(f"starting hamilton, k={k}; x={x}")
  if x==None and G==None and n==None:
    # initialize values (can be done outside, but making it easy)
    G = [
    #c=1 2 3 4 5     r
      [0,1,1,0,1], # 1
      [1,0,1,1,1], # 2
      [1,1,0,1,0], # 3
      [0,1,1,0,1], # 4
      [1,1,0,1,0], # 5
    ]
    # make G 1-index by adding 0s
    G.insert(0, [None]*len(G[0]))
    for r in G:
      r.insert(0, None)
    n = len(G[0]) - 1
    x = [0]*(n+1)
    x[0] = None
    x[1] = 1  # we need to start from 1st vertix
    # validate
    assert G[1][2] == 1
    assert n == 5
  
  # backtracking requires do while
  while True:
    nextvertex_hamilton(k, x, G, n)
    # print(f"after nextvertex_hamilton, k={k}; x={x}")
    if x[k] == 0:
      return  # very last thing that runs
    if k == n:
      print(f"hamilton result: {x} {k}")
      R.append(x[:])
    else:
      hamilton(k+1, x, G, n, R)
      print(f"ending hamilton, k+1={k+1}; x={x}")

  # NOTE: below line never gets called
  print(f"ending hamilton, k={k}; x={x}")

def nextvertex_hamilton(k, x, G, n):
  print(f"    starting nextvertex, k={k}; x={x}")
  while True:
    # try all values from 0 to 5 in x[k] until below 3 conditions are met
    x[k] = (x[k] + 1) % (n + 1)
    # print(f"mod: x[{k}]={x[k]}")

    # if all 3 conditions are met, use above x[k] and go to next k
    # condition1: if edge exists to previous node
    condition1 = G[x[k-1]][x[k]] == 1
    # condition2: if duplicate not found
    condition2 = x[k] not in x[1:k]
    # condition3: if last vertix has edge to 1st vertix
    condition3 = (k<n) or (k==n and G[x[n]][x[1]] == 1)
    conditions = [condition1, condition2, condition3]
    if all(conditions):
      # print(f"all conditions met for k={k}. Going to next k")
      return
    else:
      pass
      # print(f"some conditions didn't meet for k={k}, trying next node in same k")

    # this condition will be met at the end after trying all possibilities of x[k]
    # to finally go to next k
    if x[k]==0:
      # print(f"return at k={k}, since x[k]==0")
      return

def main():
    # nqueen()
    R = []
    hamilton(R=R)
    pprint(R)
    # x = [0,1,2,5,4]
    # k = 3
    # print(x[k], x[1:k])


main()
