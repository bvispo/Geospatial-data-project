# Geospatial-data-project
![foto](https://github.com/bvispo/Geospatial-data-project/blob/main/images/ciudad.jpg)


# Objetive
The objective of this project is to determine the perfect location for a new company in the gaming industry. 

Some of th given requisites where:
- **Designers** --> near to companies that do design.
- **30% of the company** --> have at least 1 child.
- **Developers** --> to be near tech startups that have raised at least 1 Million dollars.
- **Executives** --> like Starbucks.
- **Account managers** --> travel a lot.
- **Average age between 25 and 40** -->some place to go party.
- **CEO** --> vegan.
- **Maintenance guy** --> basketball court
- **Dog—"Dobby"** --> hairdresser every month. 

The first filters I applied to look for possible locations were:
 1. Madrid, Lisbon and London. These are three metropolitan capitals where one can easily find tech hubs.
 2. Requisites chossen: Starbucks, Bars, Preschool and train stations.
 
# Working plan 
​
Before first filtering using MondoDB, I set an strategic location for each city, setting it up where most entreprises where settled on each citie. These were:
 - Madrid: Paseo de la Castellana.
 - Lisbon: Avenida Antonio Augusto de Aguiar.
 - London: St Paul´s Cathedral.

 These coordinates were used to realice the API Foursquare calls, using **Starbucks, Bars, and Train Stations** in the three given cities: **Madrid, Lisbon and London**.


​Once all the information was downloaded in json format, I made a calculation of the distances between the coordinates of origin and the information obtained from Foursquare. 
​
For the final decision of the location I have made a normalisation and assigned weights to the distances obtained. In the end, a ranking was obtained on which the final decision was based. 
​
The following resources have been used to achieve the objective of this project: 
​
-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.
​
​
### Structure of the project files
- **Src folder**, which contains the several functions applied along the project.
- **Data_jsons**: folder that contains the different json files used in MongoDB.
- **Two jupyter notebooks**: one, collections.ipynb, where I have called the Foursquare API. And the second, geoqueries.ipynb, where the different geoqueries are done.
- **Readme**
- **.gitignore**
​
# Libraries
​
[sys](https://docs.python.org/3/library/sys.html)

[import requests](https://pypi.org/project/requests/2.7.0/)

[pandas](https://pandas.pydata.org/)

[dotenv](https://pypi.org/project/python-dotenv/)

[pymongo](https://www.mongodb.com/2)

[json](https://docs.python.org/3/library/json.html)

[os](https://docs.python.org/3/library/os.html)

[geopandas](https://geopandas.org/)

[shapely](https://pypi.org/project/Shapely/)

[reduce](https://docs.python.org/3/library/functools.html)

[operator](https://docs.python.org/3/library/operator.html)

[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)

[re](https://docs.python.org/3/library/re.html)