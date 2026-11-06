import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

def get_llm(model_name:str = "openai/gpt-oss-20b", temprature=0.5):
    api_key=os.getenv("chat_groq_api_key")
    llm=ChatGroq(model=model_name, temperature=temprature, api_key=api_key)
    return llm


researcher_prompt=ChatPromptTemplate.from_messages([
    {"role":"system", "content":"""
        
        "You are a research agent. Given a blog topic and target audience, produce a clear,"
        "structure research outline. Include:\n"
        "1. 5-7 key points the blog should cover\n"
        "2. Important facts, stats, or examples for each point\n"
        "3. Suggested angle or hook\n"
        "Be concise. Use bullet points. Do not write full blog yet "

"""},
    {"role":"user", "content":"Topic: {topic}, Audience:{audience}, {revision_hints}, Write the research outline now. "}
])


def researcher_agent(llm:ChatGroq, topic:str, audience:str, feedback:str = "" )->str:
    revision_hints=f"The human provided this feedback on your previouse research. Please address it{feedback}."
    if not feedback:
        revision_hints="This is your first attempt"

    chain= researcher_prompt | llm
    result=chain.invoke(
        {
            "topic":topic,
            "audience":audience,
            "revision_hints":revision_hints

        }
    )
    return result.content


###writer agent

writer_prompt=ChatPromptTemplate.from_messages([
    {"role":"system", "content":"""
        
        "You are a blog writer agent. using the research notes provided, write a omplete,"
        "engaging blog post. \n"
        "Rules: \n"
        "Length: 500-800 words. \n"
        "Structure: catchy title, intro hook, 3-5sections with H2 headings, conclusion\n"
        "- Tone: Clear, friendly, suited to the target audience\n"
        "- Use markdown formatting\n"
        "Do not add 'word count' line at the end"

"""},
    {"role":"user", "content":"""
        Topic:{topic},
        Audience:{audience},
        Research Notes:{research},

        {revision_hints}

        Write the full blog post now.

    """}
])

def writer_agent(llm:ChatGroq, topic:str, audience:str, research:str = "", feedback:str = "" )->str:
    revision_hints=f"The human provided this feedback on your previouse draft and asked for thee changes:{feedback}. Please apply thee changes during writing the blog"
    if not feedback:
        revision_hints="This is your first attempt"

    chain= writer_prompt | llm
    result=chain.invoke(
        {
            "topic":topic,
            "audience":audience,
            "research":research,
            "revision_hints":revision_hints

        }
    )
    return result.content



###editor prompt

editor_prompt=ChatPromptTemplate.from_messages([
    {"role":"system", "content":"""
        
       "You are a editor agent- the final quality gate before publishing.\n"
       "Take the draft and produce the final polished version. Specifically:\n"
       "- Fix grammer, spelling, and awkward phrasing\n"
       "- Tighten word sentences\n"
       "- Improve flow and transitions between sections\n"
       "- Make the title and intro more compelling if needed\n"
       "- Keep the same structure and markdown formatting\n"
       "- Blog wordings should look ike human and not an AI, and dont use any special chars/complex/fancy words.\n"
       "Output only the final polished blog post - no commentary"
"""},
    {"role":"user", "content":"""
        Topic:{topic},
        draft:{draft}

        Return the published bog post.

    """}
])


def editor_agent(llm:ChatGroq, topic:str, draft:str = "")->str:

    chain= editor_prompt | llm
    result=chain.invoke(
        {
            "topic":topic,
            "draft":draft

        }
    )
    return result.content