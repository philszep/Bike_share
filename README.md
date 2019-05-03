# Bike_share

This is a project that I am working on that analyzes bike share data for the city of New York, and in the future other similar large scale bike share systems. 

This is motivated by bike culture in the Netherlands, where biking is central to local transportation. The goal here is to develop insights and tools that can help make biking in the US _easy, efficient and safe._ 

The tools are intended to be useful to several audiences. The overarching goals for various audiences are:

* Individual bikers: How can we make biking more convenient and safe for individuals? 
* City planners: What insights and tools can we provide for cities in order for them to best focus resources into making biking an efficient and safe method of transportation within the city?
* Bike share operators: How best to optimize bike share systems in order to facilitate easy and efficient use of bikes for as many people as possible?


**Contents:** 

Notebooks: 

* `Summer_2018.ipynb` : Exploratory trip analysis with Summer (June, July, August) 2018 data.  
* `Winter_2018.ipynb`: Exploratory trip analysis with Winter (January, February, March) 2018 data.   
* `StationGIFs_NYC_Winter2018.ipynb`: Sample notebook for creating station usage GIFs in `./Images/` 

* `./Notebooks/clustering`: Folder containing several notebooks that cluster stations into different usage categories. 

    * `Summer_2018_weekday_clustering.ipynb`: K-means clustering on stations using data from the Summer 2018 dataset -- clumps stations into high/low use stations and morning/evening pickup stations, relevant for commuters  
    * `Summer_2018_weekend_clustering.ipynb`: K-means clustering on stations using data from the Summer 2018 dataset -- clumps stations into high/low use stations and daytime/evening pickup stations, likely relevant for recreational bikers  
    * `Winter_2018_weekday_clustering.ipynb`: same as summer notebook but for winter dataset 
    * `Winter_2018_weekday_clustering.ipynb`: same as summer notebook but for winter dataset 

* `./Notebooks/networkanalysis`: folder containing several notebooks that use networkx library to analyze aspects of the bikeshare system from the perspective of network theory. Used to create maps with top trips in `./Images`, see for example `Winter_2018_WD_trips.gif`.
    

* `top_trips_Chicago_Q4.ipynb`: Preliminary work on plotting commons trips for data from Chicago

To do: 

* Use clustering data as classification of stations (as in `Summer_2018_weekday_clustering.ipynb`, for example), combined with station feature data to create a classifier for "bikeable" neighborhoods. (Work in progress...) 
* Next step: _accummulate feature data_ 




This currently utilizes tools from the following sources:

* Tilemapbase - https://github.com/MatthewDaws/TileMapBase  
* OpenStreetMap Data is "© OpenStreetMap contributors”, see http://www.openstreetmap.org/copyright  
* mplleaflet - https://github.com/jwass/mplleaflet  
* NYC citibike data - https://www.citibikenyc.com/system-data
* Chicago Divvy bike share data - https://www.divvybikes.com/system-data

