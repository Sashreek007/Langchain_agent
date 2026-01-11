# LinkedIn Profile Summary Agent

## Introduction

This repository contains a LinkedIn Profile Summary Agent built with the LangChain framework. The agent takes publicly available profile data from LinkedIn and uses a large language model to generate a concise summary and a couple of interesting facts about the person. By combining a custom data-scraper, a prompt template and OpenAI's chat model, the script demonstrates how to chain together multiple components into a simple AI "agent."

LangChain is an open-source framework that makes it easier to build applications with language models such as GPT, LLaMA and Mistral. One of its strengths is its support for prompt engineering, allowing you to design reusable templates that guide the model to produce consistent outputs. This project uses LangChain's PromptTemplate, ChatOpenAI and StrOutputParser to assemble a chain that accepts a block of LinkedIn data and returns a formatted summary.

## Features

* **LinkedIn profile scraping** – A helper function in `third_parties/linkedin.py` fetches profile data. When `mock` is set to `True`, it retrieves a sample JSON from a public gist; otherwise it calls the Scrapin API and requires a `SCRAPIN_API_KEY` environment variable.

* **Prompt templating and chaining** – The agent defines a prompt asking the model to generate a short summary and two interesting facts about the person. This prompt is instantiated as a `PromptTemplate`, then piped through a `ChatOpenAI` LLM and a `StrOutputParser` to build a simple chain.

* **Extensible language model** – By default, the script uses OpenAI's gpt-5-mini via `ChatOpenAI`. You can substitute any other LangChain-compatible model (such as Llama or Mistral) by modifying the `llm` instance.

* **Environment configuration** – Secrets (your OpenAI API key and, optionally, a Scrapin API key) are loaded from a `.env` file via python-dotenv. This keeps sensitive data out of the codebase and allows for easy configuration.

* **Pipenv support** – The repository includes a Pipfile specifying dependencies like langchain, langchain-openai, langchain-ollama, langchain-community and python-dotenv. You can also install the packages with pip using a generated requirements.txt.

## Requirements

* **Python ≥ 3.13** – Defined in the Pipfile and Pipfile.lock.
* **OpenAI API key** – Set `OPENAI_API_KEY` in your `.env` file.
* **Scrapin API key (optional)** – If you want to fetch live LinkedIn data, set `SCRAPIN_API_KEY` in your `.env`. When using the mock mode, this is not required.
* **pipenv (optional)** – Recommended for managing virtual environments, though you can use plain pip.

## Installation

### Clone the repository
```bash
git clone https://github.com/Sashreek007/Langchain_agent.git
cd Langchain_agent
```

### Set up a virtual environment (recommended)
```bash
# Using pipenv
pipenv install
pipenv shell

# Or using venv and pip
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### Create a `.env` file in the project root with your API keys:
```
OPENAI_API_KEY=sk-your-openai-key
SCRAPIN_API_KEY=sk-your-scrapin-key   # optional
```

### Run the script
```bash
python main.py
```

The script will load your API keys, fetch data for the hard-coded LinkedIn profile and output a brief summary and two interesting facts.

## Usage

The entry point is `main.py`. It performs the following steps:

1. Load environment variables via python-dotenv.
2. Print out the value of `OPENAI_API_KEY` to verify it loaded correctly.
3. Define a prompt template with placeholders for LinkedIn information. The template requests a short summary and two interesting facts.
4. Initialize a language model (`ChatOpenAI`) with a specified temperature and model name.
5. Compose a chain: `PromptTemplate` → `ChatOpenAI` → `StrOutputParser`.
6. Call `scrape_linkedin_profile()` to retrieve profile data. When `mock=True`, it fetches a JSON example from a public gist, which returns a dictionary under the "person" key.
7. Invoke the chain with the profile information and print the result.

### Customizing the agent

* **Change the LinkedIn URL** – Pass a different URL to `scrape_linkedin_profile()` in `main.py`.
* **Switch models** – To try other models (e.g. a Llama model via Ollama), import and instantiate `ChatOllama` (commented in `main.py`) and replace the `llm` assignment.
* **Modify the prompt** – Edit `summary_template` to request a different number of facts or a different style of summary.
* **Disable mocking** – Call `scrape_linkedin_profile(linkedin_url, mock=False)` to use the live Scrapin API. Remember to set `SCRAPIN_API_KEY` in your environment.

## Project Structure

* `main.py` – The primary script that orchestrates loading environment variables, building the prompt, creating the chain and generating the output.
* `third_parties/` – Contains helper modules for external data. `linkedin.py` defines `scrape_linkedin_profile()` to fetch LinkedIn data either from a mocked gist or from the Scrapin API.
* `.gitignore` – Excludes common virtual environment and environment file patterns.
* `Pipfile / Pipfile.lock` – Define the project's dependencies and Python version.
* `README.md` – The original repository's brief description (one line). This new README supplements it with detailed guidance.

## How It Works

Under the hood, LangChain uses prompt templates to structure the input given to a language model. A prompt template defines placeholders for variables (such as a block of LinkedIn data) and instructions on how to format the output. LangChain's `PromptTemplate` class enables you to reuse and format prompts conveniently. When combined with a `ChatOpenAI` model, it forms part of a chain – a sequence of operations that transforms input data into a final response. In this project, the chain takes LinkedIn data, feeds it through the prompt and model, and parses the text output with `StrOutputParser`.

LangChain is specifically designed to simplify building such pipelines for language models. It offers classes for prompts, memory, agents and vector stores, and its modular design allows you to swap out components like the language model or the data source with minimal changes.

## Contributing

Pull requests and issues are welcome! Future improvements could include:

* Adding support for additional social media platforms (e.g. Twitter or GitHub) via new data scrapers.
* Implementing caching or rate-limiting for the Scrapin API.
* Using LangChain agents to decide which prompts or models to use based on the input profile.
* Integrating vector stores (via langchain-community) to enrich the summary with additional context.

## Acknowledgements

This project builds upon the LangChain framework and uses the `PromptTemplate` and `ChatOpenAI` classes to generate summaries. LangChain is an open-source framework for building applications with language models that provides extensive support for prompt engineering. The data scraping functionality is adapted from the Scrapin API (mocked through a public gist in this example).
