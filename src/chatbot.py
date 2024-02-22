import time
import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

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
        
        self.llm_chain = self.get_chain()


    @st.cache_resource
    def get_chain(_self):
        pass

    def response(_self, prompt):
        pass


    def response_generator(_self, prompt):
        pass