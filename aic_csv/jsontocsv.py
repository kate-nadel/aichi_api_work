import json
import csv
import glob


# we need to know the headers, not all files may have all headers so make a big list first
# all headers are consistent throughout JSON files
headers = []

for filename in glob.glob("exhibitions/*.json"):
	with open(filename, "r") as data:
		json_file = json.load(data)
		for key in json_file.keys():
			if key not in headers:
				headers.append(key)

print(headers)

# make a new writer, using DictWriter

with open('csv_aic_exhibitions.csv','w') as outfile:

	# pass the headers we know about
	writer = csv.DictWriter(outfile, fieldnames=headers)

	writer.writeheader()

	# loop through the files again
	for filename in glob.glob("exhibitions/*.json"):
		with open(filename, "r") as data:
			json_file = json.load(data)
			writer.writerow(json_file)
