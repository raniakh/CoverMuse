import replicate
import streamlit as st
import os
from userInterface import appLayout

os.environ["REPLICATE_API_TOKEN"] = "r8_" #your api token. get yours at: https://replicate.com/docs/get-started/python

cover_letter_info = appLayout()
if bool(cover_letter_info):
    pre_prompt = ("You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. "
                  "You only respond once as 'Assistant'.")

    # Create a prompt for LLM: Include user inputs.
    prompt = f"The job description is: {cover_letter_info['job_desc']}\n"
    prompt += f"The candidate name to include on the cover letter: {cover_letter_info['user_name']}\n"
    prompt += f"The job title/role: {cover_letter_info['role']}\n"
    prompt += f"The company name: {cover_letter_info['company']}\n"
    prompt += f"The hiring manager is: {cover_letter_info['manager']} \n"
    prompt += f"How I heard about the opportunity: {cover_letter_info['referral']} \n"
    prompt += f"The experience I have: {cover_letter_info['experience']} \n"
    prompt += f"The education I have: {cover_letter_info['education']} \n"
    prompt += f"Generate a cover letter"

    # Generate LLM response
    with st.spinner("Generating cover letter"):
        response = replicate.run(
            'a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
            # Llama 2 model
            input={
                "prompt": f"{pre_prompt} {prompt} Assistant:",
                "temperature": cover_letter_info['temp'],
            }
        )
        generated_cover_letter = " ".join([item for item in response])

    generated_cover_letter = generated_cover_letter + ("\n## Test - this line was added after response was generated## "
                                                       "\n")

    st.subheader("Generated Cover Letter:")
    st.write(generated_cover_letter)
    # a download link
    st.subheader("Download the generated cover letter:")
    st.download_button("Download Cover Letter as TXT", generated_cover_letter, key="cover_letter")
