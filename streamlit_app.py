import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

st.title('🎈 My Personal Chatbot <3')

# st.write('Hello world!')

#Set the title of the app
st.set_page_config(page_title = "My Personal Chatbot!")

with st.sidebar:
  #set the sidebar title
  st.title(" Chatting App")
  st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](<https://streamlit.io/>)
    - [HugChat](<https://github.com/Soulter/hugging-chat-api>)
    - [OpenAssistant/oasst-sft-6-llama-30b-xor](<https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor>) LLM model
    
    💡 Note: No API key required!
    ''')
  add_vertical_space(5)
  st.write("Made with ❤️ by Nayanika, ref: (<https://youtube.com/dataprofessor>)")
