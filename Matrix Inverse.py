A = [] #Initialize Matrix A
B = [] #Initialize Matrix B (Inverse Of A)
multResult = [] #Initialize Result.
ord  = int(input("Enter Order Of Matrix: "))  #get order of square matrix

def make(matrix):
  for i in range(ord):    
    l = []
    for j in range(ord):
      inp = int(input("Enter Value: "))
      l.append(inp)
    matrix.append(l)
  


def matrixMultiply():
  for i in range(ord):
    l = []
    for j in range(ord):
      result = 0
      for k in range(ord):
        result += A[i][k] * B[k][j]
        if k == ord - 1:
          l.append(result)
    if j == ord - 1:
        multResult.append(l)

def check():
  I = []
  for i in range(ord):
    l = []
    for j in range(ord):
      if i == j:
        l.append(1)
      else:
        l.append(0) 
    I.append(l)
  if multResult == I:
    print("It is the inverse.")
  else:
    print("Not Inverse")

make(A),make(B)
matrixMultiply()
check()