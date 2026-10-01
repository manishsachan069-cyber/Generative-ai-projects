from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

llm=ChatGroq(model="openai/gpt-oss-20b", streaming=True)
search=GoogleSerperAPIWrapper()
tools=[search.run]

if "memory" not in st.session_state:
    st.session_state.memomy=MemorySaver()
    st.session_state.history=[]


agents=create_agent(
    model=llm,
    tools=tools,
    checkpointer=st.session_state.memory,
    system_prompt="you are amazing ai agent and can also search from google as well"
)

### BUILDING WEB INTERFACE..

st.subheader("QuickAnswer - Answer at the speed of thought")


for message in st.session_state.history:
    role=message["role"],
    content=message["content"],
    st.chat_message(role).markdown(content)

query=st.chat_input("ask anything")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role":"user", "content": query})

    response=agents.stream(
        {"messages":[{"role":"user", "content": query}]},
        {"configurable": {"thread_id":"1"}},
        stream_mode="messages"
        )

    ai_container=st.chat_message("ai")    ### AI ka container banaya
    with ai_container:                    ### container k refernce se empty space create kia
        space=st.empty()

        message=""                        ### message variable banaya jisme chunk k data ko store krege

        for chunk in response:               ###jese jese chunk ka response milta he, ham use message me append krte jate he 
            message=message+chunk[0].content
            space.write(message)                 ### and finaly space me write krte he 

    st.session_state.history.append({"role":"ai", "content": message})
