# Rule Generation 

This project implements a rule generation chatbot using the langchain library. The chatbot utilizes the ChatGPT model provided by OpenAI to generate rules based on user descriptions.

## Features

- Generate rules based on user descriptions.
- Utilizes the langchain library and OpenAI's ChatGPT model.
- Supports both index mode and direct AI agent mode.
- Implements a memory system to store and retrieve conversations.

## Installation

1. Clone the repository:

   ´git clone https://github.com/your-username/rule-generation-chatbot.git´


2. Install the required dependencies:

    ´pip install -r requirements.txt´

3. Set up OpenAI API credentials:

- Sign up for an OpenAI account at https://openai.com/.
- Obtain your API key from the OpenAI dashboard.


and complete settings.py:

    OPENAI_API_KEY = "OPENAI_API_KEY"

    ONLY_INDEX_MODE = False
    OPENAI_llM_MODEL = "gpt-3.5-turbo"
    AI_AGENT_TYPE = AgentType.ZERO_SHOT_REACT_DESCRIPTION
    LLM_TEMPERATURE = 0.5
    AI_AGENT_RETURN_DIRECT = False

    LOCAL_CACHE = False
    INDEX_HTML_PATH = "./templates/index.html"
    RULES_kNOWLEDGE_PATH = "./documents/Rules.md"
    AI_AGENT_TEMPLATE_PATH = "./rulegenerator/templates/rule_generator_template.txt"
    HISTORY_PATH = "./rule_creator/history.txt"
    COLLECTION_NAME = "rule-building-knowledge-base"


## Usage
Run the FastAPI server:

    uvicorn main:app --reload

The server will start running at http://localhost:8000.



## Documentation
For detailed documentation on the project and its components, refer to the following resources:

https://python.langchain.com/en/latest/

https://fastapi.tiangolo.com/