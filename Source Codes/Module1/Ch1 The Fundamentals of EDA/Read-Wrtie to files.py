"""
Code snaps from Chapter 1
"""
# lines 5- 9 reads text file, opens is, iterates through the text file contents, and print out each line
filename = "datamining.txt"
file = open(filename, mode="r", encoding='utf-8')
for line in file:
    print(line)
file.close()
