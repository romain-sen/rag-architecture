from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from transformers import AutoTokenizer

Settings.llm = Ollama(model="mistral")
Settings.tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
Settings.embed_model = HuggingFaceEmbedding(
    model_name="dangvantuan/sentence-camembert-large"
    # model_name="sentence-transformers/all-mpnet-base-v2"
)

Settings.chunk_size = 1024
Settings.chunk_overlap = 20
