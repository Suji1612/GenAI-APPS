from openai import OpenAI
import streamlit as st

f = open("keys/genaiapp_key.txt")
key = f.read()
client = OpenAI(api_key=key)
st.snow()
st.title(":rainbow[GenAI Application]")
st.header('GENERATOR APP FOR MCQ', divider='rainbow')

# client.create_completion("Hello world")

prompt = st.text_input('Enter Data Science Topic')
if st.button("Generate"):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role":"system","content":"Generate 3 SQL questions and answer for MCQ test in MCQ format."},
            {"role":"user","content":prompt}
    ]
    )

    if response.choices:
        st.write(response.choices[0].message.content)