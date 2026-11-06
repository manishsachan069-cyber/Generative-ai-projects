from pydantic import BaseModel

class BlogState(BaseModel):
    topic:str = ""
    audience:str = "general reader"

    ###Researcher Output
    research:str = ""
    research_feedback:str = ""

    ###Writer output
    draft:str = ""
    draft_feedback:str = ""

    ###editor Output
    final_blog:str = ""

    ###Metadata
    revesion_count:int = 0
