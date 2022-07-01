import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('model.pkl', 'rb'))

def run():
    img1 = Image.open('bank.png')
    img1 = img1.resize((700,130))
    st.image(img1,use_column_width=False)
    st.sidebar.title("Loan Eligibility Prediction")
    text = '''
    Loan Eligibility Prediction uses Random Forest Classifier to predict whether a person is eligible for a loan or not.
     Distribution of the loans is the core business part of almost every banks.
     The main portion the bank’s assets is directly came from the profit earned from the loans distributed by the banks. 
     The prime objective in banking environment is to invest their assets in safe hands where it is.
     Today many banks/financial companies approves loan after a regress process of verification and validation but still there is no surety whether the chosen applicant is the deserving right applicant out of all applicants. 
     Through this system we can predict whether that particular applicant is safe or not and the whole process of validation 
    '''
    st.sidebar.write(text)
    x = False




    st.title("In need of small Business loan? Enter your details")

    ## Full Name
    fn = st.text_input('Full Name')

    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Marital Status
    mar_display = ('No','Yes')
    mar_options = list(range(len(mar_display)))
    mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

    ## No of dependets
    dep_display = ('No','One','Two','More than Two')
    dep_options = list(range(len(dep_display)))
    dep = st.selectbox("Dependents",  dep_options, format_func=lambda x: dep_display[x])

    ## For edu
    edu_display = ('Not Graduate','Graduate')
    edu_options = list(range(len(edu_display)))
    edu = st.selectbox("Education",edu_options, format_func=lambda x: edu_display[x])

    ## For emp status
    emp_display = ('Job','Business')
    emp_options = list(range(len(emp_display)))
    emp = st.selectbox("Employment Status",emp_options, format_func=lambda x: emp_display[x])

    ## For Property status
    prop_display = ('Rural','Semi-Urban','Urban')
    prop_options = list(range(len(prop_display)))
    prop = st.selectbox("Property Area",prop_options, format_func=lambda x: prop_display[x])

    ## For Credit Score
    cred_display = ('Between 300 to 500','Above 500')
    cred_options = list(range(len(cred_display)))
    cred = st.selectbox("Credit Score",cred_options, format_func=lambda x: cred_display[x])

    ## Applicant Monthly Income
    mon_income = st.number_input("Applicant's Monthly Income($)",value=0)

    ## Co-Applicant Monthly Income
    co_mon_income = st.number_input("Co-Applicant's Monthly Income($)",value=0)

    ## Loan AMount
    loan_amt = st.number_input("Loan Amount",value=0)

    ## loan duration
    dur_display = ['2 Month','6 Month','8 Month','1 Year','16 Month']
    dur_options = range(len(dur_display))
    dur = st.selectbox("Loan Duration",dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        if dur == 1:
            duration = 180
        if dur == 2:
            duration = 240
        if dur == 3:
            duration = 360
        if dur == 4:
            duration = 480
        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 1:
            st.balloons()
            st.header("Congratulations! You are Eligible for the loan.")
        else:
            st.snow();
            st.header("Sorry! You are not eligible for the loan.")
            

run()