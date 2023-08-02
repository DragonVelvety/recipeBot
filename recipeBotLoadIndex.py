"""Import packages"""
from langchain.chat_models import ChatOpenAI
from llama_index import GPTVectorStoreIndex, LLMPredictor, Document, PromptHelper, StorageContext, load_index_from_storage, SimpleDirectoryReader
from llama_index.indices.query.query_transform.base import HyDEQueryTransform
from llama_index.query_engine.transform_query_engine import TransformQueryEngine
import os

"""Specify the Open AI API key"""
os.environ['OPENAI_API_KEY'] = 'put_your_key_here'

def query_with_index(query_str, persist_dir="D:\\Documents\\recipeBot\\recipeIndex"):
    
    """Rebuild the storage context"""
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)

    """Load the index"""
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    response = str(query_engine.query(query_str))
    
    return response  