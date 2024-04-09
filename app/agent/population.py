import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from agent.prompt import new_prompt, instruction_str
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df_path = os.path.join(base_dir, "data", "population.csv")

population_df = pd.read_csv(df_path)

population_query_engine = PandasQueryEngine(
    df=population_df,
    verbose=True,
    instruction_str=instruction_str,
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})
