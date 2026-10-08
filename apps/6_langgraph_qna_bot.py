from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages ##add_message will store user questiona dn AI response in te form of List.
from langgraph.checkpoint.memory import InMemorySaver
from typing import Annotated

class ChatState(BaseModel):
    messages:Annotated[list, add_messages]

llm=ChatGroq(model="openai/gpt-oss-20b")

def ChatBotNode(state:ChatState)->ChatState: ##->It means it will directly return the chatstate
    res=llm.invoke(state.messages)
    state.messages=[res]                     ##It will append the users messages and LLM response
    return state

memory=InMemorySaver()

graph=StateGraph(ChatState)

graph.add_node("chatnode", ChatBotNode)

graph.add_edge(START, "chatnode")
graph.add_edge("chatnode", END)

graph=graph.compile(checkpointer=memory)

while True:
    query=input("user: ")
    if query.lower() in ["quite", "break", "bye"]:
        print("Thank you for your time")
        break

    res=graph.invoke(
        {"messages":[{"role":"user", "content":query}]},
        {"configurable":{"thread_id":1}}
    )

    ans=res["messages"][-1].content

    print("AI: ", ans)

