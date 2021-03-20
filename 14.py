import csv

def dictionary():
    with open("iwfile.csv", 'r') as file:
        for i in csv.DictReader(file):
            print(dict(i))

dictionary()
