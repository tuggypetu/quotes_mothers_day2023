import requests
import json
import streamlit as st

# Define the API endpoint and parameters
url = 'https://api.forismatic.com/api/1.0/'
params = {
    'method': 'getQuote',
    'format': 'json',
    'lang': 'en',
    'key': 1  # An API key is not required for this API
}

# Define the Streamlit app layout
st.set_page_config(page_title="Mother's Day Quotes", page_icon=":family:", layout="wide")
st.write("14-05-2023")
st.title("Mother's Day Quotes 👩")
st.subheader("happy mother's day Mama!\nCelebrate your mother with these inspiring quotes")

if st.button("Get new quote"):
    # Call the API and display the quote
    response = requests.get(url, params=params)
    if response.status_code == 200:
        # data = response.json()
        try:
            data = json.loads(response.text)
            print(data)
            st.write("")
            st.write(f"<p style='font-size:20px;'><i>{data['quoteText']}</i></p>", unsafe_allow_html=True)
            st.write(f"by - {data['quoteAuthor']}" if data['quoteAuthor'] else "by - Unknown")
            st.balloons()
        except:
            st.write("Error retrieving quote. Please try again later.")
    else:
        st.write("Error retrieving quote. Please try again later.")
