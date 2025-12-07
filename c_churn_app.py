def load_model():
    with open("c_churn_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

# slidebar

logo = "parami.jpg"
st.sidebar.image(logo, use_container_width=True)
st.sidebar.title("Introduction to Machine Learning")
st.sidebar.subheader("Midterm Project\nNyein Min Soe")
st.sidebar.markdown(
    """
    **Student ID:** PIUS20230027  
    **Email:** nyeinminsoe@parami.edu.mm
    """
)


# title
st.title('Customer Churn Classifier')
st.subheader("About the Dataset")
st.write('This dataset is randomly collected from an Iranian telecom companyâ€™s database over a period of 12 months. A total of 3150 rows of data, each representing a customer, bear information for 13 columns. The attributes that are in this dataset are call failures, frequency of SMS, number of complaints, number of distinct calls, subscription length, age group, the charge amount, type of service, seconds of use, status, frequency of use, and Customer Value.')
st.subheader("Select the parameters of the customer")


# input

Call_Failure = st.slider(
    "Number of call failures.", 0, 36, 6, step=1)

Complains = int(st.selectbox(
    'Complains (0 is No complaint, 1 is having complaint.)', 
    options=[1, 0], index=0))

Subscription_Length = st.slider(
    "Total months of subscription", 3, 47, 35, step=1)

Charge_Amount = int(st.selectbox(
    "Charge amount (0 is lowest, 9 is highest).", 
    options=[0,1,2,3,4,5,6,7,8,9], index=0))

Seconds_of_Use = st.slider(
    "Total seconds of calls", 0, 17090, 2990, step=1)

Frequency_of_use = st.slider(
    "Total number of calls", 0, 255, 54, step=1)

Frequency_of_SMS =  st.slider(
    "Total number of text messages", 0, 552, 21, step=1)

Distinct_Called_Numbers =st.slider(
    "Total number of distinct phone calls ", 0, 552, 21, step=1)

Age_Group = int(st.selectbox(
    "Age Group (1 is younger age, 5 is older age)",
    options=[1,2,3,4,5], index=0))

Status = int(st.selectbox(
    "Sim Status (0 is active, 1 is non-active)", 
    options=[0,1], index=0))

Customer_Value = st.slider("The calculated value of customer", 0.00, 2200.00, step = 0.01)


# predict

if st.button("🚀 Predict"):
    input_data = pd.DataFrame([{
        "Call  Failure": Call_Failure,
        "Complains": Complains,
        "Subscription  Length": Subscription_Length,
        "Charge  Amount": Charge_Amount,
        "Seconds of Use": Seconds_of_Use,
        "Frequency of use": Frequency_of_use,
        "Frequency of SMS": Frequency_of_SMS,
        "Distinct Called Numbers": Distinct_Called_Numbers,
        "Age Group": Age_Group,
        "Status": Status,
        "Customer Value": Customer_Value}])



    model=load_model()
    prediction = model.predict(input_data)
    
    # output
    
    if prediction == 1:
        st.success(f'**🎉 This is your customer**')
    else:
        st.error(f'**💔 This is no longer your customer**')


