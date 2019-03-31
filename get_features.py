from __future__ import print_function    # (at top of module)
from spotipy.oauth2 import SpotifyClientCredentials; import spotipy ; import time; import sys; import pandas as pd;import json
from pandas.io.json import json_normalize as normalize

def get_features(path_name):
    """ Method to find the audio features of songs saved in a dataframe.
        Parameter: A pandas DataFrame consisting of track ids
        Output : A pandas DataFrame consisting of all the audio features for songs in the data frame, and a list consisting of indices for corrupted values.
    """

    client_credentials_manager = SpotifyClientCredentials(client_id ="3fa87ccb238d49b7a2ae565655f70b3b", client_secret ="de18a565c67746a597f68068e50a5104")
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace=False

    #load dataframe into 
    print("Loading pickle file into a dataframe....")
    df = pd.read_pickle(path_name)
    print("Done") 

    # Request the audio features for the chosen tracks (limited to 50)
    ids= df['track_id']
    dumps = [];cindices=[]  #lists to save dictionaries and indices of corrupted values.
 
    print("Creating a Data Frame consisting of features. This can take a few minutes....")

    #group values 50 at a time.
    for i in range (int(len(ids)/50)):
        dumps = sp.audio_features(ids[i*50:50*(i+1)]) 
        if i==0:
            features_df = pd.DataFrame([], columns = dumps[0].keys())
        for j in range (len(dumps)):
            try:
                features_df.loc[j+50*i] = list(dumps[j].values())
            except:
#                print(j+50*i)     uncomment the print statement to print corruped data fields.
                cindices.append(j+50*i)
                continue                
    print("Success!") 
    return features_df, cindices
 
if __name__=='__main__':
    logic = True
    while logic:
        try:
            path_name = input('Enter name of Pickled DataFrame to load.\n>')
            df, cindices = get_features(path_name)
            resp = input('Enter \'e\' to export the data or \'p\' to print it \n >')
            if resp == 'p':
                print(df)
            if resp == 'e':
                file_name = input('Please enter your desired file name to export the data \n >')
                ext = input('Enter desired export type. Enter csv or pkl \n >')
                if ext == 'csv':
                    df.to_csv(file_name+'.'+ext)
                elif ext == 'pkl':
                    df.to_pickle(file_name+'.'+ext)
                print("Finished exporting!")
            logic = False
        #exept statement to check for errors and start from beginning if there's an error.
        except:
            continue    
"""
    need to complete the merging code...
    if len(cindices)!=0:
        print("Dropping corrupted data fields...")
        df2 = pd.read_pickle(path_name)  
        input_df = df2.drop(cindices)
    else:
        input_df = pd.read_pickle(pathname)
    resp = input('Want to merge DataFrame? Enter y or no... >')
    if resp == 'y':
        input_df 
"""
