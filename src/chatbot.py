import time
import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
#from langchain.chat_models import ChatOpenAI
#from langchain_community.chat_models import ChatOpenAI

from langchain_community.chat_models import ChatOpenAI

from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
#from langchain_openai import OpenAI

from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)


from langchain.memory import ConversationBufferMemory



class chatbot:
    def __init__(self):

        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
        os.environ["OPENAI_API_TYPE"] = st.secrets["OPENAI_API_TYPE"]
        os.environ["OPENAI_API_BASE"] = st.secrets["OPENAI_API_BASE"]
        os.environ["OPENAI_ENGINE_NAME"] = st.secrets["OPENAI_ENGINE_NAME"]
        


        #template = """You are a chatbot having a conversation with a human.
        #    {chat_history}
        #    Human: {human_input}
        #    Chatbot:"""

        
        self.llm_chain = self.get_chain()
        


        #self.llm = ChatOpenAI(temperature=0.0, 
        #                      engine=os.environ.get("OPENAI_ENGINE_NAME"))

    @st.cache_resource
    def get_chain(_self):
        llm = ChatOpenAI(temperature=0, 
                              engine=os.environ.get("OPENAI_ENGINE_NAME"))
        

        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(
                    content="You are a chatbot having a conversation with a human."
                ),  # The persistent system prompt
                MessagesPlaceholder(
                    variable_name="chat_history"
                ),  # Where the memory will be stored.
                HumanMessagePromptTemplate.from_template(
                    "{human_input}"
                ),  # Where the human input will injected
            ]
        )

        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        
        #prompt = PromptTemplate(
        #    input_variables=["chat_history", "human_input"], template=template
        #)
        #memory = ConversationBufferMemory(memory_key="chat_history")
                
        llm_chain = LLMChain(
            llm=llm,
            prompt=prompt,
            verbose=True,
            memory=memory,
        )

        return llm_chain
        

    def response(_self, prompt):
        
        #messages = [
        #    SystemMessage(content="You are a helpfull assistant."),
        #    HumanMessage(content=f"{prompt}")
        #]


        response = _self.llm_chain.predict(human_input=prompt)
        #response = self.llm(messages)
        return response


    def response_generator(_self, prompt):
        response = _self.response(prompt)
        
        for word in response.split():
            yield word + " "
            time.sleep(0.05)
