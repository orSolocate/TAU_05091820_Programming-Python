''' Exercise #1. Python for Engineers.'''

#---Question-1-----------------------------------------------------------------
a = 1.5 # Replace ??? with a number (int/float) of your choice.
diag = 6 # Replace ??? with a number (int/float) of your choice.

# Write the rest of the code for question 1 below here.
b = ((diag**2)-(a**2))**0.5
print "Length of b is "+str(b)
print "Area is "+str(a*b)
print "Perimeter is "+str((2*a)+(2*b))



#---Question-2-----------------------------------------------------------------
a1 = 0 # Replace ??? with a positive number (int/float) of your choice.
q  = 3 # Replace ??? with a positive number (int/float) of your choice.
n  = 2 # Replace ??? with a positive integer of your choice.

# Write the code for question 2 below here.
print "The "+str(n)+" number in this series is "+str((a1*(q**(n-1))))


#---Question-3-----------------------------------------------------------------
donor = 'B' # Replace ??? with ('AB'/'A'/'B','O').
recipient = 'B' # Replace ??? with ('AB'/'A'/'B','O').

# Write the code for question 3 below here.
if ((donor=='O') or (recipient=='AB') or (donor==recipient)):
    print "True"
elif  (donor!="A" and donor!="B" and donor!="AB") or (recipient!="A" and recipient!="B" and recipient!='O'):
    print "Invalid input"
else:
    print "False"


#---Question-4-----------------------------------------------------------------
str1 = 'abcdxRz1dcb76MKab'  # Replace ??? with a string of your choice.

# Write the code for question 4 below here.
length=len(str1)
if length<6:
    print "No"
elif ((length%2)==1) and (str1[5]=='R' or str1[5]=='r') and (str1[0:4:1]==str1[length-4::1]):
    if (str1[length/2-1:length/2+2]==str1[-1:-4:-1]): #another if because if str1 is odd there is no middle char
        print 'Yes'
else: print "No"
        

#---Question-5-----------------------------------------------------------------
str2 = 'Ab$gx7Nxfcz'  # Replace ??? with a string of your choice.

# Write the code for question 5 below here.
str_new=str2[-1]+str2[1:-1]+str2[0]
if (str_new[2].islower()):
    print str_new[:2]+str_new[2].upper()+str_new[3::]
elif (str_new[2].isalpha()):
    print str_new[:2]+str_new[2].lower()+str_new[3::]
else:  print str_new[:2]+'%'+str_new[3::]
