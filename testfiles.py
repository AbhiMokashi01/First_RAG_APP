from Embedded_manager import *
from loaders import *
from splitting import*
from langchain_core.documents import Document
from vectorStore import *


def main():
    embedding_manager=Embedding_manager()
    vectorStore = VectorStore()    

    documents=file_loading("./data")
    chunked_documents=split_documents(documents)
    texts = [doc.page_content for doc in chunked_documents]
    embeddings=embedding_manager.generate_embedding(texts)
    vectorStore.update_vectorStore(chunked_documents,embeddings)
    







if __name__=="__main__":
    main()