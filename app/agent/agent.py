"""
This module is the main entry point for the agent

Example usage:
    $ python main.py
"""

import pandas as pd
import re

from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.schema import NodeWithScore

from agent.pdf import countries_engine
from agent.population import population_query_engine

tools = [
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

context = """Purpose: The primary role of this agent is to assist users by providing accurate
            information about world population statistics and details about some countries. """

agent = ReActAgent.from_tools(tools=tools, verbose=True, context=context)

# while (prompt := input("Enter a prompt (q to quit): ")) != "q":
#     result = agent.query(prompt)
#     print(result)
#     # Create an empty list to hold the information about each source node
#     source_details = []

#     # Loop through each source node and extract the required information
#     for node in result.source_nodes:
#         # Extract details from each node
#         node_info = {
#             "score": node.score,
#             "filename": node.metadata["file_name"],
#             "page_label": node.metadata["page_label"],
#             "file_path": node.metadata["file_path"],
#             "file_type": node.metadata["file_type"],
#             "last_modified": node.metadata["last_modified_date"],
#             "text": node.text,  # You might want to truncate this if it's very long
#         }
#         source_details.append(node_info)

#     # Print the extracted information for each source node
#     for info in source_details:
#         print(info)
