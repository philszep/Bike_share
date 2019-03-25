import pandas as pd
import numpy as np

def bike_clean_df(df, subs_only = True):
    """Cleans bikeshare dataframe. 
    Removes NaN
    Filter out non-subscribers
    Drops trips longer than two hours
    Converts station ids to ints
    Converts datetime strings to datetime objects
    """
    #Drop NaN values
    df.dropna(inplace=True)
    
    #Restrict to subscribers    
    if subs_only:
        clean_df = df[df['usertype'] == 'Subscriber'].copy() # Careful with copy when DF contains mutable objects like lists....
        clean_df.drop
    
    #Drop trips longer than two hours
    clean_df = clean_df[clean_df['tripduration'] < 7200]

    #Convert station ids to integers
    clean_df['start station id']=clean_df['start station id'].astype(int)
    clean_df['end station id']=clean_df['end station id'].astype(int)

    #Convert to datetime
    clean_df['starttime'] = pd.to_datetime(clean_df['starttime'])
    clean_df['stoptime'] = pd.to_datetime(clean_df['stoptime'])

    return clean_df
    

def get_trip_info(df):
    """Extracts some relevant data from trips
    Drops cols: ['start station name', 'start station latitude', 'start station longitude', 'end station name', 'end station latitude', 'end station longitude']
    Adds cols: ['start_day', 'stop_day','pickup_hour','dropoff_hour', 'age', Trip_Type','start_end_station']
    """
    trip_info_df = df.copy()
 
    trip_info_df.drop(columns = ['start station name', 'start station latitude', 'start station longitude', 'end station name', 'end station latitude', 'end station longitude'],inplace=True)

    
    #Get weekday labels and create column
    trip_info_df['start_day'] = trip_info_df['starttime'].map(lambda x: x.weekday()) # 0 = Monday, .. , 6 = Sunday
    trip_info_df['stop_day'] = trip_info_df['stoptime'].map(lambda x: x.weekday()) # 0 = Monday, .. , 6 = Sunday

    #Get hours and create column
    trip_info_df['pickup_hour'] = trip_info_df['starttime'].map(lambda x: x.hour) # 0 .. 24
    trip_info_df['dropoff_hour'] = trip_info_df['stoptime'].map(lambda x: x.hour) # 0 .. 24

    #Get age
    trip_info_df['age'] = 2018 - trip_info_df['birth year']


    #Assign different times to types of trip 
    #Weekend = [Sat,Sun], 'Late Night' = before 6am or after 8pm, 'Commuter' = 6-10am or 4-8pm, 'Daytime Errand' = 10am-4pm)
    trip_info_df = trip_info_df.assign(Trip_Type =
    np.select(
        condlist=[trip_info_df['start_day'] == 5, trip_info_df['start_day']==6, trip_info_df['pickup_hour'] < 6, trip_info_df['pickup_hour'] <10, trip_info_df['pickup_hour'] < 16, trip_info_df['pickup_hour']<20, trip_info_df['pickup_hour'] < 24], 
        choicelist=['Weekend','Weekend','Late Night','Commuter','Daytime Errand','Commuter','Late Night'], 
        default='Other'))

    #Create column of start-end station pairs
    trip_info_df = trip_info_df.assign( start_end_station = tuple(zip(trip_info_df.loc[:,'start station id'], trip_info_df.loc[:,'end station id'])))

    # Remove ordering (forget which station is start/end)
    #start_end = subs_df['start_end_station'].copy()
    trip_info_df['start_end_station'] = trip_info_df['start_end_station'].map(lambda x: tuple(sorted(x)))


    return trip_info_df



def get_stations_info(df, city = 'NYC'):
    """ Create station info dataframe from bike share dataframe.
        df: bikeshare dataframe
        Return: dataframe with index = 'station_id' and columns = ['station_name', 'lon','lat']
    """
    if city == 'NYC':
        stations_info_df = df[['start station id','start station latitude', 'start station longitude','start station name']].set_index('start station id')
        stations_info_df = stations_info_df.drop_duplicates()
        stations_info_df.rename({'start station name': 'station name','start station longitude': 'lon', 'start station latitude': 'lat'},axis=1,inplace=True)

        #Remove stations outside of NYC 
        drops=stations_info_df[stations_info_df['lat']>45].index
        stations_info_df.drop(drops,inplace=True)

    return stations_info_df

# Below is another way of creating the stations_info_df, there were issues here because only 
# currently active stations are included in station_information.json and this does not include 
# those on Governors Island 

# Build the NYC station info df (with lat, long, name, capacity)
# This station file seems to be missing at least one station (id = 3254) figure this out later, for now us stations_info_df 
# Extracted from the data itself...
#stations_file = open('./data/NYC/station_information.json','r')
#stations = stations_file.read()
#stations_file.close()

#stations_json = json.loads(stations)
#stations_json_list = stations_json['data']['stations']
#stations_json_list = stations_json['stationBeanList']


#stations_info_df = pd.DataFrame(stations_json_list)
#stations_info_df.drop(['has_kiosk','region_id','rental_methods','rental_url','short_name','eightd_has_key_dispenser','eightd_station_services','electric_bike_surcharge_waiver','external_id'],axis = 1,inplace=True)
#stations_info_df['station_id'] = stations_info_df['station_id'].astype('int')
#stations_info_df[stations_info_df['name'] == ' Soissons Landing']

#stations_info_df.set_index('station_id',inplace=True)
#stations_info_df[stations_info_df['station_id']==3264]
#stations_info_df.drop(['city','is_renting', 'availableDocks','availableBikes','altitude','landMark','lastCommunicationTime','postalCode','location','stAddress2','status','statusValue','statusKey','testStation','stAddress1','kioskType'],axis = 1,inplace=True)   
#stations_info_df.set_index('id',inplace=True)
#stations_info_df


def get_hourly_pickups(df, weekday_only = False, weekend_only = False):
    """ Create dataframe of number of pick_ups per station per hour
    """
    #Create weekday and weekend dataframes
    if weekday_only == True:
        pickup_df = df[df['Trip_Type'] != 'Weekend'].copy()
    elif weekend_only == True:
        pickup_df = df[df['Trip_Type'] == 'Weekend'].copy()
    else:
        pickup_df  = df.copy()


    return pickup_df