
import spotipy
from credentials import client_ID, client_SECRET
from spotipy.oauth2 import SpotifyClientCredentials

# connects to Spotify API client using Spotipy library

credentials = SpotifyClientCredentials(client_id=client_ID, client_secret=client_SECRET)
sp = spotipy.Spotify(client_credentials_manager=credentials)

def run():
    again = True
    while again:
        title = input("Enter the title of a song: ")
        artist = input("Enter the artist the song is by: ")

        results = sp.search(q='artist:' + artist + ', track:' + title, limit = 15, type="track") # finds the possible songs that match the user input from the Spotify library
        
        if results['tracks']['total'] == 0:
            print("No results found. Please make sure the song title and artist are correct. Please try again.\n")
        else:
            print(f"Here are some songs similar to {title} by {artist}:")
            song = results['tracks']['items'][0] # saves the data of the user inputted song 
            

            recommendations = sp.recommendations(seed_tracks=[song['uri']]) # extracts the uri of the user inputted song and uses it to fuel recommendations
            recDic = {}
            for num, track in enumerate(recommendations['tracks'], 1):
                print(f"{num}. {track['name']} - {track['artists'][0]['name']}")
              
                recDic[num] = [track['preview_url'], f"{track['name']} by {track['artists'][0]['name']}"] # saves the preview url and the title and artist of each song
            
            # UI menu vvv
            endAgain = True
            while endAgain:
                songNum = int(input("Enter the number of the song you'd like to preview (0 for no preview): "))
                if songNum < 0 or songNum > 20:
                    print("Please enter a valid number.")
                elif songNum == 0:
                    endAgain = False
                else:
                    if recDic[songNum][0] == None:
                        print(f"There is no preview available for {recDic[songNum][1]}")
                    else:
                        print(f"Here is the preview link of {recDic[songNum][1]}: {recDic[songNum][0]}")
                

            endAgain = True
            while endAgain:
                qAgain = input("Would you like to get recommendations for another song? (y/n)\n")
                if qAgain == "y" or qAgain == "Y":
                    endAgain = False
                elif qAgain != "n" and qAgain != "N":
                    print("Please enter either \"y\" for yes or \"n\" for no")
                else:
                    endAgain = False
                    again = False
             

run()
                    


            






    
