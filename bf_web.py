# web_app.py
import streamlit as st
import pandas as pd
import pickle

# Load the best model
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Body Fat Percentage Prediction')

# User input for height, weight, age, hip size, waist size, and neck size
height = st.number_input('Enter Height (cm)', min_value=0.0, step=0.1)
neck_size = st.number_input('Enter Neck Size (cm)', min_value=0.0, step=0.1)
#weight = st.number_input('Enter Weight (kg)', min_value=0.0, step=0.1)
#age = st.number_input('Enter Age', min_value=0, step=1)
hip_size = st.number_input('Enter Hip Size (cm)', min_value=0.0, step=0.1)
waist_size = st.number_input('Enter Waist Size (cm)', min_value=0.0, step=0.1)
BMI = st.number_input('Enter BMI', min_value=0.0, step=0.1)
# Create a DataFrame from user input
user_data = pd.DataFrame({
    #'Age': [age],
    #'Weight_kg': [weight],
    'Height': [height],  # Convert height to meters
    'Neck_Size': [neck_size],
    'Hip_Size': [hip_size],
    'Waist_Size': [waist_size],
    'BMI': [BMI]
})

# Make predictions
body_fat_percentage = model.predict(user_data)

# Display the predicted body fat percentage
if st.button('Predict Body Fat Percentage'):
    st.write(f'**Predicted Body Fat Percentage:** {body_fat_percentage[0]:.2f}%')

































# # web_app.py
# import streamlit as st
# import pandas as pd
# import pickle

# # Load the best model
# with open('best_model.pkl', 'rb') as model_file:
#     model = pickle.load(model_file)

# st.title('Body Fat Percentage Prediction')

# # User input for height, weight, age, hip size, waist size, and neck size
# height = st.number_input('Enter Height (cm)', min_value=0.0, step=0.1)
# weight = st.number_input('Enter Weight (kg)', min_value=0.0, step=0.1)
# age = st.number_input('Enter Age', min_value=0, step=1)
# hip_size = st.number_input('Enter Hip Size (cm)', min_value=0.0, step=0.1)
# waist_size = st.number_input('Enter Waist Size (cm)', min_value=0.0, step=0.1)
# neck_size = st.number_input('Enter Neck Size (cm)', min_value=0.0, step=0.1)

# # Create a DataFrame from user input
# user_data = pd.DataFrame({
#     'Age': [age],
#     'Weight_kg': [weight],
#     'Height_m': [height / 100.0],  # Convert height to meters
#     'Hip_Size': [hip_size],
#     'Waist_Size': [waist_size],
#     'Neck_Size': [neck_size]
# })

# # Make predictions
# body_fat_percentage = model.predict(user_data)

# # Display the predicted body fat percentage
# if st.button('Predict Body Fat Percentage'):
#     st.write(f'**Predicted Body Fat Percentage:** {body_fat_percentage[0]:.2f}%')














# # web_app.py
# import streamlit as st
# import pandas as pd
# import pickle

# st.title('Body Fat Percentage Prediction')

# # Upload CSV data
# uploaded_file = st.file_uploader('BF_model_dataa', type=['csv'])

# if uploaded_file is not None:
#     # Load the uploaded data
#     input_data = pd.read_csv(uploaded_file)

#     # Load the best model
#     with open('best_model.pkl', 'rb') as model_file:
#         model = pickle.load(model_file)

#     # Make predictions
#     predictions = model.predict(input_data)

#     # Display the predictions
#     st.write('**Predictions:**')
#     st.write(predictions)
