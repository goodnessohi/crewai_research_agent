from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

topic = 'Retrieval Augmented Generation Evaluation'

#tool 1
llm = LLM(model = "gpt-4o-mini")

#tool 2
search_tool = SerperDevTool
