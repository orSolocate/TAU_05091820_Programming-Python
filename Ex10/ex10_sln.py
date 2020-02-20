import matplotlib.pyplot as plt
from scipy import misc
import numpy as np

#-----------------------------------------------------------------------------
def load_data(filename):
    f = None
    try:
        f = open (filename,'r')
        column_names = f.readline().strip('\n').split(',')
        row_names = []
        data = []        
        for line in f: 
            tokens = line.strip('\n').split(',')
            row_names.append(tokens[0]) 
            values = [float(n) for n in tokens[1:]] 
            data.append(values)
    except IOError as err:
        print err.filename, ':', err.strerror
        column_names = []
        row_names = []
        data = []
    finally:
        if f:
            f.close()
        column_names = np.asarray(column_names)
        row_names = np.asarray(row_names)
        data = np.asarray(data, dtype=float)
    return data, column_names, row_names

#-----------------------------------------------------------------------------
def get_diff_values(m):
    return m - np.concatenate( (m[:,:1], m[:, 0:(m.shape[1]-1)]), axis=1)

#-----------------------------------------------------------------------------
def get_diff_percentage(m):
    return 100. * get_diff_values(m)/np.concatenate((np.ones((m.shape[0],1)),
                                                    m[:,:-1]), axis=1 )

#-----------------------------------------------------------------------------
def get_stable(prm, monikers):
    return monikers[(prm >= 0).all(axis=1)]

#-----------------------------------------------------------------------------
def part1_main():
    m, header, monikers  = load_data('matrix.csv')
    print m
    print get_diff_values(m)
    d = get_diff_percentage(m)
    print d
    print get_stable(d, monikers)

#-----------------------------------------------------------------------------
def arr_dist(a1, a2):
    return abs(np.int_(a1) - np.int_(a2)).sum()

#-----------------------------------------------------------------------------
def np_array_to_ascii(darr):
    return ''.join([chr(item) for item in darr])

#-----------------------------------------------------------------------------
def ascii_to_np_array(s):
    return np.fromstring(s, dtype=np.uint8)

#-----------------------------------------------------------------------------
def put_message(im, msg):
    np_msg = ascii_to_np_array(msg)
    img_idx = find_best_place(im, np_msg)
    im1 = create_image_with_msg(im, img_idx, np_msg)
    return im1

#-----------------------------------------------------------------------------
def find_best_place(im, np_msg):
    r, c = im.shape
    min_idx = 0
    min_dist = 100000
    m = min(r,256)
    n = min(c - len(np_msg) + 1, 256)
    for i in range(m):
        for j in range(n):
            if i == 0 and j < 3:
                #Preserve 3 bytes for the meta-data
                continue
            curr_dist = arr_dist(im[i:i+1, j:j+len(np_msg)][0], np_msg)
            if min_dist >= curr_dist:
                min_dist = curr_dist
                min_idx = (i,j)
    return min_idx

#-----------------------------------------------------------------------------
def create_image_with_msg(im, img_idx, np_msg):
    im1 = im.copy()
    im1[img_idx[0]:img_idx[0]+1, img_idx[1]:img_idx[1]+len(np_msg)] = np_msg
    im1[0][0] = img_idx[0]
    im1[0][1] = img_idx[1]
    im1[0][2] = len(np_msg)
    return im1

#-----------------------------------------------------------------------------
def get_message(im):
    l = im[0][2]
    r = im[0][0]
    c = im[0][1]
    np_msg = im[r:r+1, c:c+l]
    msg = np_array_to_ascii(np_msg[0])
    return msg

#-----------------------------------------------------------------------------
def part2_main():
    msg1 = 'Hello, NUMPY!'
    orig_file_name = 'parrot.png'

    im1 = misc.imread(orig_file_name)
    im2 = put_message(im1, msg1)

    #misc.imsave('parrot_encr.png', im2)

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
