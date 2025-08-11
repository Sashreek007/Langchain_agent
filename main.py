import os
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile


load_dotenv()
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("Hello_langchain")
summary_template = """
    given the Linkedin information {information}  about a person from I want you to create:
    1. a short summary
    2. two interesting facts about them
    """

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

# llm = ChatOllama(model="llama3.1:8b")
llm = ChatOpenAI(temperature=0, model="gpt-5-mini")

chain = summary_prompt_template | llm | StrOutputParser()
linkedin_data = scrape_linkedin_profile(
    linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True
)
res = chain.invoke(input={"information": linkedin_data})

print(res)
