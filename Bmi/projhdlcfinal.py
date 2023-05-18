import streamlit as st
st.title("Calculate BMI")#title

name = st.text_input("Enter your name")# Creating a text input box for the name

gender = st.radio("Select your gender", ('Male', 'Female', 'Other'))# Creating a radio button for gender

# Creating a number input box for age
age = st.number_input("Enter your age")

# Creating a text input box for address
address = st.text_area("Enter your address")

# Creating checkboxes for hobbies
hobbies = st.multiselect("Select your hobbies", ('Reading', 'Music', 'Sports', 'Traveling'))

# Creating number input boxes for weight and height
weight = st.number_input("Enter your weight in kg")
height = st.number_input("Enter your height in cms")

bmi = weight / ((height/100)**2)#calculate bmi

# Displaying the BMI
st.write("Your BMI is: ", bmi)

