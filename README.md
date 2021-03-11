# aichi_api_work
Working with the AICHI API and their exhibition data

In this repo are files exploring the AIC's exhibition and artwork data. The dataset was downloaded as a [data dump](https://api.artic.edu/docs/#data-dumps-vs-api), making the files easier to work with and less taxing on their servers that repeatedly accessing their API. The folder of json files titled "exhibitions" is from this data dump. The "artworks" file is in my local repo, but not on github because it is too large.

Files ending in .py are the python files used to parse the large dataset, and files ending in .json are the parsed data files combined into one relevant json file. They have similar titles to keep things consistent and as clear as possible.

In the aic_csv folder are the files relevant to transforming all of the exhibition data from the AIC into a CSV file.


Files:

[artwork_has_exhib_data.json](https://github.com/perceptionmgmt/aichi_api_work/blob/main/artwork_has_exhib_data.json) - this files loops through the artwork data and if the field "exhibition_history" is not equal to None, the artwork is added to this json file.

[exhib_has_artworkandartist.json](https://github.com/perceptionmgmt/aichi_api_work/blob/main/exhib_has_artworkandartist.json) - this file loops through exhibition data and if "artist_ids" and "artwork_ids" are not null (or []) then the exhibition file is added to this json file. These are the exhibitions that have both artist data and artwork/object data.

[exhibition_has_artistdata.json](https://github.com/perceptionmgmt/aichi_api_work/blob/main/exhibition_has_artistdata.json) - similarly, this file only has exhibitions that contain data in the "artist_ids" field.

[exhibition_has_artworkdata.json](https://github.com/perceptionmgmt/aichi_api_work/blob/main/exhibition_has_artworkdata.json) - and again, this file only has exhibitions that contain data in the "artwork_ids" field.

[not_AICONLY_exhibitions.json](https://github.com/perceptionmgmt/aichi_api_work/blob/main/not_AICONLY_exhibitions.json) - this file contains any exhibition where "type" does not equal "AIC Only" (includes “Rotation,” “AIC & Other Venues,” null, “Mini Exhibition,” “Permanent Collection Special Project”)

[AICOTHERS_exhibitions.json](https://github.com/perceptionmgmt/aichi_api_work/blob/main/AICOTHERS_exhibitions.json) - this file contains the exhibitions where "type" equals "AIC & Other Venues" (what we would consider traveling exhibitions)

In the [aic_csv](https://github.com/perceptionmgmt/aichi_api_work/tree/main/aic_csv) are the following files and the scripts that produced them:

[csv_aic_exhibitions.csv](https://github.com/perceptionmgmt/aichi_api_work/blob/main/aic_csv/csv_aic_exhibitions.csv) - this file is a large file of all of the exhibition data organized as a csv and includes the headings

id  | api_model |  api_link | title | is_featured | description | short_description | web_url  | image_url | type | status  |  aic_start_at | aic_end_at | date_display | department_display |  gallery_id | gallery_title |  artwork_ids |  artwork_titles | artist_ids  | site_ids | image_id | alt_image_ids | document_ids | suggest_autocomplete_all | last_updated_source |  last_updated | timestamp | suggest_autocomplete_boosted    

[csv_text.csv](https://github.com/perceptionmgmt/aichi_api_work/tree/main/aic_csv) was just a test run
