from FE_Base import feature_extracting, shuffle_record, test_phenotype
from gogenpy import utils
    
randomizer = utils.randomizer
records = []
for i in xrange(100):
    c = 'class 1';
    x = 0
    y = randomizer.randrange(1,5)
    z = randomizer.randrange(1,5)
    r1 = randomizer.randrange(1,5)
    r2 = randomizer.randrange(1,5)
    r3 = randomizer.randrange(1,5)
    r4 = randomizer.randrange(1,5)
    records.append([x,y,z,r1,r2,r3,r4,c])

for i in xrange(100):
    c = 'class 2';
    y = 0
    x = randomizer.randrange(1,5)
    z = randomizer.randrange(1,5)
    r1 = randomizer.randrange(1,5)
    r2 = randomizer.randrange(1,5)
    r3 = randomizer.randrange(1,5)
    r4 = randomizer.randrange(1,5)
    records.append([x,y,z,r1,r2,r3,r4,c])

for i in xrange(100):
    c = 'class 3';
    z = 0
    y = randomizer.randrange(1,5)
    x = randomizer.randrange(1,5)
    r1 = randomizer.randrange(1,5)
    r2 = randomizer.randrange(1,5)
    r3 = randomizer.randrange(1,5)
    r4 = randomizer.randrange(1,5)
    records.append([x,y,z,r1,r2,r3,r4,c])

variables = ['x','y','z','r1','r2','r3','r4']
records = shuffle_record(records)

'''
test_phenotype(records, variables, 'sqr(cos(abs(x)))')
test_phenotype(records, variables, 'x')
test_phenotype(records, variables, 'y')
test_phenotype(records, variables, 'z')
'''
feature_extracting(records, variables, label='Ideal-data-5-Fold', fold=5)
feature_extracting(records, variables, label='Ideal-data-1-Fold', fold=1)
