# aichi_api_work
Working with the AICHI API and their exhibition data

In this repo are files exploring the AIC's exhibition and artwork data. The dataset was downloaded as a [data dump](https://api.artic.edu/docs/#data-dumps-vs-api), making the files easier to work with and less taxing on their servers that repeatedly accessing their API. The folder of json files titled "exhibitions" is from this data dump. The "artworks" file is in my local repo, but not on github because it is too large.

Files ending in .py are the python files used to parse the large dataset, and files ending in .json are the parsed data files combined into one relevant json file. They have similar titles to keep things consistent and as clear as possible.

In the aic_csv folder are the files relevant to transforming all of the exhibition data from the AIC into a CSV file.
