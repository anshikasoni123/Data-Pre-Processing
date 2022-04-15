import csv

data_set = []

with open('bright_stars.csv','r') as f:
     csvreader = csv.reader(f)
     for data in csvreader:
         data_set.append(data)

headers = data_set[0]
stars_data = data_set[1:]

for data_point in stars_data:
    data_point[2] = data_point[2].lower()

stars_data.sort(key = lambda stars_data:stars_data[2])

with open('bright_stars_sorted.csv','a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)