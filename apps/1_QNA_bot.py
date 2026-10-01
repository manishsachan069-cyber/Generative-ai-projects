import warnings

warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm=ChatGoogleGenerativeAI(model='gemini-3.6-flash')

st.title("🤖 AskBuddy-QNA Bot")
st.markdown("QNA Bot with LangChain and Google Gemini")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message['role']
    content=message['content']
    st.chat_message(role).markdown(content)

query=st.chat_input("ask anything")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    st.chat_message("ai").markdown(res.content[0]['text'])
    st.session_state.messages.append({"role":"ai", "content":res.content[0]['text']})