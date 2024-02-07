import pandas as pd

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
# Subset for "populated places" only. See https://www.geonames.org/export/codes.html
df = df.loc[df.featurecode == "PPL"]
df = df.sort_values(by="name").reset_index(drop=True).dropna(axis=1, how="all")
df.to_csv("./plaatsen_in_nederland.csv")
