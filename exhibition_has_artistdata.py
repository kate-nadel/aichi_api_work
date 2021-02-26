import requests
import json
import glob

# EXHIBITION ENDPOINT/DATA
# work in progress! not working yet...

# this script loops through the downloaded json files to see which exhibitions have artist data
# new file created called "exhibitions_artistdata.json" listing all exhibitions containing artist data

artist_id_count = 0
for filename in glob.glob("exhibitions/*.json"):
    # print(filename)
    with open(filename, "r") as jsonfiles:
        data = json.load(jsonfiles)

        if data["artist_ids"] != []:
            artist_id_count+=1

            # print((data["id"]),(data["artwork_ids"]))

            print(artist_id_count)

            with open("exhibition_has_artistdata.json", "a") as out:
                json.dump(data, out, indent=2)

        # if data["type"] == "AIC & Other Venues":
        # if data["type"] == "Mini Exhibition":
        # if data["type"] == "Permanent Collection Special Project":
        # if data["type"] == "AIC Only":
        # if data["type"] == "Rotation":
        # if data["type"] != "AIC Only":
