#########################################
# Question 1 - do not delete this comment
#########################################

def reverse_string(s):
    res=''
    if s=='':
        return ''
    rec_res=reverse_string(s[0:-1])
    res+=s[-1]
    res+=rec_res
    return res

#########################################
# Question 2 - do not delete this comment
#########################################


def min_sublist_sum(numbers, target):
    if target==0:
        return 0
    if numbers==[]:
        return float("inf")
    if target<0:
        return float("inf")
    option1=min_sublist_sum(numbers[:-1],target-numbers[-1])
    option2=min_sublist_sum(numbers[:-1],target)
    if option1<option2: #if we 'used' the number
        return option1+1
    if option2<=option1: #if we did not use the last nunmber
        return option2
    elif option1==float("inf"): return float("inf")
    else: return float("inf")

#########################################
# Question 3 - do not delete this comment
#########################################


def uncover_cell(ms_board, ms_revealed, idx):
    if idx>len(ms_board)-1 or idx<-1*(len(ms_board)-1): #index out of range
        return ms_revealed        
    if ms_revealed[idx]==True:#cell has already been opened
        return ms_revealed
    if ms_board[idx]=='*': #stepped on a mine!
        ms_revealed[idx]=True
        print('boom!')
        return ms_revealed
    if ms_board[idx]>0 or (ms_board[idx]==0 and (idx==0 and idx==len(ms_board)-1)):
        #'1' or '2' or '0' in both edges the edge
        ms_revealed[idx]=True
        return ms_revealed
    #if we got here the cell contains '0'
    ms_revealed[idx]=True
    if idx==0: # we only need to reveal cells on the right
        return uncover_cell(ms_board, ms_revealed, idx+1)
    if idx==len(ms_board)-1:# we only need to reveal cells on the left
        return uncover_cell(ms_board, ms_revealed, idx-1)
    # the '0' is in the middle of the board
    rev_left=uncover_cell(ms_board, ms_revealed, idx-1)
    rev_right=uncover_cell(ms_board, ms_revealed, idx+1)
    return rev_left and rev_right

#########################################
# Question 4 - do not delete this comment
#########################################


def is_valid_paren(s, cnt=0):
    if s=='' and cnt==0: #empty list and no open parens
        return True
    if s=='' and cnt!=0: #empty list but open parens!
        return False
    while s[-1]!=')' and s[-1]!='(':
            s=s[:-1] #cut the last char, because it is not a paren
            if s=='' and cnt==0: #repeat the conditions for empty list from the begining
                return True
            if s=='' and cnt!=0:
                return False
    if s[-1]=='(':
        if cnt==0:
            return False #means there is '(' without ')' beforehand
        s=s[:-1] #cut the '(' char and continue to scan
        return is_valid_paren(s,cnt-1) #less one '(' but we are still going
    if s[-1]==')':
        s=s[:-1] #cut the ')' char and continue to scan
        return is_valid_paren(s,cnt+1) #one more ')' but we are still going

    
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

assert reverse_string("abc") == "cba"
assert reverse_string("Hello!") == "!olleH"

assert min_sublist_sum([0,1,2,1], 2) == 1
assert min_sublist_sum([0,1,1], 2) == 2
assert min_sublist_sum([0,1,1], 3) == float("inf")

ms_board = ["*", 1, 0, 0, 0, 1, "*", 2, "*", 1, 0, 0, 0, 0]
ms_revealed = [False]*len(ms_board)

ms_revealed1 = uncover_cell(ms_board, ms_revealed, 1)
ms_revealed2 = uncover_cell(ms_board, ms_revealed1, 2)
ms_revealed3 = uncover_cell(ms_board, ms_revealed2, 11)
ms_revealed4 = uncover_cell(ms_board, ms_revealed3, 6)


assert is_valid_paren("(.(a)") == False
assert is_valid_paren("p(()r((0)))") == True
