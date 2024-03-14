# Chatbot Developer Assistant

This is a Streamlit-based chatbot application designed to assist developers in building software by providing step-by-step guides on specific technologies or frameworks. The chatbot leverages an agent to search the internet based on user queries and returns a detailed guide to solve the query.

## Features

1. User-friendly chat interface for developers to ask questions about specific technologies or frameworks.
2. Intelligent agent that searches the web for relevant information based on the user's query.
3. Step-by-step guides generated dynamically to help developers solve their programming problems.
4. Markdown support for code snippets and formatting in the generated guides.

## Installation

1. Clone the repository:


`git clone https://github.com/KimaniKibuthu/chat_over_docs.git`

2. Install Poetry (if not already installed):

`pip install poetry`

3. Install the project dependencies:

`poetry install`

4. Go into the virtual environment

`poetry shell`

5. Setup environments by adding a .env file at the root directory and fill in these API keys:

``` .env
LANGCHAIN_API_KEY=""
LANGCHAIN_PROJECT="chat_over_docs"
LANGCHAIN_TRACING_V2="true"
HUGGINGFACEHUB_API_TOKEN=""
TAVILY_API_KEY=""
```

For the langchain API key, check: https://docs.smith.langchain.com/setup

For the huggingface API key, check: https://huggingface.co/docs/api-inference/en/quicktour#get-your-api-token

For the Tavily API key, check: https://app.tavily.com/


## Usage

1. Run the Streamlit app:

`poetry run streamlit run app.py`

2. Open the provided URL in your web browser.

3. Start chatting with the developer assistant by typing your query in the chat window.


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the Apache 2.0 License
