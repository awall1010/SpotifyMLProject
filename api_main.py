import data_trainer as trainer
import api_helper as api
import User_Data

clientID =  "7aab6148c26545039fcbadd0fbf18f41"
clientSecret = "f4ecf1ce33ea4d118bf14ca5b1ca153f"

#Training spotify data
# trainer = trainer.data_trainer()
# trainer.setHeaders(clientID, clientSecret)
# trainer.getSpotifyPlaylists()
# df = trainer.getSpotifyPlaylists()
# df.info()
# df.to_csv("Spotify_tracks.csv")

#Get user playlist data
print()
username =input("Enter your username: ")
user = User_Data.User_Data()
user.setHeaders(clientID, clientSecret)
user.setUser(username)
user.choosePlaylist()
