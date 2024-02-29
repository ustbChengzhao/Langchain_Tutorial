import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect
    
    Here are some examples different Tones:
    - Foemal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.

    Here are some examples of words in different Dialects:
    - American English: Frech Fries,cooton candy,apartment,garbage,cookie,green thumb,parking lot, pants, windshield
    - British English: Chips, candy floss, flat, rubbish, biscuit, green fingers, car park, trousers, windscreen

    Below is the email,tone,and dialect: 
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}
    
    YOUR RESPONSE:
"""
prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template
)

def get_llm():
    llm = OpenAI(temperature=0.5)
    return llm

llm = get_llm()
st.set_page_config(
    page_title="Convert Email",
    page_icon=":robot:"
)
st.header("Globalize Text")

st.markdown("## Enter Your Email To Convert")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        label="Which tone would you like your email to have?",
        options=["Formal", "Informal"]
    )
    
with col2:
    option_dialect = st.selectbox(
        label="Which dialect would you like your email to have?",
        options=["American", "British"]
    )
    

def get_text():
    input_text = st.text_area(label="",
                              placeholder="Your email...",
                              key="email_input")
    return input_text

email_input = get_text()

st.markdown("## Your Converted Email:")

if email_input:
    prompt_with_input = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)
    fomatted_email = llm(prompt_with_input)
    st.write(fomatted_email)