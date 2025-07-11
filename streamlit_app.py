import streamlit as st
from persona.memory import UserMemory
from persona.chain_of_thought import ChainOfThought
from persona.persona import Persona
from persona.prompt_manager import PromptManager

st.set_page_config(page_title="Persona Bot", page_icon="🤖")
st.title("🤖 Persona Bot")

if 'user_memory' not in st.session_state:
    st.session_state['user_memory'] = UserMemory()
if 'chain' not in st.session_state:
    st.session_state['chain'] = ChainOfThought()
if 'persona' not in st.session_state:
    st.session_state['persona'] = Persona()
if 'prompt_manager' not in st.session_state:
    st.session_state['prompt_manager'] = PromptManager("prompts/")

user_input = st.text_input("You:", "", key="user_input")
if st.button("Send") or user_input:
    st.session_state['chain'].start(user_input)
    thoughts = st.session_state['chain'].get_thoughts()
    with st.expander("Bot's Thoughts", expanded=True):
        for t in thoughts:
            st.write(f"- {t}")
    response = st.session_state['persona'].respond(
        user_input,
        st.session_state['user_memory'],
        st.session_state['chain'],
        st.session_state['prompt_manager']
    )
    st.markdown(f"**Bot:** {response}")
