''' Exercise #2. Python for Engineers.'''
#Or Bahari - 204356315
#########################################
# Question 1 - do not delete this comment
#########################################

A = [1, 3, 5, 0, 3, 1, 5]
# Write the rest of the code for question 1 below here.
N=len(A)
avg=0
if N==0:
    print "NA"
else:
    for i in range(0,N):
        avg+=A[i]
    avg=avg/(N+0.0)
    print avg
    
#########################################
# Question 2 - do not delete this comment
#########################################
A = [1, 2, 5, 4]
B = [3, 1, 4, 0]


# Write the rest of the code for question 2 below here.
N=len(A)
max_A=0
for i in range(0,N):
    if max_A<A[i]:
        max_A=A[i]
min_B=0
for i in range(0,N):
    if min_B>B[i]:
        min_B=B[i]
if N==0:
    print "NA"
else:
    mult_sum=0
    for i in range(0,N):
        mult_sum+=A[i]*B[(N-1)-i]
print max_A
print min_B
print mult_sum

#########################################
# Question 3 - do not delete this comment
#########################################

val = "how much wood could a woodchuck chuck" 
val2 = "pam pam" 

# Write the rest of the code for question 3 below here.
list_val=val.split()
N=len(list_val)
for i in range(2,N,3):
    list_val[i]=list_val[i-1]
new_list=" ".join(list_val)
print new_list

#########################################
# Question 4 - do not delete this comment
#########################################
A = [1, 5, 4]
B = [7, 5, 10]

# Write the rest of the code for question 4 below here.
A.sort()
B.reverse()
A.extend(B)
print A

#########################################
# Question 5 - do not delete this comment
#########################################

A = [2, 6, 10, 14] 
B = [5, 4, 3, 2] 
C = [5, 4, 3, 0]

# Write the rest of the code for question 5 below here.
N=len(A)
d=A[1]-A[0]
i=1
con=True
while i<=N-2:
    if d==A[i+1]-A[i]:
        i+=1
        continue
    con=False
    print con
    print i
    break    
if con:
    print con
    print d
    
#########################################
# Question 6 - do not delete this comment
#########################################

items = [ ["rice", 1.0, 10.0], ["salt", 4.0, 15.0], ["milk", 1.0, 20.0], ["eggs", 1.0, 20.0]  ]
items2 = [ ["rice", 1.0, 10.0], ["salt", -4.0, 15.0], ["milk", 1.0, 20.0], ["eggs", 1.0, -20.0]  ]

# Write the rest of the code for question 6 below here.
N=len(items)
income=0
valid=True
for i in range(0,N):
    if len(items[i])!=3:
        valid=False
        print items[i][0]
        break
    if not (items[i][0].isalpha() and items[i][1]>0 and items[i][2]>0):
        valid=False
        print items[i][0]
        break
    income+=items[i][1]*items[i][2]
if valid:
    print income
    
#########################################
# Question 7 - do not delete this comment
#########################################

Matrix = [ [4, 5, 3, 8], [0, 2, 4, 9], [10, 9, 2, 2], [1, -3, 4, 4] ]
Matrix2 = [ [1, 0], [2, -1] ]

# Write the rest of the code for question 7 below here.
max_len=1
cur_len=1
l=len(Matrix)
r=len(Matrix[0])
for i in range(0,l):
    for j in range(0,r-1):
        if Matrix[i][j]<=Matrix[i][j+1]:
            cur_len+=1
        else: break
        if cur_len>max_len:
            max_len=cur_len
    cur_len=1
print max_len
