import matplotlib.pyplot as plt
from scipy import misc
import numpy as np


#-----------------------------------------------------------------------------
# Auxiliary function. Don't modify it.
def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])

#-----------------------------------------------------------------------------
# Auxiliary function. Don't modify it.
def ascii_to_np_array(s):
    return np.fromstring(s, dtype=np.uint8)

#-----------------------------------------------------------------------------

#########################################
# Question A-1 - do not delete this comment
#########################################
def load_data(filename):
    mat=[]
    row_names=[]
    try:
        f= open(filename,'r')
        column_names= f.readline().strip(',\n').split(',')
        for line in f:
            tokens=line.split(',') #now we have a list without the ','
            row_names.append(tokens[0])
            values=[float(n) for n in tokens[1:]]
            mat.append(values)
        f.close()
        column_names= np.asarray(column_names)
    except IOError:
        #print the error?
         column_names= np.asarray([])
    finally:
        data = np.asarray(mat,dtype=float)
        row_names= np.asarray(row_names)
        return data, column_names, row_names
    

#########################################
# Question A-2 - do not delete this comment
#########################################
def get_diff_values(prices):
    columns=prices.shape[1]
    b=prices-prices[:,:columns-1]
    
    
#########################################
# Question A-3 - do not delete this comment
#########################################
def get_diff_percentage(prices):
    a=get_diff_values(prices)
    #same algorithm in the previous fun
    #/left_cell*100
    #return new array

#########################################
# Question A-4 - do not delete this comment
#########################################
def get_stable(prm, share_names):
    ##boolean (need >0) 
#-----------------------------------------------------------------------------
def part1_main():
    prices, header, share_names = load_data('matrix.csv')
    print prices, '\n', header, '\n', share_names
    print get_diff_values(prices)
    prm = get_diff_percentage(prices)
    print prm
    print get_stable(prm, share_names)

#-----------------------------------------------------------------------------

#########################################
# Question B-1 - do not delete this comment
#########################################
def arr_dist(a1, a2):
    pass #Remove this line. Write you code instead.

#########################################
# Question B-2 - do not delete this comment
#########################################
def find_best_place(im, np_msg):
    pass #Remove this line. Write you code instead.

#########################################
# Question B-3 - do not delete this comment
#########################################
def create_image_with_msg(im, img_idx, np_msg):
    pass #Remove this line. Write you code instead.

#########################################
# Question B-4 - do not delete this comment
#########################################
def put_message(im, msg):
    pass #Remove this line. Write you code instead.

#########################################
# Question B-5 - do not delete this comment
#########################################
def get_message(im):
    pass #Remove this line. Write you code instead.

#-----------------------------------------------------------------------------
def part2_main():
    msg1 = 'Hello, NUMPY!'
    orig_file_name = 'parrot.png'

    im1 = misc.imread(orig_file_name)
    im2 = put_message(im1, msg1)

    plot_image = np.concatenate((im1, im2), axis=1)

    plt.figure()
    plt.imshow(plot_image, cmap=plt.cm.gray)
    plt.show()

    msg2 = get_message(im2)
    print msg2

#-----------------------------------------------------------------------------
part1_main()
part2_main()

#============================ END OF FILE ====================================
