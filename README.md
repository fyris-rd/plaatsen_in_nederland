# plaatsen_in_nederland

Geolocaties voor alle plaatsen in Nederland. Data verzameld uit GeoNames dump: https://download.geonames.org/export/dump/.

## Installatie

```shell
docker build -t plaatsen_in_nederland .
```

## Gebruik

```shell
docker run -v $(pwd):/app plaatsen_in_nederland
```

| Kolom             | Beschrijving                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------- |
| geonameid         | Integer id of record in geonames database                                                                                 |
| name              | Name of geographical point (utf8)                                                                                         |
| asciiname         | Name of geographical point in plain ascii characters                                                                      |
| alternatenames    | Alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table |
| latitude          | Latitude in decimal degrees (wgs84)                                                                                       |
| longitude         | Longitude in decimal degrees (wgs84)                                                                                      |
| feature class     | See [Geonames Feature Class Codes](http://www.geonames.org/export/codes.html)                                             |
| feature code      | See [Geonames Feature Codes](http://www.geonames.org/export/codes.html)                                                   |
| country code      | ISO-3166 2-letter country code                                                                                            |
| cc2               | Alternate country codes, comma separated, ISO-3166 2-letter country code                                                  |
| admin1 code       | Fipscode (subject to change to iso code), see exceptions below                                                            |
| admin2 code       | Code for the second administrative division, a county in the US                                                           |
| admin3 code       | Code for third level administrative division                                                                              |
| admin4 code       | Code for fourth level administrative division                                                                             |
| population        | Bigint (8 byte int)                                                                                                       |
| elevation         | In meters, integer                                                                                                        |
| dem               | Digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' or 30''x30'' area in meters                       |
| timezone          | The IANA timezone id (see file timeZone.txt)                                                                              |
| modification date | Date of last modification in yyyy-MM-dd format                                                                            |
