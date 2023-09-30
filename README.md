# SpotifyMLProject
This is a program that generates song attributes that we believe a user will like so they can find suggested songs at the end of playlists. It uses a LSTM, 
and the training data is all of Spotify's public playlist, gathered by connecting to Spotify's developer API. It then allows a user to connect to Spotify API, 
and by typing in their username, can find all of their public playlists and allow our LSTM model to predict other songs that would fit for the playlist. 
Here is a demo of how our product works: https://www.youtube.com/watch?v=Lcc3ULKgoCQ.

Spotify Attribute Generation
Noah Masur, Ali Woodward, Aidan Wall

Included files
   Code:
 	api_helper.py - Tools to get data from Spotify api
	User_data.py - Get a specific users Spotify playlist data
	data_trainer.py - Get Spotify's playlist data
	api_main.py - Implementation of the various api calls
	BasicModel.ipynb - LSTM model
   Data:
	Spotify_tracks.csv - Spotify playlist training data
	Noahmasur_tracks.csv - Example user data used for predictions
   Write-ups:
	Machine Learning Spotify Final.pdf - Final presentation
	FinalPresentation.mp4 - Video of presentation
	CPSC 393- Final Paper.docx - Final Paper

Resources
https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/
https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
https://www.youtube.com/watch?v=tepxdcepTbY
https://github.com/bnsreenu/python_for_microscopists/blob/master/181_multivariate_timeseries_LSTM_GE.py
https://github.com/yhegab/spotify_reccomendation_app
