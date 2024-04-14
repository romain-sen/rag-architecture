import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core import PromptTemplate
from agent.model import Settings

import os


# new_prompt = PromptTemplate(
#     """\
#     You are working with a pandas dataframe in Python.
#     The name of the dataframe is `df`.
#     This is the result of `print(df.head())`:
#     {df_str}

#     Follow these instructions:
#     {instruction_str}
#     Query: {query_str}

#     Expression: """
# )

# instruction_str = """\
#     1. Convert the query to executable Python code using Pandas.
#     2. The final line of code should be a Python expression that can be called with the `eval()` function.
#     3. The code should represent a solution to the query.
#     4. PRINT ONLY THE EXPRESSION.
#     5. Do not quote the expression."""


# base_dir = os.path.dirname(os.path.abspath(__file__))
# df_path = os.path.join(base_dir, "data", "population_world_melted.csv")

# population_df = pd.read_csv(df_path)

# population_query_engine = PandasQueryEngine(
#     df=population_df,
#     verbose=True,
#     instruction_str=instruction_str,
#     service_context=Settings,
# )


# population_query_engine.update_prompts({"pandas_prompt": new_prompt})


# Chemin d'accès au fichier CSV
base_dir = os.path.dirname(os.path.abspath(__file__))
df_path = os.path.join(base_dir, "data", "population_world_melted.csv")

# Chargement des données
population_df = pd.read_csv(df_path)

# Template de prompt pour le Query Engine
new_prompt = PromptTemplate(
    "You are working with a pandas dataframe in Python. "
    "The name of the dataframe is `df`. "
    "This is the result of `print(df.head())`: {df_str}\n\n"
    "Follow these instructions: {instruction_str}\n"
    "Query: {query_str}\n\n"
    "Expression: "
)

# Instructions pour le Query Engine
instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. Filter by year, like 2020 : df[df["Year"] == "2020"].
    4. Filter by country, like France : df[df["Country"] == "France"].
    4. Population of France in 2020 : df[(df["Country"] == "France") & (df["Year"] == "2020")]["Population"].
    5. PRINT ONLY THE EXPRESSION.
    6. Do not quote the expression.
    7. Do not exclude any rows from the dataframe.
    """

# Initialisation du Query Engine
population_query_engine = PandasQueryEngine(
    df=population_df,
    verbose=True,
    instruction_str=instruction_str,
    service_context=Settings,
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})
