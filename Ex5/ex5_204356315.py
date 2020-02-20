#########################################
# Question 1 - do not delete this comment
#########################################

# Write the rest of the code for question 1 below here.

def sum_file_nums(infile):
    line_sum=0
    f= open(infile,'r')
    for line in f:
        line_sum+=float(line)
    f.close()
    return line_sum

#########################################
# Question 2 - do not delete this comment
#########################################

# Write the rest of the code for question 2 below here.

def filter_file_nums(infile, outfile): #assuming that infile contains integers (1 for each line)
    inp=open(infile,'r')
    out=open(outfile,'w')
    for line in inp:
        if int(line)%3==0:
            out.write(line) 
    inp.close()
    out.close()
    return None

#########################################
# Question 3 - do not delete this comment
#########################################


# Write the rest of the code for question 3 below here.

def get_x_freqs(infile, outfile, x):
    inp=open(infile,'r')
    out=open(outfile, 'w')
    dicx={}
    for line in inp:
        line=line.lower().split()
        for word in line:
            count=0
            if dicx.has_key(word):
                count=dicx[word]
            dicx[word]=count+1
    any_words=False
    for word in dicx.keys():
        if dicx[word]>=x:
            any_words=True
            out.write(word+'\n')
    if any_words==False:
                      out.write('no_words!\n')
    inp.close()
    out.close()
    return None


#########################################
# Question 4 - do not delete this comment
#########################################


# Write the rest of the code for question 4 below here.

def get_csv_matrix(infile):
    inp=open(infile,'r')
    matrix=[]
    tokens=[]
    is_first_line=True
    i=1 #line number
    for line in inp: 
        tokens=(line.rstrip().split(','))#list of lists of words for each line
        if is_first_line:
            col_length=len(tokens)
        tokens_float=[]
        try:
            for j in range(0,col_length):
                tokens_float.append(float(tokens[j]))
            matrix.append(tokens_float)
            is_first_line=False
            i+=1
        except IndexError:
                        print ('Inconsistent number of fields detected in line ' +str(i))
                        inp.close()
                        return None
        except ValueError:
                           print ('Non-numeric field encountered in line '+str(i))
                           inp.close()
                           return None
    inp.close()
    return matrix


#########################################
# Question 5 - do not delete this comment
#########################################

# Write the rest of the code for question 5 below here.

def map_to_dict(mapping_file): #return a dictionary of the mapping file
    inp=open(mapping_file,'r')
    dic={}
    for line in inp:
        tokens=(line.rstrip().split(','))
        dic[tokens[0]]=tokens[1]
    inp.close()
    return dic
    

def decode(input_text_file, code_mapping_file, output_text_file):
    try:
        inp=open(input_text_file,'r')
        dic_map=map_to_dict(code_mapping_file)
        out=open(output_text_file,'w')
        line=inp.readline().split(' ')
        for number in line:
            if not dic_map.has_key(number):
                raise ValueError("Missing decrypting for code "+str(number))
            out.write(dic_map[number])
        out.write('\n')
    except IOError:
        print("IO error encountered, cannot decode, exiting!")        
    finally:
        if inp is not None:
            inp.close()
        if out is not None:
            out.close()
    return None
