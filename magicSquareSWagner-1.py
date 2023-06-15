# Program name: Magic Square
# Program description:
# Author: Saran Wagner
# Date: February 5 2023

# declare and initialize variables
rowSum,colSum,diagSum = [],[],[]        # hold the sums of rows, columns, diag
magic_square = []                             # initialize 2 dimensional list

# Print Welcome Banner
print("\n*********************************")
print("* Let's test for a Magic Square *")
print("*********************************\n")



# get input from a file for magic magic_square contents and load magic_square

# should check for valid file name
file_name = input('Input the Magic Square file to be tested: ')

try:
    with open(file_name, 'r') as f:
        f.close()

except:
    print("File", file_name, "was not found")
    quit()

with open(file_name,'r') as f:
    for line in f:
        line = line.strip()
        input_row = line.split(',')
        # should check for non numbers
        try:
            for i in range(len(input_row)):  # convert strings to integers
                input_row[i] = int(input_row[i])
        except:
            print("Not a number")
            quit()
        magic_square.append(input_row)  # append each row at a time to magic_square


# Test input for magic_square size

size = len(magic_square)
valid_magic_square = True
for row in magic_square:
    if len(row) != size:
        valid_magic_square = False

# If each row is not same size as number of rows then msg and quit
if not valid_magic_square:
    print('Your input numbers do not make a magic_square.  Not magic magic_square!')
    quit()
# To get common sum, everything must be equal
commonSum = sum(magic_square[0])
# Checks sum of rows
for row in magic_square:
    if sum(row) != commonSum:
        print("Not a magic square, numbers don't add up to be the same")
        quit()
# Checks sum of collumns
for xRow in range(size):
    colsum = 0
    for yCol in range(size):
        colsum = colsum + magic_square[xRow][yCol]
    if colsum != commonSum:
        print("Not a magic square, numbers don't add up to be the same")
        quit()

# Checks diagonal sums
diagSum = 0
diagSum2 = 0
for diag in range(size):
    diagSum = diagSum + magic_square[diag][diag]
    diagSum2 = diagSum2 + magic_square[diag][size - diag - 1]
if diagSum != commonSum or diagSum2 != commonSum:
    print("Not a magic square, diagonal numbers don't add up to be the same")
    quit()

# display magic_square

print("You entered the following magic_square of size ",size)
for xRow in range(size):             # nested loop looks at all values in list
    for yCol in range(size):
        print(magic_square[xRow][yCol], end="\t")
    print()
print()
print("Magic square compatible")
print("Common sum:", commonSum)