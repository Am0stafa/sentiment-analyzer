from dotenv import load_dotenv
import os
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain.llms import Replicate

load_dotenv()  

# # Access the values using os.environ.get()
# db_user = os.environ.get("DB_USER")
# db_password = os.environ.get("DB_PASSWORD")

# from flowgpt link https://flowgpt.com/prompt/2J_1lBVanD55AdkNHw6g_
template = '''Classify the text into positive, neutral or negative with the score in JSON format:
Text: {{ text }}
Classification:
Score:
'''

prompt = PromptTemplate(template=template, input_variables=["text"])

#initialize Replicate
llm = Replicate(
    model="replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
    input={"temperature": 0.6, "max_length": 500, "top_p": 1}
)

llm_chain = LLMChain(prompt=prompt, llm=llm)

def main():
    # Set the title and description
    st.title("Sentiment Analyzer ChatBot :book:")
    st.write("Enter your text, and this app will provide an answer.")

    # User input
    user_input = st.text_area("Enter your text here:")

    if st.button("Send"):
        # return json
        result = llm_chain.run(user_input)
        st.write("Answer:")
        st.write(result)

if __name__ == "__main__":
    main()
