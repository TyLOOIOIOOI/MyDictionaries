from pdb import line_prefix


infile = open("WorldSeriesWinners.txt", "r")

team = {}
year = {}

for t in infile:
    t = t.strip()
    if t in team:
        team[t] = team [t] + 1
    else:
        team[t] = 1


for n in range (1903, 2009):
    if n != 1904 or 1994:
        t =  n
        year[n] = t




#n = 1904

#for line in infile:
    #year[n] = line
    #n += 1
    #if line in year:
        #year[line] += 1
    #else: 
        #year[line] = 1

print(team)
print(year)
