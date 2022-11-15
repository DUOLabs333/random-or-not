import random
import csv
import os
import struct
seed=random.Random(4817672)


#Possible choices for getting integers from os.urandom
_lambdas=[lambda : int.from_bytes(os.urandom(10),"big"),lambda : int.from_bytes(os.urandom(10),"little"),lambda : struct.unpack("i",os.urandom(4))[0]]

#Which lambda should we choose
choice=0

#The range of the random numbers to use
random_range=int(os.getenv("RANDOM_RANGE",6))
class DataCollection:
    def __init__(self,filename,_lambda):
        self.file=filename
        self.generate =lambda : _lambda()

mersenne=DataCollection('MersenneTwister',lambda : seed.randrange(1,random_range+1))


urandom=DataCollection('URandom',lambda : _lambdas[choice]() % random_range + 1)


for _ in [mersenne,urandom]:
    with open(_.file+'.csv', 'w+', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(["First Die","Second Die"])
        for i in range(1000000):
            writer.writerow([_.generate(),_.generate()])
