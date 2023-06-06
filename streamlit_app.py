import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat

# Settingup the Main Title
st.title('My Personal Chatbot <3')
#setting up the sub title
st.write('Speak your mind and heart!')
# Setting up the Side-Bar

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
  st.write("Made with ❤️ by Nayanika (<https://youtube.com/dataprofessor>)")
  
# Generate empty lists for generated and past.
## generated stores AI generated responses
# generated IS THE CHATBOT response, past is the HUMAN response
if "generated" not in st.session_state:
  st.session_state["generated"] = ["Hi There! How can I help you?"]
if "past" not in st.session_state:
  st.session_state["past"] = ["Hi!"]
  
  
# creating the containers for input and response
input_container - st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# Take the user input
def get_text():
  text_input = st.get_text("You: ", "", key = "input")
  return text_input

## Applying the user input box
with input_container():
  user_input = get_text()
  
# generate the response
def generate_response(prompt):
  chatbot = hugchat.chatbot()
  response = chatbot.chat(prompt)
  return response
  
