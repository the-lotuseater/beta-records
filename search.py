import spotipy as sp; import sys; import pprint;import spotipy.oauth2 as oauth2

def search_track(str):
    credentials = oauth2.SpotifyClientCredentials(
    client_id='3fa87ccb238d49b7a2ae565655f70b3b',
    client_secret='de18a565c67746a597f68068e50a5104')
    token = credentials.get_access_token()
    spotify = sp.Spotify(auth=token)
    return sp.search(str)


if __name__=='__main__':
    result = search_track('Billie Jean') 
    pprint.pprint(result._get_uri(result._get_id()))
