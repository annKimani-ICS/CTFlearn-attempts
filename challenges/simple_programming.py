#open data file
file_path = "../../../Downloads/data.txt"  #file path for the data we're working with

Lines = 0
with open(file_path, 'r') as file:
    #iterate through each line and count the number of zeros and ones
    for line in file:
        count_zeros = line.count("0")
        count_ones = line.count("1")

        #if condition is met increment the counter by one
        if count_ones % 2 == 0 or count_zeros % 3 == 0:
            Lines += 1
            print(Lines)
