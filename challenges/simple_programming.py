import line

file_path = "../../../Downloads/data.dat"  #file path for the data we're working with

#initialize counter for lines
count = 0
lines = file_path.readlines()

# Strip whitespace from the line and check if it's not empty
if line.strip():
    for line in lines:  #check for the number of zeros and ones
        count_zeros = line.count('0')
        count_ones = line.count('1')

# Check if the count of 0's is a multiple of 3 or the count of 1's is a multiple of 2
if count_zeros % 3 or count_ones % 2:
    count += 1 #increment counter if condition is met
    print(count)
