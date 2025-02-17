# import library
import streamlit as st
import numpy as np
import pandas as pd
import pickle

#Judul Utama
st.title('Travel Insurance Predictor')
st.text('This web can be used to predict your status claim of policyholder')



# Menambahkan sidebar
st.sidebar.header("Please input your features")

def create_user_input():
    # Numerical Features
    duration = st.sidebar.slider('Duration', min_value=0, max_value=547, value=50)
    net_sales = st.sidebar.number_input('Net Sales', min_value=-357.5, max_value=666.0, value=42.0)
    commission = st.sidebar.number_input('Commision (in value)', min_value=0.0, max_value=262.76, value=10.23)
    age = st.sidebar.slider('Age', min_value=18, max_value=88, value=38)
    
    # Categorical Features
    agency = st.sidebar.selectbox('Agency', ['RAB', 'JZI', 'C2B', 'LWC', 'EPX', 'CWT', 'KML', 'TST', 'CCR', 'SSI', 'CBH', 'ART', 'TTW', 'ADM', 'CSR'])
    agency_type = st.sidebar.radio('Agency Type', ['Airlines', 'Travel Agency'])
    distribution_channel = st.sidebar.radio('Distribution Channel', ['Online', 'Offline'])
    
    product_name = st.sidebar.selectbox('Product Name', [
        'Value Plan', 'Annual Gold Plan', 'Single Trip Travel Protect Gold', 'Cancellation Plan',
        'Bronze Plan', '1 way Comprehensive Plan', 'Single Trip Travel Protect Platinum', 'Basic Plan',
        '2 way Comprehensive Plan', 'Rental Vehicle Excess Insurance', 'Silver Plan', 'Annual Silver Plan',
        'Travel Cruise Protect', 'Single Trip Travel Protect Silver', 'Gold Plan', 'Comprehensive Plan',
        'Ticket Protector', 'Annual Travel Protect Gold', 'Child Comprehensive Plan', 'Premier Plan',
        'Annual Travel Protect Silver', 'Individual Comprehensive Plan', 'Spouse or Parents Comprehensive Plan',
        'Annual Travel Protect Platinum', '24 Protect', 'Travel Cruise Protect Family'
    ])
    
    destination = st.sidebar.selectbox('Destination', [
        'BRUNEI DARUSSALAM', 'KOREA REPUBLIC OF', 'SINGAPORE', 'UNITED KINGDOM', 'CHINA', 'INDIA', 'THAILAND',
        'PHILIPPINES', 'SPAIN', 'HONG KONG', 'MALAYSIA', 'AUSTRALIA', 'IRELAND', 'UNITED STATES', 'MYANMAR',
        'FRANCE', 'INDONESIA', 'CAMBODIA', 'NEW ZEALAND', 'TAIWAN PROVINCE OF CHINA', 'JAPAN', 'GERMANY',
        'SOUTH AFRICA', 'NORWAY', 'ITALY', 'AUSTRIA', 'UNITED ARAB EMIRATES', 'SWITZERLAND', 'BRAZIL',
        "LAO PEOPLE'S DEMOCRATIC REPUBLIC", 'NEPAL', 'CANADA', 'VIET NAM', 'BANGLADESH', 'SAUDI ARABIA',
        'JORDAN', 'MACAO', 'PORTUGAL', 'SWEDEN', 'DENMARK', 'PAKISTAN', 'MALTA', 'ISRAEL', 'GREECE', 'COLOMBIA',
        'MACEDONIA THE FORMER YUGOSLAV REPUBLIC OF', 'PERU', 'AZERBAIJAN', 'BELGIUM', 'OMAN', 'BAHRAIN', 'KENYA',
        'SRI LANKA', 'BENIN', 'NETHERLANDS', 'CROATIA', 'ICELAND', 'GUINEA', 'SLOVENIA', 'CZECH REPUBLIC',
        'PAPUA NEW GUINEA', 'PANAMA', 'TURKEY', 'BHUTAN', 'FRENCH POLYNESIA', 'HUNGARY', 'TUNISIA', 'FINLAND',
        'VANUATU', 'GHANA', 'MONGOLIA', 'MAURITIUS', 'MEXICO', 'QATAR', 'RUSSIAN FEDERATION', 'COSTA RICA',
        'VENEZUELA', 'MALDIVES', 'KUWAIT', 'UZBEKISTAN', 'MOROCCO', 'POLAND', 'GEORGIA', 'TANZANIA UNITED REPUBLIC OF',
        'BERMUDA', 'KYRGYZSTAN', 'ECUADOR', 'UKRAINE', 'ARGENTINA', 'EGYPT', 'ETHIOPIA', 'BELARUS', 'UGANDA', 'FIJI',
        'ROMANIA', 'ZAMBIA', 'GUADELOUPE', 'CYPRUS', 'KAZAKHSTAN', 'ANGOLA', 'BULGARIA', 'FAROE ISLANDS', 'TAJIKISTAN',
        'CHILE', 'LATVIA', 'GUAM', 'NORTHERN MARIANA ISLANDS', 'BOLIVIA', 'ZIMBABWE', 'CAMEROON', 'TURKMENISTAN',
        'LEBANON', 'ESTONIA', 'LITHUANIA', 'SERBIA', 'ARMENIA', 'LUXEMBOURG', 'TRINIDAD AND TOBAGO', 'NAMIBIA', 'GUYANA',
        'JAMAICA', 'REPUBLIC OF MONTENEGRO', 'SENEGAL', 'PUERTO RICO', 'CAYMAN ISLANDS', 'IRAN ISLAMIC REPUBLIC OF',
        'URUGUAY', 'NIGERIA', 'BOTSWANA', 'MALI', 'MOLDOVA REPUBLIC OF', 'SAMOA'
    ])
    
    # Creating a dictionary with user input
    user_data = {
        'Duration': duration,
        'Net Sales': net_sales,
        'Commision (in value)': commission,
        'Age': age,
        'Agency': agency,
        'Agency Type': agency_type,
        'Distribution Channel': distribution_channel,
        'Product Name': product_name,
        'Destination': destination
    }
    
    # Convert the dictionary into a pandas DataFrame (for a single row)
    user_data_df = pd.DataFrame([user_data])
    
    return user_data_df

# Get customer data
data_customer = create_user_input()

# Membuat 2 kontainer
col1, col2 = st.columns(2)

# Kiri
with col1:
    st.subheader("Customer's Features")
    st.write(data_customer.transpose())

# Load model
with open(r'travel-insurance-model.sav', 'rb') as f:
    model_loaded = pickle.load(f)
    
# Predict to data
kelas = model_loaded.predict(data_customer)
probability = model_loaded.predict_proba(data_customer)[0]  # Get the probabilities

# Menampilkan hasil prediksi

# Bagian kanan (col2)
with col2:
    st.subheader('Prediction Result')
    if kelas == 1:
        st.write('Class 1: This customer will Claim')
    else:
        st.write('Class 2: This customer will Not Claim')
    
    # Displaying the probability of the customer buying
    st.write(f"Probability of Claim: {probability[1]:.2f}")  # Probability of class 1 (BUY)
