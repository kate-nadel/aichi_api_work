import requests
import json
import glob

# this script collects all data for exhibitions where type = AIC & Other Venues
traveling_exhib_count = 0
for filename in glob.glob("exhibitions/*.json"):

    with open(filename, "r") as jsonfiles:
        data = json.load(jsonfiles)

        if data["type"] == "AIC & Other Venues":
            print(data)

            with open("AICOTHERS_exhibitions.json", "a") as out:
                json.dump(data, out, indent=2)
