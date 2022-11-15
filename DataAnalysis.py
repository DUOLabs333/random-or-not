import csv,os,statistics
tab="    "
#The range of the random numbers to use
random_range=int(os.getenv("RANDOM_RANGE",6))

class DataAnalysis:
    def __init__(self,filename):
        self.file=filename
        self.totals=[0]*(2*random_range+1)

mersenne=DataAnalysis("MersenneTwister")

urandom=DataAnalysis("URandom")

#Read data from csv
for _ in [mersenne,urandom]:
    with open(_.file+'.csv', 'r', encoding='UTF8') as f:
        reader = csv.reader(f)
        next(reader) #Skip header
        for row in reader:
            _.totals[int(row[0])+int(row[1])]+=1

def percent_difference(a,b):
    return (abs(a-b)/max(a,b))*100

def percent_format(a):
    return "{:.2f}%".format(a)

#Print result 
print("Results:")
percent_differences=[0,0]+[percent_difference(mersenne.totals[i],urandom.totals[i]) for i in range(2,len(mersenne.totals))]

print(tab+"Percent Differences:")
for i in range(2,len(mersenne.totals)):
    print(tab*2+str(i)+" : "+percent_format(percent_differences[i]))
print()
print(tab+"Mean: "+percent_format(statistics.mean(percent_differences)))
print()
print(tab+"Standard Deviation: "+percent_format(statistics.pstdev(percent_differences)))
print()
print()
print("Analysis:")
print(tab+"Chi-square Statistic:")
print(tab*2+"{:.3f}".format(sum([((mersenne.totals[i]-urandom.totals[i])**2)/(urandom.totals[i])])))
print()


print(tab+"Degrees of Freedom (DF):")
print(tab*2+str(2*random_range-2-1))
