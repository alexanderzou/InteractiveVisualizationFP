import pprint

f = open("../datafiles/parsedconditioncontributingdeathdata.csv")
lines = f.readlines()
f.close()

#format: {"state,conditiongroup,agegroup": deaths}
data = {}

for line in lines[1:]:
    line = line.split(",")
    state,condition,age = line[0],line[1],line[-2]
    if condition.startswith("\""):
        condition = "Adverse Events"
    key = f"{state},{condition},{age}"
    if key not in data.keys():
        data[key] = 0
    if line[-1] == "\n":
        continue
    deaths = float(line[-1])
    data[key] += deaths

#pprint.pprint(data)

g = open("../datafiles/processed_conditions.csv","w")
g.write("State,ConditionGroup,AgeGroup,COVID19Deaths\n")
for k in data.keys():
    g.write(k+","+str(data[k])+"\n")
g.close()
