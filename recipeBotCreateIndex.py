"""Import packages""" 
from langchain.chat_models import ChatOpenAI
from llama_index import GPTVectorStoreIndex, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage, Document, SimpleDirectoryReader
import os

"""Specify the Open AI API key"""
os.environ['OPENAI_API_KEY'] = 'put_your_key_here'

"""Define a function for the prompt and for loading the input data """
def index_documents(folder):

    """Define variable values for prompt configuration"""
    max_input_size    = 8192
    num_outputs       = 256
    max_chunk_overlap = 0.2
    chunk_size_limit  = 600
    
    """Define class for prompt engineering"""
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit = chunk_size_limit)
    
    """Define wrapper class for langchain LLM settings"""
    llm_predictor = LLMPredictor(llm = ChatOpenAI(temperature = 0, model_name = "gpt-3.5-turbo-16k", max_tokens = num_outputs))

    """Load input documents from a directory"""
    documents = SimpleDirectoryReader(folder).load_data()

    index = GPTVectorStoreIndex.from_documents(documents, llm_predictor = llm_predictor, prompt_helper = prompt_helper)

    """Define target directory for the JSON files"""
    index.storage_context.persist(persist_dir="D:\\Documents\\recipeBot\\recipeIndex")

"""Function call with input directory"""
index_documents("D:\\Documents\\recipeBot\\Recipes")