import spotipy
import requests
import pandas as pd

class api_helper():
    def __init__(self):
        authToken = ""
        headers = {}

    def getToken(self,clientID, clientSecret):
        from spotipy.oauth2 import SpotifyClientCredentials
        tokenRequester = SpotifyClientCredentials(client_id = clientID, client_secret = clientSecret)
        authToken = tokenRequester.get_access_token(as_dict = False, check_cache = True)
        return authToken

    def setToken(self,authToken):
            self.authToken = authToken

    def testToken(self):
        response = requests.get(f'https://api.spotify.com/v1/artists/2WoVwexZuODvclzULjPQtm', headers=self.headers)
        if str(response) == '<Response [200]>':
            return True
        elif str(response) == '<Response [401]>':
            return False
        else:
            print(f"{str(response)}")
            print("apihelper.testToken: Returning False")
            return False

    def setHeaders(self, authToken = "N/A"):
        if(authToken == "N/A"):
            self.headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.authToken}',
                }
        else:
            self.headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {authToken}',
                }

    def getTrackAttributes(self, trackID):
        prev_response = ""
        while True:
            response = requests.get(f'https://api.spotify.com/v1/audio-features/{trackID}', headers=self.headers)
            if str(response) == '<Response [200]>':
                break
            else:
                print(f"{str(response)}")
                print("...")
                if(prev_response == str(response)):
                    return str(response)
                else:
                    prev_response = str(response)


        results =  response.json()
        attrList = []
        attrList.append(results["id"])
        attrList.append(results["danceability"])
        attrList.append(results["energy"])
        attrList.append(results["speechiness"])
        attrList.append(results["acousticness"])
        attrList.append(results["instrumentalness"])
        attrList.append(results["liveness"])
        attrList.append(results["valence"])
        attrList.append(results["tempo"])

        return attrList

    def getUsersPlaylists(self, user_id, offset = 0, limit = 50):
        params = (
            ('market', 'US'),
            ('limit', limit),
            ('offset', str(offset))
            )

        prev_response = ""
        while True:
            response = requests.get(f'https://api.spotify.com/v1/users/{user_id}/playlists', headers=self.headers, params=params)

            if str(response) == '<Response [200]>':
                break
            else:
                print(f"{str(response)}")
                print("...")
                if(prev_response == str(response)):
                    return str(response)
                else:
                    prev_response = str(response)

        results = response.json()
        playlist_list = []

        for playlists in results["items"]:
            playlist_list.append([playlists["id"], playlists["name"].lower()])

        return playlist_list

    def getAllUsersPlaylists(self, user_id):
        playlist_list = []
        offset = 0
        response = []

        while True:
            response = self.getUsersPlaylists(user_id, offset)
            for playlist in response:
                playlist_list.append(playlist)

            if len(response) != 50:
                break
            else:
                offset += 50

        return playlist_list

    def getPlaylistTracks(self,playlist_id, offset = 0):
        prev_response = ""
        while True:
            response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',headers=self.headers)
            if str(response) == '<Response [200]>':
                break
            else:
                print(f"{str(response)}")
                print("...")
                if(prev_response == str(response)):
                    return str(response)
                else:
                    prev_response = str(response)
        results = response.json()

        trackList = []
        order = 1
        for track in results['items']:
            artist = track['track']['album']["artists"][0]['id']
            id = track["track"]['id']

            temp_track = [id,order, artist]
            trackList.append(temp_track)
            order += 1
        return trackList

    def getPlaylistAttributes(self, playlist_id, tracks = []):
        if len(tracks) == 0:
            tracks = self.getPlaylistTracks(playlist_id)
        data = []
        for track in tracks:
            attributes = self.getTrackAttributes(track[0])
            attributes.insert(0,playlist_id)
            data.append(attributes)
        df = pd.DataFrame.from_records(data)

        return df

    def printUserPlaylist(self, user_id, offset = 0, limit = 50):
            params = (
                ('market', 'US'),
                ('limit', limit),
                ('offset', str(offset))
                )

            prev_response = ""
            while True:
                response = requests.get(f'https://api.spotify.com/v1/users/{user_id}/playlists',headers=self.headers, params=params)

                if str(response) == '<Response [200]>':
                    break
                else:
                    print(f"{str(response)}")
                    print("...")
                    if(prev_response == str(response)):
                        return str(response)
                    else:
                        prev_response = str(response)

            results = response.json()
            playlist_list = []
            i = 0
            for playlists in results["items"]:
                playlist_list.append(playlists["id"])
                print(i," ",playlists['name'],": ",playlists['id'])
                i+=1

            features = playlist_list
            choices = {}
            for i in range(len(features)):
                choices[i] = features[i]
            index = self.get_choice(choices.keys())
            print(playlist_list[index])
            return playlist_list[index]

    def get_choice(self, lst):
        choice = input("Enter choice number: ")
        while choice.isdigit() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while int(choice) not in lst:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")
        return int(choice)
