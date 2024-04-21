import pprint

f = open("../datafiles/parsedconditioncontributingdeathdata.csv")
lines = f.readlines()
f.close()

#format: {"state,conditiongroup,agegroup": deaths}
data = {}

for line in lines[1:]:
    line = line.split(",")
    if line[-1] == "\n":
        continue
    state,condition,age,deaths = line[0],line[1],line[3],float(line[-1])
    key = f"{state},{condition},{age}"
    if key not in data.keys():
        data[key] = 0
    data[key] += deaths

#pprint.pprint(data)

g = open("../datafiles/processed_conditions.csv","w")
g.write("State,ConditionGroup,AgeGroup,COVID19Deaths\n")
for k in data.keys():
    g.write(k+","+str(data[k])+"\n")
g.close()
