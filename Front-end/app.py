import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase connection
cred = credentials.Certificate('path/to/your/firebase-key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Streamlit webpage layout
st.title('FarmBeats Project Dashboard')

# Function to fetch data from Firebase
def get_data():
    photos = db.collection('photos').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()
    distances = db.collection('distances').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1).stream()
    
    latest_photo = next(photos).to_dict()
    latest_distance = next(distances).to_dict()
    
    return latest_photo, latest_distance

photo, distance = get_data()

# Display the latest photo and distance
st.image(photo['url'], caption='Latest Photo')
st.write('Latest Distance:', distance['value'], 'meters')

# Update the data every 10 seconds
st.button('Refresh Data')
