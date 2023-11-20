# MOOSIC Web Application - work in progress

# Project Description

MOOSIC is a music recommendation engine based on the mood of the user. After selecting Genre/Artists and Mood the User will get a top ten tracks recommendation. 


For our model we used a combination of TNSE and KNN. To train our model we decided on the [Spotify Dataset 600k Tracks](https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks) (open source). We liked this Dataset, because it had the features genre, valence, liveliness, acousticness and speechiness, which helped in feature engineering the mood filter. This mood filter makes our model unique. 
  

# Setup

1. Clone the repo and go in it.
1. Run these commands in your terminal:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


# How to Use MOOSIC Web App
Run main.py and copy URL with the port into your browser bar. 
You should now see the page. 


# Include Credits

### Organization

* Neuefische GmbH [Link](https://github.com/neuefische/)

### __Team Credits__: __Rhythm Byte Engineers__

* Christian [Link](https://github.com/ChrisHabe)
* Shahi [Link](https://github.com/ShahiW)
* Grace [Link](https://ghraciella.github.io/)

<br>

# choose a license