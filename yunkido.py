# from dotenv import load_dotenv
# load_dotenv()

from langchain.chat_models import ChatOpenAI
import streamlit as st

'https://syskido.tistory.com' 

chat_model = ChatOpenAI()

st.text('나령 윤기도 인공지능 단편소설') 
content = st.text_input('단편소설의 주제를 제시해주세요.') 

if st.button('단편소설 2000자 내외 작성 요청하기'):
    with st.spinner('시 작성 중....'):
        result = chat_model.predict(content + "에 대한 단편소설를 써줘")
        st.write(result)




   
   
   