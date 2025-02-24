import streamlit as st 
from RAG_pipeline import answer_query, llm_model, retrieve_docs

upload_file = st.file_uploader(
    'upload pdf',
    type= 'pdf',
    accept_multiple_files= False
)

# chatbot skeleton (question and answer)

user_query = st.text_area('Enter your prompt here:', height=150, placeholder='Ask anything')

ask_question = st.button('Ask AI Lawyer')

if ask_question:
    
    if upload_file:
        st.chat_message('user').write(user_query)
        
        retrieved_docs=retrieve_docs(user_query)
        response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        
        st.chat_message('AI Lawyer').write(response)
        
    else:
        st.error('No PDF uploaded. Please upload a PDF file.')
        





