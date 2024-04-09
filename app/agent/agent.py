"""
This module is the main entry point for the agent

Example usage:
    $ python main.py
"""

import pandas as pd

from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent

from agent.prompt import context
from agent.note_engine import note_engine
from agent.pdf import countries_engine
from agent.population import population_query_engine

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="population_data",
            description="This gives informations about the world population statistics and details about a country.",
        ),
    ),
    QueryEngineTool(
        query_engine=countries_engine,
        metadata=ToolMetadata(
            name="countries_data",
            description="Query engine for the countries PDF. This gives informations about the countries (France and Canada).",
        ),
    ),
]

agent = ReActAgent.from_tools(tools=tools, verbose=True, context=context)

# while (prompt := input("Enter a prompt (q to quit): ")) != "q":
#     result = agent.query(prompt)
#     print(result)
