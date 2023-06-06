import streamlit as st
import pickle
# from sklearn.feature_extraction.text import CountVectorizer

st.write('''
# Tweet Classifier
 This app is used to categorised **tweet**
''')
         

categories = {
        0: "Arts & Culture",
        1: "Business & Entrepreneurs",
        2: "Pop Culture",
        3: "Daily Life",
        4: "Sports & Gaming",
        5: "Science & Technology"
    }

# Load the trained model from a pickle file
with open("best_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the classifier function
def classify_tweet(tweet):
    # Prediction
    prediction = model.predict([tweet])
    
    # Return the prediction result as a JSON object
    return categories[prediction[0]]


tweet = st.text_area('Please Enter your tweet here for classification:')

if st.button('Classify ! '):

    result = classify_tweet(tweet)

    st.write(f'This tweet can be classified as *{result}*')
