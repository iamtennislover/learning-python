import pprint

def multi_stage_graph():
  """
  code of https://www.notion.so/ammul/4-1-1-MultiStage-graph-c8002146439d4c7689f83ec7ac8a068f
                                                                
                        Example                                
                                                                
                                                                
                                                                
                                2                              
                    - 2  ----------------------- 5 \            
                  -/   --\    3              --     -\          
                -/        ---\            --/   -     -\    6   
          2   -/              ---\     --/    -/        -\      
            -/                -   ---\/     -/            \     
          -/                    --/   ---\-/               -\   
        -/                6  --/         /---\               -\ 
      -/        1          -/          -/     --       4       -
    /      --------- 3   ------------/--------- 6  --------- 8 
  1-                          7   -/                        /  
      --                         -/           --            /   
        \-                      /         ---/             /    
          \--  3              -/       --/               /-     
            \-           6 -/     ---/                 /  5    
              \--        -/   ---/ 8                  /        
                  \-     /   -/                       /         
                    \- 4  ----------------------  7  -          
                                    9                           
  """
  s = 4
  n = 8
  cv = [0]*(n+1)
  print(cv)
  d = [0]*(n+1)
  c = [[0]*(n+1)]
  # build a 2x2 matrix to store edges cost
  for i in range(1,n+1):
    c.append([0]*(n+1))
  c[1][2] = 2; c[1][4] = 3;  c[1][3] = 1
  c[2][5] = 2; c[2][6] = 3; c[3][6] = 7;  c[3][5] = 6
  c[4][5] = 6;  c[4][6] = 8; c[4][7] = 9; c[5][8] = 6
  c[6][8] = 4;  c[7][8] = 5

  cv[n] = 0
  # loop from 7 -> 1
  for i in range(n-1,0,-1):
    # e.g. i = 2
    minc = 9999 # min cost for a vertix
    for k in range(i+1,n+1):
      print(i,k)
      if (c[i][k] + cv[k]) < minc and c[i][k] != 0:
        minc = c[i][k] + cv[k]
        d[i] = k
        print(i,k, minc)
    cv[i] = minc
    print(i, minc, d[i], "final")
  print("final cv", cv)
  print("final d", d)
  p = [None]*(s+1)
  p[1] = 1
  p[s] = n
  for i in range(2,s+1):
    print(i, d[i-1], p)
    previous_stage_vertix = p[i-1]
    next_target = d[previous_stage_vertix]
    p[i] = next_target
    print('after', p)
  print(p)



def matrix_chain_multiplication(d):
  """
  d: all dimensions in a list:
    [5,4,6,2,7] means we have 4 matrix multiplcation
    5x4, 4x6, 6x2, 2x7

  returns minimum multiplication cost and travesal
  """
  n = len(d)
  # cm to represent matrix of nxn size to store best costs
  # NOTE: 0th index is useless
  # NOTE: cannot use [[0]*n]*n to create a matrix as it uses same list inside - causes mutability issue
  cm = [[0]*n for i in range(n)]
  km = [[0]*n for i in range(n)]  # km represents k placement

  # first, find all diffs b/w i-j and loop over them incrementally
  # i=1, j=4; max diff=3; hence looping from 1 to 3
  for di in range(1, n-1):
    # 2nd, loop over i,j to be able to place cost in them
    # NOTE: using n-di to loop over only by diff as diagonal
    # i.e. for di=1; only look in 1,2; 2,3; 3,4
    # for di=2; only look in 1,3; 2,4;
    print("diff", di)
    for i in range(1,n-di):
      j = di+i
      print("with: i,j", i,j)
      # 3rd, finally find cost by min using another loop of k
      # since k goes from i-j
      minc = 99999 # initialize with large minimum cost
      for k in range(i,j,1):  # k is between i-j
        print(f"k: {k}, cm[i][k]: {cm[i][k]}, cm[k+1][j]: {cm[k+1][j]}, d[i-1]: {d[i-1]}, d[k]: {d[k]}, d[j]: {d[j]}")
        c = cm[i][k] + cm[k+1][j] + d[i-1]*d[k]*d[j]
        if (c < minc):
          minc = c      # find best min
          km[i][j] = k # store location of k
      print(f"storing cm: {minc}, i,j: {i},{j}. final cm: {cm}")
      cm[i][j] = minc
  
  print(f"cm:\n{pprint.pformat(cm)}")
  print(f"km:\n{pprint.pformat(km)}")
  # result will alway be in 1,n-1
  final_cost = cm[1][n-1]
  print("final_cost", final_cost)

  # travese km to find the ordering
  """
  logic:
  km[i][j] represents place to split
  so, for 1st one: i=1; j=n-1
  k[1][4] = 3

  we split at 3: we get 1,3 and 4,4
  find k[1][3] = 1;
  we split at 1: we get 1,1 and 2,3
  find k[2][3] = 2;
  we split at 2: we get 2,2 and 3,3

  we can see a2xa3 are 1st multiplied,
  then a2a3 x a1,
  then a2a3a1 x a4
  """
  # TODO:
  # km2 = km[1][n-1]
  # for x in range(1,n):
  #   pass
  # km[km2]

