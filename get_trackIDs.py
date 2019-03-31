import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import timeit


def byYear(year):
    client_credentials_manager = SpotifyClientCredentials("3fa87ccb238d49b7a2ae565655f70b3b", "de18a565c67746a597f68068e50a5104")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # timeit library to measure the time needed to run this code
    start = timeit.default_timer()

    #create empty lists where the results are going to be stored
    artist_name = []
    track_name = []
    popularity = []
    track_id = []

    #Spotify limits the results to 10,000. Thus this for loop grabs the artist name, track name, popularity and track_id for songs from year 2018
    #My thought was to create 3 data sets 2018, 2017 and 2016 then merge them together for a grand total of 30,000 songs.
    for i in range(0,10000,50):
        track_results = sp.search(q='year:'+str(year), type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

    print(type(track_results))
    print(track_results)
    stop = timeit.default_timer()
    print ('Time to run this code (in seconds):', stop - start)

    #confirms that the length of the track_id list is indeed 10,000
    print('number of elements in track_id:', len(track_id))

    #using Pandas we will load the data frame for the 10,000 songs from 2018
    df = pd.DataFrame({'artist_name': artist_name, 'track_name': track_name, 'track_id': track_id, 'popularity': popularity})

    #Confirms if our data frame is a 10,000 X 4 Matrix
    print(df.shape)
    df.info()

    return df

if __name__=='__main__':
    resp = input('Do you want data for a range of years? Enter y or n \n >')
    if resp == y:
    # do it for a year.
    else:
        year =  input('Enter year to get data \n >')
        df = byYear(year)
   
    #export data   
    file_name = input('Enter file name to save data, inlude extension as well. (eg. data.pkl) \n >')
    df.to_pickle(file_name)
