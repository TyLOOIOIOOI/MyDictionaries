


infile = open("WorldSeriesWinners.txt", "r")
infile2 = open("WorldSeriesWinners.txt", "r")
infile3 = open("WorldSeriesWinners.txt", "r")

clubname = {}
year = {}

for t in infile:
    t = t.strip()
    if t in clubname:
        clubname[t] = clubname [t] + 1
    else:
        clubname[t] = 1


x = 1902

for y in infile2:
    y = y.strip()
    if x ==1903 or x ==1993:
        x +=2
        year[x] = y
    else:
        x += 1
        year[x] = y 

the_year = int(input("Please enter a year: "))

if the_year == 1904 or the_year == 1994:
    print ("No World Series Winner")


else:
    n = the_year
    x = year[n]
    for l in infile3:
        l = l.strip()
        if l == x:
            if l in clubname:
                clubname[t] = clubname [t] + 1
            else:
                clubname[t] = 1


    l = clubname[t] -2




print("Winner in "
    + str(n)
    + ", "
    + "was the "
    + x
    + " They won "
    + str(l)
    + " times",


)

#n = 1904

#for line in infile:
    #year[n] = line
    #n += 1
    #if line in year:
        #year[line] += 1
    #else: 
        #year[line] = 1

#print(team)
#print(year)
