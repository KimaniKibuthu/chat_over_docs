import streamlit as st
import random
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.agents import AgentExecutor, Tool, create_react_agent
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from utils import RetryCallbackHandler
from prompts import prompt_two

# Load environment variables
load_dotenv()

# Create prompts

prompt_template = PromptTemplate.from_template(prompt_two)


# Mixtral LLM

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

mixtral = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.3)

# Instantiate error handler
error_handler = RetryCallbackHandler()

# Instantiate tools
search = TavilySearchResults()

tool_search_item = Tool(
    name="search internet",
    description="Searches the internet for the documentation and examples in order to answer a query",
    func=search.run,
    handle_tool_error=True,
)

# List of all tools
tools = [tool_search_item]

# Instantiate agents


agent = create_react_agent(mixtral, tools, prompt_template)


agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True,
    handle_parsing_errors=True,
    callbacks=[error_handler],
)


def main():
    st.set_page_config(
        page_title="Price Range Predictor, powered by gemini",
        page_icon="🧠",
        layout="centered",
        initial_sidebar_state="auto",
        menu_items=None,
    )

    st.title("🧠 Your Docs Helper")
    st.caption("📋 A Helper to aid you with your questions on development")

    spinner_messages = [
        "Spinning up some code magic...",
        "Finding answers faster than a speeding bullet...",
        "Cooking up some code soup...",
        "Holding on tight, we're about to take off into the coding cosmos...",
        "Gathering data faster than a caffeinated programmer...",
        "Revving up the engine... Vroom Vroom!",
        "Brace yourself, the code storm is coming...",
        "Warp speed engaged! Hold on to your keyboard!",
        "Loading... or as we like to call it, the digital equivalent of holding your breath...",
        "Building castles in the cloud... of code!",
    ]

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "How can I help you?"}
        ]

    if prompt := st.chat_input("How can I help?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner(random.choice(spinner_messages)):
            agent_response = agent_executor.invoke({"input": prompt})
            agent_output = agent_response["output"]
        st.session_state.messages.append({"role": "assistant", "content": agent_output})
        st.chat_message("assistant").write(agent_output)


if __name__ == "__main__":
    main()
