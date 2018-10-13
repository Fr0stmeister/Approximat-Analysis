# Made by Frostmeister
# Enter the plinth area and rate of construction of super-structure

plinthA = int(input('Enter the total plinth area in sq.m : '))

rateSuper = int(input('Enter the cost of construction of super-structure in Rs/sq.m : '))

costSuper = plinthA * rateSuper
print('The cost of construction of super-structure is : ' + str(costSuper))

costSub = 0.2*costSuper
print('The cost of construction of sub-structure is : ' + str(costSub))

costTotal = costSub + costSuper
print('The total cost of construction of super structure and sub structure is : ' + str(costTotal))


print('The additional costs are as follows')
for i in range (10):
    print('-', end = ' ')

costWS = 0.05 * costTotal
print('Water Supply : '+ str(costWS))
costS = 0.05 * costTotal
print('Sanitation : ' + str(costS))
costElect = 0.09 * costTotal
print('electricity : ' + str(costElect))
costArch = 0.01 * costTotal
print('Architectural : ' + str(costArch))
costM = 0.05 * costTotal
print('Miscellaneous : ' + str(costM))


for i in range (10):
    print('-', end = ' ')

addCost = costWS + costS + costM + costElect + costArch
print('The total additional cost is : ' + str(addCost))

overCost = costTotal + addCost
print('The overall cost of construction and additional cost is : ' + str(overCost))


costCont = 0.05 * overCost
print('The cost for contingencies is : ' + str(costCont))
costWCE = 0.10 * overCost
print('The cost for work charge establishment is : ' + str (costWCE))

costFinal = overCost + costCont + costWCE
print('The final cost of construction will be : ' + str(costFinal))