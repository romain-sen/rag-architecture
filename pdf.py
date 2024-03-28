import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core import SimpleDirectoryReader
from model import Settings


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("Creating index... ", index_name)
        index = VectorStoreIndex.from_documents(
            data, show_progress=True, service_context=Settings
        )
        # Save the index
    else:
        print("Loading index... ", index_name)
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index


pdf_path = os.path.join("data", "pdfs")
countries_pdf = SimpleDirectoryReader(pdf_path).load_data()
countries_index = get_index(countries_pdf, "countries_index")
countries_engine = countries_index.as_query_engine()
# canada_engine.query()
