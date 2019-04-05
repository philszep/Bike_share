# Bike_share

This is a project that I am working on that analyzes bike share data for the city of New York, and in the future other similar large scale bike share systems. 

The goal is to develop tools that will be hopefully provide insights into the overall usage of the bike share system as well as the quality of cycling infrastructure within the city. It may also be interesting for people interested in buying a bikeshare subscription or wanting to incorporate more biking into their daily lives.

**Contents:** 

Notebooks: 

* `Summer_2018.ipynb` : Exploratory trip analysis with Summer (June, July, August) 2018 data.  
* `Winter_2018.ipynb`: Exploratory trip analysis with Winter (January, February, March) 2018 data.   
* `StationGIFs_NYC_Winter2018.ipynb`: Sample notebook for creating station usage GIFs in './Images/' 

* `Summer_2018_weekday_clustering.ipynb`: K-means clustering on stations using data from the Summer 2018 dataset -- clumps stations into high/low use stations and morning/evening pickup stations, relevant for commuters  
* 'Summer_2018_weekend_clustering.ipynb': K-means clustering on stations using data from the Summer 2018 dataset -- clumps stations into high/low use stations and daytime/evening pickup stations, likely relevant for recreational bikers  
* 'Winter_2018_weekday_clustering.ipynb': K-means clustering on stations using data from the Winter 2018 dataset -- similar to summer results  
* 'Winter_2018_weekday_clustering.ipynb': K-means clustering on stations using data from the Winter 2018 dataset -- similar to summer results  

* 'top_trips_Chicago_Q4.ipynb': Preliminary work on plotting commons trips for data from Chicago
* 'Clustering_exploration.ipynb': exploratory clustering on individual trips
* 'Winter_2018_station_types.ipynb' and 'Winter_2018_trip_types.ipynb': some crude attempts at classifying stations and trips

To do: 

* Use clustering data as classification of stations (as in 'Summer_2018_weekday_clustering.ipynb', for example), combined with station feature data to create a classifier for 'bikeable' neighborhoods. (Work in progress...) 
* Next step: _accummulate feature data_




This currently utilizes tools from the following sources:

Tilemapbase - https://github.com/MatthewDaws/TileMapBase  
OpenStreetMap Data is "© OpenStreetMap contributors”, see http://www.openstreetmap.org/copyright  
mplleaflet - https://github.com/jwass/mplleaflet  

