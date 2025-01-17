import pprint

#Color aesthetics with regard to product design and multimedia web pages
#https://eds.p.ebscohost.com/eds/pdfviewer/pdfviewer?vid=1&sid=343c0a69-29b8-40d8-a145-c9718a483064%40redis

#Investigating Color-Blind User-Interface Accessibility via Simulated Interfaces
#https://mdpi-res.com/computers/computers-13-00053/article_deploy/computers-13-00053.pdf?version=1708147771

f = open("../datafiles/Archive__COVID-19_Vaccination_and_Case_Trends_by_Age_Group__United_States.csv")
lines = f.readlines()
f.close()

# #each bucket will have [[time],[value]]
# buckets = {
#     "<2 Years":[[],[]],
#     "2 - 4 Years":[[],[]],
#     "5 - 11 Years":[[],[]],
#     "12 - 17 Years":[[],[]],
#     "18 - 24 Years":[[],[]],
#     "25 - 49 Years":[[],[]],
#     "50 - 64 Years":[[],[]],
#     "65+ Years":[[],[]]
# }
# labels = lines[0].split(",")
# print(labels)

# for line in lines[1:]:
#     line = line.split(",")
#     buckets[line[1]][0].append(line[0])
#     buckets[line[1]][1].append(line[3])

# pprint.pprint(buckets["<2 Years"])

f = open("../datafiles/processed_vax.csv","w")
f.write("date,ageGroup,vaxxed\n")

for line in lines[1:]:
    line = line.split(",")
    date = line[0].split(" ")[0]
    f.write(f"{date},{line[1]},{line[3]}\n")

f.close()