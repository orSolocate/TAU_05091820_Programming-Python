#########################################
# Question 1a - do not delete this comment
#########################################
import math

def map_bin2dec(n):
    dic_length=int(math.pow(2,n))
    dic={}
    strings=range(dic_length-1,-1,-1)
    for decimal in strings:
        key=bin(decimal)[2:].zfill(n)
        dic[key]=str(decimal)
    return dic

#########################################
# Question 1b - do not delete this comment
#########################################

def bin_triplets_to_decimal(bin_str):
    length=len(bin_str)
    num=[] #List of the final number we want to return at the end
    if length==0:
        return "0"
    for index in range(0,length,3):
        triplet=bin_str[index:index+3]
        count=map_bin2dec(3).get(triplet)
        num.append(count)
    return ('').join(num)

#########################################
# Question 2a - do not delete this comment
#########################################

def swap_student_courses(students_dict):
    courses_dict={}
    for name in students_dict:
        for course in students_dict[name]:
            stud_in_course=[]
            if courses_dict.has_key(course):
                stud_in_course=courses_dict.get(course)
            stud_in_course.append(name)
            courses_dict[course]=stud_in_course
    return courses_dict

#########################################
# Question 2b - do not delete this comment
#########################################

def count_courses_intersection(courses_dict):
    pairs_dict={}
    for course1 in courses_dict:
        for course2 in courses_dict:
            if course2!=course1:
                if not (pairs_dict.has_key((course1,course2)) or pairs_dict.has_key((course2,course1))):                
                    count=0
                    for name in courses_dict.get(course1):
                        for name2 in courses_dict.get(course2):
                            if name==name2:
                                count+=1
                    pair=(course1,course2)
                    pairs_dict[pair]=count
    return pairs_dict     

#########################################
# Question 3a - do not delete this comment
#########################################

def filter_text(text):#string list
    lst=[]
    for i in range(0,len(text)):
        if not text[i] in lst:
            lst.append(text[i])
    return lst    

def find_following_words(text):
    dic={}
    text=text.lower()
    text_list=filter_text(text.split())                                
    for word in text_list:
        chains=[]
        for word2 in text_list:                                                                                           
            if word[-1]==word2[0]:
                if dic.has_key(word):
                    chains=dic.get(word)
                chains.append(word2)
        chains.sort() ## sorting the new list
        dic[word]=chains
    return dic

#########################################
# Question 3b - do not delete this comment
#########################################

def play_word_chain(text, word):
    text=text.lower()
    unused_list=filter_text(text.split())
    cur_word=word.lower()
    dic=find_following_words(text)
    used_list=[]
    used_list.append(cur_word)
    print cur_word
    unused_list.remove(cur_word)
    while dic.get(cur_word)!=[]:
        for i in dic.get(cur_word):
            if i not in used_list:
                print i
                used_list.append(i)
                cur_word=i
                unused_list.remove(i)
                break        
    return unused_list        

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

print map_bin2dec(1)
print map_bin2dec(2)

print bin_triplets_to_decimal("001111")
print bin_triplets_to_decimal("110011")

print swap_student_courses({"Yuval": ["Math", "Computer Science", "Statistics"],\
                      "Gal": ["Algebra", "Statistics", "Physics"],\
                      "Noam": ["Statistics", "Math", "Programming"]})
print count_courses_intersection({'Bible': ['Daniel', 'Roni'],\
                                 'Psychology': ['Roni'], 'Biology': ['Daniel']})

print find_following_words("The little girl sings a Song")

unused_words = play_word_chain("The little girl sings a Song", "sings")
print unused_words

unused_words = play_word_chain("The little girl sings a Song", "tHe")
print unused_words
