import os
import zipfile
import pandas as pd
import requests

r = requests.get("https://download.geonames.org/export/dump/NL.zip")
with open("NL.zip", "wb") as f:
    f.write(r.content)
with zipfile.ZipFile("NL.zip", "r") as zip_ref:
    zip_ref.extractall("./")
df = pd.read_csv("NL.txt", sep="\t", header=None)
df.columns = [
    "geonameid",
    "name",
    "asciiname",
    "alternatenames",
    "latitude",
    "longitude",
    "featureclass",
    "featurecode",
    "countrycode",
    "cc2",
    "admin1code",
    "admin2code",
    "admin3code",
    "admin4code",
    "population",
    "elevation",
    "dem",
    "timezone",
    "modificationdate",
]
# Subset op "populated places". Zie https://www.geonames.org/export/codes.html
df = df.loc[df.featurecode == "PPL"]
df = df.sort_values(by="name").reset_index(drop=True).dropna(axis=1, how="all")

# Cleanup en export
os.remove("NL.zip")
os.remove("NL.txt")
os.remove("readme.txt")
df.to_csv("./plaatsen_in_nederland.csv")
