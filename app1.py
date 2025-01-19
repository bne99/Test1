import streamlit as st
import pandas as pd

# Initialize session state
if 'emails' not in st.session_state:
    st.session_state.emails = []

# Function to add a new email
def add_email(subject, recipient, status):
    st.session_state.emails.append({
        'Subject': subject,
        'Recipient': recipient,
        'Status': status
    })

# Streamlit app layout
st.title('Email Management System')

# Input form for new emails
with st.form(key='email_form'):
    subject = st.text_input('Email Subject')
    recipient = st.text_input('Recipient')
    status = st.selectbox('Status', ['Pending', 'Sent', 'Replied'])
    submit_button = st.form_submit_button(label='Add Email')

    if submit_button:
        add_email(subject, recipient, status)
        st.success('Email added successfully!')

# Display the email list
if st.session_state.emails:
    st.subheader('Email List')
    df = pd.DataFrame(st.session_state.emails)
    st.dataframe(df)
else:
    st.info('No emails added yet.')
