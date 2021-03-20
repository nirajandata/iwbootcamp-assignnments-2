import csv


data=[("nirajan dhakal",18),("hari kumar",90)]

with open('iwfile.csv','w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['name','num'])
    for row in data:
        csv_out.writerow(row)