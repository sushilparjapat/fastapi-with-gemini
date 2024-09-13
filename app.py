from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from fastapi import FastAPI
from langserve import add_routes
import uvicorn
import getpass
import os



app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"
)

KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = getpass.getpass(KEY)



prompt2=PromptTemplate(
    input_variables=["topic"],
    template="Write me an poem about {topic} for a 5 years child with 100 words?"
)

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3, convert_system_message_to_human=True) 



add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8003)