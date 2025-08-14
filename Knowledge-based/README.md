<!-- #region -->
# Chapter 7-9: Knowledge-based Agents

## Logical Agents
Knowledge-based agents store facts typically using logic. First-order logic is often performed using 
the dedicated logic programming language [Prolog](https://en.wikipedia.org/wiki/Prolog). Here are two online examples using SWI-Prolog:

* [A Simple Prolog Knowledge Base.](https://swish.swi-prolog.org/example/kb.pl)
* [The n-Queens Problem as a Logic Problem.](https://swish.swi-prolog.org/example/queens.pl)

Python provides
several modules for logic and symbolic mathematics. Here is a 
short primer for 
* [Logic Programming with Python.](https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_logic_programming.htm)


## Large Language Models
Large language models (LLMs) are a type of knowledge-based agents that use natural language rather than logic. They can be used via an API or run locally. Important task are [prompt engineering](https://www.kdnuggets.com/a-gentle-introduction-to-context-engineering-in-llms)/[context engineering](https://www.kdnuggets.com/a-gentle-introduction-to-context-engineering-in-llms). Resources:

* [OpenAI Python API Library.](https://github.com/openai/openai-python)
* [Hugging Face](https://huggingface.co/) provides a large collection
  of downloadable pretrained LLMs with 
* [Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) from OpenAI.
* Textbook: [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) by Dan Jurafsky and James H. Martin. Part I contains 
  an excellent introduction to language models, transformers and large language models.


## Agentic AI
An AI solution that uses a set of specially prompted LLM calls. The solution involves any or all of these:

  - Multiple LLM calls
  - LLMs can use tools (browse the web, access files, etc.) to interact with an environment.
  - A planner coordinates activities of the agents: Can be a

    - developer-defined workflow using "prompt chaining" and LLMs giving each other feedback, or 
    - use a LLM to plan its own tasks (the LLM acts as an autonomous agent leading to the name agentic AI).

Video:
* [Introduction to Agentic AI with Coding Examples](https://youtu.be/LSk5KaEGVk4) ([Code repository](https://github.com/ed-donner/action))

Tools:
* [Open AI Agent SDK](https://openai.github.io/openai-agents-python/): native support for function calling, retrieval, and tool orchestration for the OpenAI ecosystem.
* [CrewAI](https://github.com/crewAIInc/crewAI): orchestrate multiple specialized AI agents working collaboratively.
* [Langgraph](https://github.com/langchain-ai/langgraph): a low-level LLM orchestration framework. Build structured, reproducible agent pipelines.
* [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol): An open protocol that enables seamless integration between LLM applications and external data sources and tools.


## License
All code and documents in this repository is provided under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License](https://creativecommons.org/licenses/by-sa/4.0/)

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)
<!-- #endregion -->

```python

```
