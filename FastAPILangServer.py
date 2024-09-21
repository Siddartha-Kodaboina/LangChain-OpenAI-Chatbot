#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# 1. Creating the template
system_message = "Traslate the following text to {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_message),
    ('user', '{text}')
  ]
)

# 2. Creating the Model
model = ChatOpenAI()

# 3. Creating the parser
parser = StrOutputParser()

# 4. Creating the chain
chain = prompt_template | model | parser

# 5. Creating the FastAPI app
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 6. Adding chain route
add_routes(app, chain, path='/chain')

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='localhost', port=8000)