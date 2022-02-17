infile = open("AI.txt", "r")
import string 
#data = infile.read()

freq_dict = {}
wordcount = 0

removetable = str.maketrans("", "", string.punctuation)
infile = [s.translate(removetable)for s in infile]

for line in infile:
    line = line.strip()
    line = line.lower()
    words = line.split (" ")


for w in words:
    if w in freq_dict:
        freq_dict[w] = freq_dict[w] + 1
    else:
        freq_dict[w] = 1


print(freq_dict)


#occurrences = data.count("artificial")
#print('Number of occurrences of the word :', occurrences)

