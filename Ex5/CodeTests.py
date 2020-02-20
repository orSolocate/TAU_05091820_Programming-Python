'''
The next code block executes several tests of common scenarios for your aid. 
You are more than welcome to add tests of your own, but it's not mandatory.
'''
import ex5_204356315
import filecmp


def check_q3(outfile, expected_out):
    f = open(outfile, "r")
    f_expected = open(expected_out, "r")
    lines = f.readlines()
    expected_line = f_expected.readlines()
    lines.sort()
    expected_line.sort()
    i = 0
    for i in range(len(lines)):
        assert (lines[i] == expected_line[i])
    assert (len(lines) == len(lines))

# TEST FOR Q1
infile = "q1_in.txt"
assert(ex5_204356315.sum_file_nums(infile)==8.0)
infile = "q1_in2.txt"
assert(ex5_204356315.sum_file_nums(infile)==0.0)

# TEST FOR Q2
infile = "q2_in.txt"
outfile = "q2_out.txt"
expected_out = "q2_out_expected.txt"
ex5_204356315.filter_file_nums(infile,outfile)
assert(filecmp.cmp(outfile,expected_out) == True)

# TEST FOR Q3
infile = "q3_in.txt"
outfile = "q3_out.txt"
expected_out = "q3_out_expected.txt"
x=2
ex5_204356315.get_x_freqs(infile, outfile, x)
check_q3(outfile,expected_out)

infile = "q3_in_2.txt"
outfile = "q3_out2.txt"
expected_out = "q3_out_expected2.txt"
x=2
ex5_204356315.get_x_freqs(infile, outfile, x)
assert(filecmp.cmp(outfile,expected_out) == True)

# TEST FOR Q4
infile = "q4_good.csv"
matrix = ex5_204356315.get_csv_matrix(infile)
assert(matrix == [[1.0,9.0,5.0,78.0],[4.9,0.0,24.0,7.0],[6.0,2.0,3.0,8.0],[10.0,21.4,8.0,7.0]])

infile = "q4_bad.csv"
matrix = ex5_204356315.get_csv_matrix(infile)
assert(matrix == None)

infile = "q4_bad2.csv"
matrix = ex5_204356315.get_csv_matrix(infile)
assert(matrix == None)


# TEST FOR Q5
input_text_file = 'q5_good_text.txt'
code_mapping_file = 'q5_mapping.txt'
output_text_file = 'q5_out.txt'
output_text_file_expected = 'q5_out_expected.txt'

ex5_204356315.decode( input_text_file, code_mapping_file , output_text_file)
assert(filecmp.cmp(output_text_file_expected,output_text_file) == True)


input_text_file = 'q5_bad_text.txt'
code_mapping_file = 'q5_mapping.txt'
output_text_file = 'q5_out2.txt'
output_text_file_expected = 'q5_out_expected2.txt'

#try:
ex5_204356315.decode( input_text_file, code_mapping_file , output_text_file)
#except ValueError as err:
#    print err.args[0]
#    assert (err.args[0] == "Missing decrypting for code 99")
#assert(filecmp.cmp(output_text_file_expected,output_text_file) == True)


print 'Congrats!!!'
print 'All preliminary tests passed!'