def lcs_recursion(a, b, c, i=0, j=0):
  """
  a = ["b", "d"]
  b = ["a", "b", "c", "d"]
  i to track a list;
  j to track b list;
  c to store the final sequence order
  """
  if i == j == 0:
    # initialize
    a.append(0) # set to 0 to stop the iteration
    b.append(0) # set to 0 to stop the iteration
    c.extend([0] * min(len(a)-1, len(b)-1)) # fill 0s with min size of a vs b

  print(i, j, a[i], b[j], c)
  if a[i] == 0 or b[j] == 0:
    return 0
  elif a[i] == b[j]:
    if len(a) < len(b):
      c[i] = a[i]
    else:
      c[j] = b[j]
    return 1 + lcs_recursion(a, b, c, i+1, j+1)
  else:
    return max(lcs_recursion(a, b, c, i+1, j),
      lcs_recursion(a, b, c, i, j+1))


I = 0
def lcs_recursion_memoization(a, b, c, d, i=0, j=0):
  """
  a = ["b", "d"]
  b = ["a", "b", "c", "d"]
  i to track a list;
  j to track b list;
  c to store the final sequence order
  d is a matrix ixj to store result of lcs_recursion
  """
  if i == j == 0:
    # initialize
    a.append(0) # set to 0 to stop the iteration
    b.append(0) # set to 0 to stop the iteration
    c.extend([0] * min(len(a)-1, len(b)-1)) # fill 0s with min size of a vs b
    d.extend([[None]*len(b) for _ in range(len(a))])

  print(i, j, a[i], b[j])
  if d[i][j] is not None:
    print("Using", i, j, d[i][j])
    return d[i][j]
  global I
  I += 1
  if a[i] == 0 or b[j] == 0:
    d[i][j] = 0
    return d[i][j]
  elif a[i] == b[j]:
    if len(a) < len(b):
      c[i] = a[i]
    else:
      c[j] = b[j]
    d[i+1][j+1] = 1 + lcs_recursion_memoization(a, b, c, d, i+1, j+1)
    return d[i+1][j+1]
  else:
    d[i+1][j] = lcs_recursion_memoization(a, b, c, d, i+1, j)
    d[i][j+1] = lcs_recursion_memoization(a, b, c, d, i, j+1)
    return max(d[i+1][j], d[i][j+1])

def lcs_dp(s1, s2):
  """
  dynamic programming LCS
  s1 = list("stone")
  s2 = list("longest")
  return: longest sequence - i.e. ['o', 'n', 'e']
  """
  rn = len(s1)
  cn = len(s2)
  lcs = [[0]*cn for _ in range(rn)] # initialize

  # fill the lcs with longest match
  # NOTE: using range(1, ...) to use 1-index to access s1 n s2 without having to do i-1 everywhere
  for i in range(1, rn):
    for j in range(1, cn):
      if s1[i] == s2[j]:
        lcs[i][j] = 1 + lcs[i-1][j-1]
      else:
        lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
  
  pprint.pprint(lcs)

  """trace to find the sequence:
  since longest match count is placed in lcs[rn-1][cn-1], traverse reverse
  - using while as its easy to read/understand, but for can also be applied
  - i = rn-1 is used to loop over lcs with uses 0th index
  """
  trace = []
  i = rn-1; j = cn-1
  while (i>=0 and j>=0):
    print(i,j, lcs[i][j])
    # since originally we traversed in max(i-1, j-1) above, we have to do the same
    # and find which path we took and reduce that index
    if (lcs[i][j] == lcs[i-1][j]):
      print("reducing i", i, j, lcs[i][j], s1[i])
      i = i - 1
    elif lcs[i][j] == lcs[i][j-1]:
      print("reducing j", i,j, lcs[i][j], s2[j])
      j = j - 1
    else:
      # this will be matched when we are at the intersection where
      # "lcs[i][j] = 1 + lcs[i-1][j-1]" matched - i.e. s1[i] == s2[j].
      # hence, store that result
      assert s1[i] == s2[j]
      trace.insert(0, s1[i])  # prepending since trace should contain the reverse order it was added
      print("reducing both", i,j,lcs[i][j], s1[i], s2[j])
      i = i - 1
      j = j - 1
  
  return trace


def main():
  # multi_stage_graph()

  # d = [5,4,6,2,7]
  # matrix_chain_multiplication(d)

  a = ["b", "d"]
  b = ["a", "b", "c", "d"]
  # a = ["x", "x"]
  # b = ["a", "b"]
  # a = "a b c d e f g h i j".split(" ")
  # b = "c d g i".split(" ")
  c = []
  # x = lcs_recursion(a,b,c)
  # print("result", x, c)

  # d = []
  # x = lcs_recursion_memoization(a, b, c, d)
  # print("result", x, c, I)
  # pprint.pprint(d)

  s1 = list("stone")
  # s1 = "a b c d e f g h i j".split(" ")
  s2 = list("longest")
  # s2 = "c d g i".split(" ")
  print("final", lcs_dp(s1, s2))


main()
