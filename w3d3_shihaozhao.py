# ~ w3d3_shihao zhao
file = open ('my_file.txt','r')
num_words = file.read()
words = num_words.split()
lines = num_words.split('\n')
print('The number of words:',len(words))
print('The number of lines:',len(lines))
