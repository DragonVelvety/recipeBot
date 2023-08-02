"""Import packages"""
import os
import openai
import gradio as gr
import datetime
from recipeBotLoadIndex import query_with_index
from llama_index.indices.query.query_transform.base import HyDEQueryTransform
from llama_index.query_engine.transform_query_engine import TransformQueryEngine

"""Specify the Open AI API key"""
os.environ['OPENAI_API_KEY'] = 'put_your_key_here'

"""Define Basic UI settings like title and theme"""
selected_theme = gr.themes.Soft(primary_hue=gr.themes.colors.blue, secondary_hue=gr.themes.colors.cyan)
block = gr.Blocks(title="Rezept-Chatbot", theme=selected_theme)

"""Define the UI settings"""
with block:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear_btn = gr.Button("Delete")
    custom_favicon = "D:\\Documents\\recipeBot\\faviconChatbot.png"
    
    """Create a function for updating the chat history"""
    def user(user_message, history):
        return gr.update(value="", interactive=False), history + [[user_message, None]]

    def bot(history):
        """Get the last user message"""
        last_user_message = history[-1][0]

        # Call the query_index function with the last user message
        output = query_with_index(last_user_message)
        bot_message = output
        history[-1][1] = ""
        for character in bot_message:
            history[-1][1] += character
            yield history
    
    """Clear all fields"""
    def clear():
        return None, None

    response = msg.submit(user, [msg, chatbot], [msg, chatbot], queue=True).then(bot, chatbot, chatbot)
    response.then(lambda: gr.update(interactive=True), None, [msg], queue=False)

    clear_btn.click(fn=clear, inputs=None, outputs=[msg, chatbot])

block.queue(concurrency_count=3)
block.launch(debug=True, favicon_path=custom_favicon)