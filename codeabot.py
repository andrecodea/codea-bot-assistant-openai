# API library:
import openai

# Web app library:
import streamlit as st

# Envinronment variables libraries:
from dotenv import load_dotenv, find_dotenv
import os

# Logging library for debugging:
import logging

# Type validation library:
from typing import List, Dict, Generator, Optional

# Environment variables configs:
_ = load_dotenv(find_dotenv())

# Basic configuration for logging:
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Constants:
DEFAULT_MODEL = 'gpt-3.5-turbo'
DEFAULT_MAX_TOKENS = 500
DEFAULT_TEMPERATURE = 0
SYSTEM_MESSAGE = {
    "role": "system",
     "content": "You are CodeaBot, a friendly and useful assistant."
     }

# Set up API client:
def get_openai_client(api_key: Optional[str] = None) -> Optional[openai.Client]:
    """
    Creates OpenAI client with provided or environment API key.
    
    Args:
        api_key: User provided API key
        
    Returns:
        OpenAI client or None if no valid key
    """
    try:
        if api_key and api_key.strip():
            return openai.Client(api_key=api_key.strip())
        elif os.getenv("OPENAI_API_KEY"):
            return openai.Client()
        else:
            return None
    except Exception as e:
        logger.error(f"Error creating API client: {e}")
        return None


# Validate OpenAI key
def validate_api_key(client: openai.Client) -> bool:
    """
    Validates if the API key is working.
    
    Args:
        client: OpenAI client to test
        
    Returns:
        True if key is valid, False otherwise
    """

    try:
        client.models.list()
        return True 
    except openai.AuthenticationError:
        return False
    except Exception as e:
        logger.error(f"Error validating API key: {e}")
        return False 


# Creates the function to generate text:
def generate_text(
    messages: List[Dict[str, str]],
    client: openai.Client,
    model: str = DEFAULT_MODEL,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    temperature: float = DEFAULT_TEMPERATURE,
    stream: bool = True
) -> Optional[Generator]:
    """
    Generates text using OpenAI's API.

    Args:
        messages: Chat messages list.
        model: LLM model being used.
        max_tokens: Max number of tokens for model response.
        temperature: Response's creativity and randomness.
        stream: If the response is a stream.

    Returns:
        Generator with API's response or None if error.
    
    """
    try:
        response = client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            stream=stream,
    )
        return response
    except openai.APIError as e:
        logger.error(f"OpenAI API error: {e}")
        st.error("Error while trying to connect with API. Please verify your API key.")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        st.error("Unexpected error. Please try again.")
        return None


def initialize_session_state():
    """Initializes session state if needed."""

    if 'messages' not in st.session_state:
        st.session_state.messages=[SYSTEM_MESSAGE]
    if 'api_key_validated' not in st.session_state:
        st.session_state.api_key_validated = False

def display_chat_history():
    """Displays chat history."""

    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            with st.chat_message('user'):
                st.write(msg['content'])

        elif msg['role'] == 'assistant':
            with st.chat_message('assistant'):
                st.write(msg['content'])

def process_bot_response(
        user_message:str,
        client: openai.Client,
        model:str,
        temperature:float,
        max_tokens:int
) -> None:
    """
    Processes the user's message and generates bot's response

    Args:
        client: OpenAI client.
        user_message: Message sent by user.
        model: LLM Model being used.
        temperature: Criativity and randomness in response.
        max_tokens: Max amount of tokens per response.
    """
    
    # Adds user message:
    st.session_state.messages.append({"role":"user", "content":user_message})

    # Shows user's message:
    with st.chat_message('user'):
        st.write(user_message)

    # Generates ans shows bot's response:
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = ""

        try:
            with st.spinner("🤔 CodeaBot está pensando..."):
                response_stream = generate_text(
                    st.session_state.messages,
                    client=client,
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

                if response_stream is None:
                    return
                
                for chunk in response_stream:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        message_placeholder.markdown(full_response +"▌")
                
                message_placeholder.markdown(full_response)

        except Exception as e:
            logger.error(f"Error while processing response: {e}")
            message_placeholder.error("Error while generating response. Try again.")
            return
    st.session_state.messages.append({"role":"assistant", "content": full_response})


def main():
    """Main function."""

    # Page layout:
    st.set_page_config(
        page_title="CodeaBot",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )


    # Title and description:
    st.title("🤖 Welcome to CodeaBot!")


    # Initializes session state:
    initialize_session_state()

    # Sidebar with configs:
    with st.sidebar:
        
        st.header("🔑 API Configuration")

        # Input for user's API key
        api_key = st.text_input(
            "OpenAI API Key",
            type="password", 
            placeholder="your key",
            help="Enter your OpenAI API key"
        )

        with st.expander("🛡️ Security Information"):
            st.markdown("""
            **API Key Security:**
            - Your API key is not stored permanently
            - It's only kept in memory during your session
            - Never share your API key with others
            - You can also use environment variables (.env file)
            """)
        with st.expander("📋 Terms of use:"):
            st.markdown("""
            - **API Key**: You are responsible for your API key
            - **Costs**: All costs are your responsibility
            - **Safety**: Maintain your API key secure
            - **Data**: Your chats are not stored
            - **Responsibility**: Use with responsibility
                        
            **This is an educational project.**
            """)

        client = get_openai_client(api_key if api_key.strip() else None)

        if not client:
            st.warning("⚠️ Please provide a valid OpenAI API key in the sidebar to start chatting.")
            st.info("💡 You can get your API key from: https://platform.openai.com/api-keys")
            return

        st.divider()

        st.header("⚙️ Configurations")

        # Clear chat button
        if st.button("🗑️ Clear chat", type="secondary", use_container_width=True):
            st.session_state.messages=[SYSTEM_MESSAGE]
            st.rerun()

        # Divides screen
        st.divider()

        # Model configs
        model = st.selectbox(
            "Modelo",
            ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
            index=0,
            help="Choose an AI model"
        )

        # Temperature slider
        temperature = st.slider(
            "Creativity and randomness",
            min_value=0.0,
            max_value=1.0,
            value=0.0,
            step=0.1,
            help="Higher temperature may induce hallucinations.",
        )

        max_tokens = st.number_input(
            "Amount of tokens per response",
            min_value=100,
            max_value=2000,
            value=500, 
            step=100,
            help="Limit the amount of tokens per response"
        )

        st.divider()

        # Information
        st.subheader("ℹ️ Information")
        st.info(f"💬 Interaction: {len(st.session_state.messages) - 1} messages.")

    # Chat main container
    chat_container = st.container()
    with chat_container:
        # Shows chat history
        display_chat_history()

    
    # User input (locked at inferior part of the screen)
    user_input = st.chat_input("Write something...")
    if user_input and user_input.strip():
        if client:
            process_bot_response(user_input, client, model, temperature, max_tokens)
            st.rerun()
        else:
            st.error("❌ Please provide a valid API key first!")


if __name__ == "__main__":
    main()