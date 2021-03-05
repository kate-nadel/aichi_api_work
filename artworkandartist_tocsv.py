import json
import csv

#converting artworkandartist json file to csv
# does not work -- issue with jsonfiles? no " ,"

with open("exhib_has_artworkandartist.json", "r") as f:

    data = json.load(f)

csv_file = open("exhib_has_artworkandartist.csv", "w")

writer = csv.writer(csv_file)

count = 0

for item in data:
    if count == 0:
        header = item.keys()
        writer.writerow(header)
        count += 1

    writer.writerow(data.values())

data_file.close()
