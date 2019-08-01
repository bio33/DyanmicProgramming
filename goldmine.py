


def getMaxGold(gold,m,n):
  val = [[0 for _ in range(n)] for _ in range(m) ]

  for col in range(n-1,-1,-1):
    for row in range(m):
      if col == n-1:
        right = 0
      else:
        right = val[row][col+1]
      if col == n-1 or row == m-1:
        right_down = 0
      else:
        right_down = val[row+1][col+1]
      if col == n-1 or row == 0:
        right_up = 0
      else:
        right_up = val[row-1][col+1]
    
      val[row][col] = gold[row][col] + max(right,right_down,right_up)
  res = 0
  for i in range(m):
    res = max(res,val[i][0])
  print(val)
  return res




gold = [[1, 3, 1, 5], 
    [2, 2, 4, 1], 
    [5, 0, 2, 3], 
    [0, 6, 1, 2]] 
  
m = 4
n = 4
  
print(getMaxGold(gold, m, n)) 
