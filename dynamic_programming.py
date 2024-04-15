MAXV = 100

class graph:
  def __init__(self, num):
    self.matrix = [[0 for _ in range(MAXV)] for _ in range(MAXV)]
    self.n = num

path = [0] * MAXV
mincost = [0] * MAXV

def creategraph(num):
  graphy = graph(num)
  
  for i in range(1, num+1):
    for j in range(1, num+1):
      graphy.matrix[i][j] = 0
  
  n = int(input("请输入边数："))
  
  for _ in range(n):
    point1, point2, value = map(int, input().split())
    graphy.matrix[point1][point2] = value
  
  print("\n建立的邻接矩阵为:")
  for i in range(1, num+1):
    for j in range(1, num+1):
      print("{:2d}".format(graphy.matrix[i][j]), end=" ")
    print()
  
  print()
  graphy.n = num
  return graphy

def main():
  num = 0
  thiscost = 0
  pre = 0
  
  num = int(input("顶点数量为："))
  
  graphy = creategraph(num)
  
  mincost[1] = 0
  for i in range(2, graphy.n+1):
    mincost[i] = 99999
  
  for i in range(2, num+1):
    for j in range(1, i):
      if graphy.matrix[j][i] != 0:
        thiscost = mincost[j] + graphy.matrix[j][i]
        if thiscost < mincost[i]:
          mincost[i] = thiscost
          path[i] = j
  
  for i in range(1, num+1):
    print("到顶点", i, "的最小开销为：", mincost[i], "，路径：", i, end="")
    pre = i
    while path[pre] != 0:
      print("<-", path[pre], end="")
      pre = path[pre]
    print()

if __name__ == "__main__":
  main()
