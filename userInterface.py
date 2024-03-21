import streamlit as st

applayout_dict = {}


def appLayout():
    st.title("Cover Letter Generator with Llama 2")

    with st.form('form to generate cover letter'):
        # User input for cover letter
        st.markdown('### Fill in the requested details')

        applayout_dict['user_name'] = st.text_input("Name")
        applayout_dict['company'] = st.text_input("Company Name")
        applayout_dict['manager'] = st.text_input("Hiring Manager")
        applayout_dict['role'] = st.text_input("Job Title")
        applayout_dict['referral'] = st.text_input("How you came across this job opening?")
        applayout_dict['job_desc'] = st.text_input("Paste the job description")
        applayout_dict['experience'] = st.text_input("Your Experience")
        applayout_dict['education'] = st.text_input("Your Degrees / Certificates")
        applayout_dict['temp'] = st.number_input("AI Temperature. Reflects the model creativity level on a scale of 0 to 1", value=0.5)

        # Generate LLM response
        applayout_dict['generate_cover_letter'] = st.form_submit_button("generate Cover Letter")
        return applayout_dict
