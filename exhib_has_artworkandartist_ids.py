import requests
import json
import glob

# EXHIBITION ENDPOINT/DATA


# this script loops through the downloaded json files to see which exhibitions have artist and artwork data
# new file created called "exhib_has_artworkandartist.json" listing all exhibitions containing artist data

artistandartwork_id_count = 0
for filename in glob.glob("exhibitions/*.json"):
    # print(filename)
    with open(filename, "r") as jsonfiles:
        data = json.load(jsonfiles)

        if data["artist_ids"] != []:
            if data["artwork_ids"] != []:

                artistandartwork_id_count+=1

            # print((data["id"]),(data["artwork_ids"]))

                print(artistandartwork_id_count)
                # print(data)

                # with open("exhib_has_artworkandartist.json", "a") as out:
                #     json.dump(data, out, indent=2)
