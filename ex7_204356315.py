#########################################
# Question 1 - do not delete this comment
#########################################

# Write the rest of the code for question 1 below here.
def catalan_rec(n):
        if n==0:
                return 1
        summ=0
        for i in range(0,n): #until (n-1) inculding
              summ+=catalan_rec(i)*catalan_rec(n-1-i)
        return summ
                

def catalan_mem(n,memo=None):
        if n==0:
                return 1
        if memo==None: memo={}
        if n not in memo:
                summ=0
                for i in range(0,n):
                      summ+=catalan_mem(i,memo)*catalan_mem(n-1-i,memo)
                memo[n]=summ
        return memo[n]
	
# If you want to do the bonus, define the functions and implement below

def catalan_rec_with_count(n,counter=1):
        if n==0:
                return (1,1)
        summ=0
        for i in range(0,n):
                c1=catalan_rec_with_count(i,1)
                c2=catalan_rec_with_count(n-1-i,1)
                summ+=c1[0]*c2[0]
                counter+=c1[1]+c2[1]
        return(summ,counter-1)

def catalan_mem_with_count(n,memo=None,counter=1):
        if n==0:
                return (1,1)
        if memo==None:
                memo={0:(1,1)}
        if n not in memo:
                summ=0
                for i in range(0,n):
                        c1=catalan_mem_with_count(i,memo,1)
                        c2=catalan_mem_with_count(n-1-i,memo,1)
                        summ+=c1[0]*c2[0]
                        counter+=c1[1]+c2[1] 
                memo[n]=(summ,counter-1)
                return memo[n]
        else: return (memo[n][0],1)
                

#########################################
# Question 2 - do not delete this comment
#########################################


# Write the rest of the code for question 2 below here.

def atm_rec(amount, bills, n):
        if n==0:
                return False
        if amount<min(bills):
                return False
        if n==1:
                if amount in bills:
                        return True
                else:   return False
        for val in bills:
                if(atm_rec(amount-val,bills,n-1)==True): #means we can get the amount from val
                        return True
        return False #after we scanned all the values

def atm_mem(amount, bills, n,memo = None):
        if memo==None:
                memo={}
        if (amount,n) not in memo:
                if n==0:
                        return False
                if amount<min(bills):
                        return False
                if n==1:
                        if amount in bills:
                                return True 
                        else:   
                                return False
                for val in bills:
                        if(atm_rec(amount-val,bills,n-1)==True): #means we can get the amount from val
                                memo[amount,n]=True
                if (amount,n) not in memo:
                        memo[amount,n]=False #after we scanned all the values
        return  memo[amount,n]
        
	
#########################################
# Question 3 - do not delete this comment
#########################################


# Write the rest of the code for question 3 below here.

def max_trail(pyramid,row=0,col=0):
        if pyramid==[]:
                return None
        sum=pyramid[row][col]
        if row<len(pyramid)-1:
                sum+=max(max_trail(pyramid,row+1,col),max_trail(pyramid,row+1,col+1))
        return sum                           

        
def max_trail_mem(pyramid,row=0,col=0,memo=None):
        if pyramid==[]:
                return None
        if memo==None:
                memo={}
        if (row,col) not in memo:
                sum=pyramid[row][col]
                if row<len(pyramid)-1:
                        sum+=max(max_trail(pyramid,row+1,col),max_trail(pyramid,row+1,col+1))
                        memo[(row,col)]=sum        
        return memo[(row,col)]
