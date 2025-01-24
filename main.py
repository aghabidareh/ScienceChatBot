import streamlit as st
from transformers import pipeline

qa_model = pipeline("question-answering", model="timpal0l/mdeberta-v3-base-squad2")

#Design
st.set_page_config(page_title="پرسسش و پاسخ هوشمند" , page_icon="🤖" , layout="centered")
st.title('پرسش و پاسخ هوشمند')

st.write('لطفا سوال خود را وارد کنید:')
question = st.text_input("سوال شما:")

#Answer the Question
if question:
    try:
        with open('data/combined/combined_text.txt' , 'r', encoding='utf-8') as file:
            context = file.read()

        result = qa_model(question=question, context=context)
        answer = result["answer"]

        st.success("پاسخ:")
        st.write(answer)
    except Exception as e:
        st.error(f"خطا در پردازش : {e}")
else:
    st.info("لطفا ابتدا سوال خود را وارد کنید")