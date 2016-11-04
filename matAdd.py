
m = int( input ("No of rows in matrix: "))
n = int( input ("No of columns in matrix: "))
print ("You chose the matrix of: ", m, "x", n)

print("")

X = [[]]
i = 0
j = 0
while j < n:
    X[0].append(int( input ("Provide the value in: ")))
    print (X)
    j = j + 1
    
j = 0
i = i + 1
while j < m:
    X[1].append(int( input ("Provide the value in: ")))
    print (X)
    j = j + 1
    


#for k in X:
 #   print(k)
                         
         




'''

X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

Y = [[1,2,3],
    [4,5,6],
    [7,8,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]


# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for k in result:
   print(k)


'''
