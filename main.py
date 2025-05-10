import streamlit as st
import pandas as pd
import pickle
import base64

# Load model
model = pickle.load(open('RidgeModel.pkl', 'rb'))

# List of valid locations
locations = [
    '1st Block Jayanagar', '1st Phase JP Nagar', '2nd Phase Judicial Layout', '2nd Stage Nagarbhavi',
    '5th Block Hbr Layout', '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar',
    '8th Phase JP Nagar', '9th Phase JP Nagar', 'AECS Layout', 'Abbigere', 'Akshaya Nagar', 'Ambalipura',
    'Ambedkar Nagar', 'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal', 'Anjanapura', 'Ardendale',
    'Arekere', 'Attibele', 'BEML Layout', 'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar',
    'Balagere', 'Banashankari', 'Banashankari Stage II', 'Banashankari Stage III', 'Banashankari Stage V',
    'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout', 'Bannerghatta', 'Bannerghatta Road',
    'Basavangudi', 'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road', 'Bellandur', 'Benson Town',
    'Bharathi Nagar', 'Bhoganhalli', 'Billekahalli', 'Binny Pete', 'Bisuvanahalli', 'Bommanahalli',
    'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli', 'Brookefield', 'Budigere',
    'CV Raman Nagar', 'Chamrajpet', 'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar',
    'Chikkalasandra', 'Choodasandra', 'Cooke Town', 'Cox Town', 'Cunningham Road', 'Dasanapura',
    'Dasarahalli', 'Devanahalli', 'Devarachikkanahalli', 'Dodda Nekkundi', 'Doddaballapur',
    'Doddakallasandra', 'Doddathoguru', 'Domlur', 'Dommasandra', 'EPIP Zone', 'Electronic City',
    'Electronic City Phase II', 'Electronics City Phase 1', 'Frazer Town', 'GM Palaya',
    'Garudachar Palya', 'Giri Nagar', 'Ulsoor', 'Uttarahalli', 'Varthur', 'Varthur Road', 'Vasanthapura',
    'Vidyaranyapura', 'Vijayanagar', 'Vishveshwarya Layout', 'Vishwapriya Layout', 'Vittasandra',
    'Whitefield', 'Yelachenahalli', 'Yelahanka', 'Yelahanka New Town', 'Yelenahalli', 'Yeshwanthpur',
    'other'
]

# Add background image
def add_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Arial', sans-serif;
            color: #111;
        }}
        .stButton>button {{
            background-color: rgba(255,255,255,0.9);
            color: #1a1a1a;
            font-size: 1.2em;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px 25px;
            transition: 0.3s ease;
        }}
        .stButton>button:hover {{
            background-color: #ffc107;
            color: #000;
            transform: scale(1.05);
        }}
        .stTextInput>div>input, .stNumberInput>div>input {{
            background-color: rgba(255,255,255,0.85);
        }}
        </style>
    """, unsafe_allow_html=True)

# Set background
add_bg_from_local("background.jpg")

# Title
st.title("🏠 Bangalore House Price Predictor")

# Inputs
location = st.selectbox("📍 Select Location", sorted(locations))
total_sqft = st.number_input("📏 Total Square Feet", min_value=300.0, step=10.0)
bath = st.slider("🛁 Number of Bathrooms", 1,10,2)
bhk = st.slider("🛏️ Number of Bedrooms (BHK)", 1,10,2)

# Predict
if st.button("🔮 Predict Price"):
    try:
        # 👇 Convert input to proper DataFrame
        input_data = pd.DataFrame({
            'location': [location],
            'total_sqft': [float(total_sqft)],
            'bath': [int(bath)],
            'bhk': [int(bhk)]
        })

        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Price: ₹ {round(prediction, 2)} Lakhs")

    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction.\n\n{e}")
