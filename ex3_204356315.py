#########################################
# Question 1 - do not delete this comment
#########################################

TOMATO = "tomato"

# Write the rest of the code for question 1 below here.
	
def find_tomato(items):
        N=len(items)
        for i in range(0,N):
                if items[i].lower()== "tomato":
                        return i
        return -1

#########################################
# Question 2 - do not delete this comment
#########################################

VOWELS = "AEIOU"

# Write the rest of the code for question 2 below here.

def even_vowels(sentence):
        num_vowels=0
        lower_sentence=sentence.lower() #strings are imutable so 'sentence will not be changed if we change 'lower_sentence'
        N=len(lower_sentence)
        for i in range(0,N):
                if (lower_sentence[i]=='a' or lower_sentence[i]=='e' or lower_sentence[i]=='i' or lower_sentence[i]=='o' or lower_sentence[i]=='u'):
                        num_vowels+=1
        return num_vowels%2==0        
	
#########################################
# Question 3 - do not delete this comment
#########################################


# Write the rest of the code for question 3 below here.

def three_div(number):
        sum_div=0
        while (number>0):
                digit = number%10
                if digit%3==0:
                        sum_div+=1
                number/=10
        return sum_div
	
#########################################
# Question 4 - do not delete this comment
#########################################


# Write the rest of the code for question 4 below here.

def is_name(test_string):
        num_spaces=0
        after_space=False
        after_alpha=False
        j=0
        while j<len(test_string):
                if j==0 or after_space:
                        if not test_string[j].isupper():
                                return False
                        else:
                                after_alpha=True
                                after_space=False
                                j+=1
                                continue                        
                if (after_alpha==True):
                        if test_string[j]==' ':
                                if num_spaces!=0:                     
                                        return False
                                else:
                                        num_spaces+=1
                                        after_space=True
                                        after_alpha=False
                        elif not test_string[j].islower():
                                        return False
                        j+=1
        return num_spaces==1
                
#########################################
# Question 5 - do not delete this comment
#########################################


# Write the rest of the code for question 5 below here.

##add functions below
def find_max(grocery_list):
        index_max=0
        max_val=grocery_list[0][1]
        for i in range(1,len(grocery_list)):
               if max_val<grocery_list[i][1]:
                       index_max=i
                       max_val=grocery_list[i][1]
        return index_max

def check_list(grocery_list,maximal_budget):
                       total_price=0
                       for i in range(0,len(grocery_list)):
                               total_price+=grocery_list[i][1]
                       return total_price<=maximal_budget

def print_items(grocery_list):
        item_list=[]
        for i in range(0,len(grocery_list)):
                item_list.append(grocery_list[i][0])
        print " ,".join(item_list)        
        
##add functions above

def adjust_to_recession(grocery_list,maximal_budget):
        if len(grocery_list)==0:
                print "Empty List"
        elif check_list(grocery_list,maximal_budget):
                print_items(grocery_list)
                print "Go Shop!"
        else:      
                print "You cannot afford "+grocery_list[find_max(grocery_list)][0]
                grocery_list.pop(find_max(grocery_list))
                adjust_to_recession(grocery_list,maximal_budget)

#########################################
# Question 6 - do not delete this comment
#########################################


# Write the rest of the code for question 6 below here.

def max_column(mat):
        if len(mat)==0:
                return -1
        max_row=0
        temp=0
        max_index=0
        for i in range(0,len(mat[0])):
                for j in range(0,len(mat)):
                               temp+=mat[j][i]
                if temp>max_row:
                               max_row=temp
                               max_index=i
                temp=0
        return max_index         
	

#########################################
# Question 7 - do not delete this comment
#########################################


# Write the rest of the code for question 7 below here.

def create_matrix(m,n):
        mat=[]
        temp_mat=[]
        for i in range(0,m):
                for j in range(0,n):
                        temp_mat.append(i*n+j+1)
                mat.append(temp_mat)
                temp_mat=[]
        return mat
	
#########################################
# Question 8 - do not delete this comment
#########################################

MUL_ERROR = "Error, Matrices cannot be multiplied"

# Write the rest of the code for question 8 below here.

def multiply_matrix(A,B):
        if len(A)==0 or len(B)==0:
                return []
        m=len(A)
        n1=len(A[0])
        n2=len(B)
        p=len(B[0])
        if n1!=n2:
                return "Error, Matrices cannot be multiplied"
        mat=[]
        value=0
        temp_mat=[]
        for i in range(0,m):
                for j in range(0,p):
                        for k in range(0,n1):
                                value+=A[i][k]*B[k][j]
                        temp_mat.append(value)
                        value=0
                mat.append(temp_mat)
                temp_mat=[]
        return mat
