import api_helper
import pandas as pd
import time

class data_trainer():
    def __init__(self):
        self.helper = api_helper.api_helper()
        self.clientId = "7aab6148c26545039fcbadd0fbf18f41"
        self.clientSecret = "f4ecf1ce33ea4d118bf14ca5b1ca153f"

    def setHeaders(self, clientID, clientSecret):
        authToken = self.helper.getToken(clientID,clientSecret)
        self.helper.setToken(authToken)
        self.helper.setHeaders()

        if self.helper.testToken():
            return True
        else:
            return False

    def setHeaders(self, clientID, clientSecret):
        authToken = self.helper.getToken(clientID,clientSecret)
        self.helper.setToken(authToken)
        self.helper.setHeaders()

        if self.helper.testToken():
            return True
        else:
            return False

    def getSpotifyPlaylists(self):
       playlists = self.helper.getAllUsersPlaylists("Spotify")
       #playlists = self.helper.getlUsersPlaylists("Spotify", 27, 2)

       data = pd.DataFrame()
       num = 0
       for playlist in playlists:
           num += 1
           print("Playlist ", num, ": ",playlist[1], end = "| ")
           time_start = time.perf_counter()
           #Remove "This is" playlists and adds others to database
           if "this is" not in playlist[1]:
               try:
                   tracks = self.helper.getPlaylistTracks(playlist[0])
                   df = self.getPlaylistAttributes(tracks, playlist[0])
                   data = pd.concat([data, df])
               except Exception as e:
                   print(e, end = "| ")
                   pass

           time_stop = time.perf_counter()
           print(round(time_stop - time_start, 2))
       return data

    def getPlaylistAttributes(self, tracks, playlist_id):
        return self.helper.getPlaylistAttributes(tracks, playlist_id)
        # for track in tracks:
        #     attributes = self.getTrackAttributes(track[0])
        #     attributes.insert(0,playlist_id)
        #     self.data.append(attributes)
