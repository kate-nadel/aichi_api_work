import json
import csv
import glob

for filename in glob.glob("exhibitions/*.json"):
    # print(filename)
    with open(filename, "r") as data:
        json_file = json.load(data)

# single file:
# json_file=open("exhibitions/6405.json","r")

csv_file=open("csv_text.csv", "w")

json_data_topython_dict=json.load(json_file)
write=csv.writer(csv_file)

write.writerow(json_data_topython_dict.keys())
write.writerow(json_data_topython_dict.values())

json_file.close()
csv_file.close()






#
#
# data = " "
#
#
# with open("exhibitions/6405.json", "r") as jsonfiles:
#     data = json.load(jsonfiles)
#
# with open("csv_test.csv", "w") as f:
#     fieldnames = data.dict()
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for item in data:
#         writer.writerow(item)




#     for line in jsonfiles.read():
#         data += line
#
# data = json.loads(data)
#
# # print(json.dumps(data, indent=2))
#
# print(type(data))
# csv_name = "aic_exhibitions.csv"
#
# with open("aic_exhibitions.csv", "w") as jsonfiles:
#     writer = csv.DictWriter(jsonfiles, data[0])
#     writer.writeheader()
#
#     for item in data:
#         writer.writerow(item)



        # csv_file = csv.writer(out)
        # csv_file.writerow(["ID", "Api_model"])
        # for item in data:
        #     csv_file.writerow([item["id"], item["api_model"]])
#








# , "api_link", "title", "description", "short_description", "web_url", "type", "aic_start_at", "aic_end_at", "date_display", "department_display", "artwork_ids", "artwork_titles", "artist_ids", "image_id", "document_ids"])
# for item in data:

#, item["api_link"], item["title"], item["description"], item["short_description"], item["web_url"], item["type"], item["aic_start_at"], item["aic_end_at"], item["date_display"], item["department_display"], item["artwork_ids"], item["artwork_titles"], item["artist_ids"], item["image_id"], item["document_ids"]])
