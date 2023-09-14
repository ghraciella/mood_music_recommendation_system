import pickle
import numpy as np


# dump dataframe here:
with open('df2.bin', 'rb') as f:
    df2 = pickle.load(f)

def get_results(model, genre: str, mood: str): 
# Random choice
    moosic_randomN_idx = np.random.choice(
                                df2.index,
                                size = 5, #playlist_length,
                                replace= False #random n = 5
                                )
    # Filter
    recommended_moosic_playlist = df2[['track_id', 'track_name', 'artist_name']].iloc[moosic_randomN_idx]

    # return recommended_moosic_playlist
    print(recommended_moosic_playlist)

