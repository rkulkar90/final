import streamlit as st

st.title('Projected Salary Estimator')

st.write("Please enter some details below to see your projected salary range:")

# Collect user input
age = st.selectbox('What is your Age Range:', ['18-21', '22-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-69', '70+'])
education = st.selectbox('What is your Education Level:', ["Bachelor's degree", "Master's degree", "Doctoral degree", "Professional doctorate", "No formal education past high school", "I prefer not to answer"])
years_coding = st.selectbox('Select your Coding Experience:', ['< 1 years', '1-3 years', '3-5 years', '5-10 years', '10-20 years', '20+ years', 'I have never written code'])

# Simple rules to project salary
if education == "Doctoral degree" or education == "Professional doctorate":
    base_salary = 120000
elif education == "Master's degree":
    base_salary = 90000
elif education == "Bachelor's degree":
    base_salary = 60000
else:
    base_salary = 40000

# Adjust salary based on experience
if years_coding == '20+ years':
    multiplier = 1.5
elif years_coding == '10-20 years':
    multiplier = 1.3
elif years_coding == '5-10 years':
    multiplier = 1.1
elif years_coding == '3-5 years':
    multiplier = 1.0
elif years_coding == '1-3 years':
    multiplier = 0.9
elif years_coding == '< 1 years':
    multiplier = 0.8
else:
    multiplier = 0.7  # no experience

predicted_salary = int(base_salary * multiplier)

# Display result
st.subheader('Predicted Salary:')
st.success(f"Your estimated yearly salary is around ${predicted_salary:,}")
