from Embedded_manager import *
from loaders import *
from splitting import*
from langchain_core.documents import Document

def main():
    embedding_manager=Embedding_manager()
    documents=file_loading("./data")
    text_chunks=split_documents(documents)
    print(embedding_manager.generate_embedding(text_chunks))






if __name__=="__main__":
    main()