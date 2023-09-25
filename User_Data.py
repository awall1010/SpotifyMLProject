import api_helper
import pandas as pd
import os

class User_Data():
    def __init__(self):
        self.user_id = ""
        self.helper = api_helper.api_helper()

    def setHeaders(self, clientID, clientSecret):
        authToken = self.helper.getToken(clientID,clientSecret)
        self.helper.setToken(authToken)
        self.helper.setHeaders()

        if self.helper.testToken():
            return True
        else:
            return False

    def setUser(self, user):
        self.user_id = user

    def getUserData(self):
        playlists = self.helper.getAllUsersPlaylists(self.user_id)
        df = None
        playlist_num = 0
        for playlist in playlists:
            playlist_num += 1
            print("Playlist", ": ", playlist_num)
            data = self.helper.getPlaylistAttributes(playlist)
            df = pd.concat([df,data])
        df.columns = ['playlist_id',"track_id",'danceability',"energy","speechiness","acousticness","instrumentalness","liveness","valence","tempo"]
        return df

    def choosePlaylist(self):
        playlist = self.helper.printUserPlaylist(self.user_id)
        df = self.helper.getPlaylistAttributes(playlist)
        df.columns = ['playlist_id',"track_id",'danceability',"energy","speechiness","acousticness","instrumentalness","liveness","valence","tempo"]

        csv_name = "csv/"+playlist+".csv"
        os.makedirs('csv', exist_ok=True)
        df.to_csv(csv_name)
