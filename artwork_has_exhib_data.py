import requests
import json
import glob

# ARTWORKS ENDPOINT /DATA
# this script collects all data for artworks where exhibition_history has a value
# generates artwork_has_exhib_data.json file

artwork_has_data = 0
for filename in glob.glob("artworks/*.json"):

    with open(filename, "r") as jsonfiles:
        data = json.load(jsonfiles)

        if data["exhibition_history"] != None:
            artwork_has_data +=1
            print(data["id"], data["exhibition_history"])
            print(artwork_has_data)

            with open("artwork_has_exhib_data.json", "a") as out:
                json.dump(data, out, indent=2)
