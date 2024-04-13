import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core import SimpleDirectoryReader
from agent.model import Settings


def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("Creating index... ", index_name)
        index = VectorStoreIndex.from_documents(
            data, show_progress=True, service_context=Settings
        )
        index.storage_context.persist(persist_dir=index_name)
    else:
        print("Loading index... ", index_name)
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index


base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_path = os.path.join(base_dir, "data", "pdfs")
countries_pdf = SimpleDirectoryReader(pdf_path).load_data()
countries_index = get_index(countries_pdf, "indexes/countries_index")
countries_engine = countries_index.as_query_engine()

pdf_path2 = os.path.join(base_dir, "data", "cours_des_comptes")
cdc_pdf = SimpleDirectoryReader(pdf_path2).load_data()
cdc_index = get_index(cdc_pdf, "indexes/cdc_index")
cdc_engine = cdc_index.as_query_engine()
