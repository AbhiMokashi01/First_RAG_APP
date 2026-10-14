from Embedded_manager import *
from loaders import *
from splitting import*
from langchain_core.documents import Document
from vectorStore import *
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from retriever import *



def main():
    load_dotenv()
    llm=init_chat_model("openai/gpt-oss-20b",model_provider="groq")
    embedding_manager=Embedding_manager()
    vectorStore = VectorStore()    

    documents=file_loading("./data")
    chunked_documents=split_documents(documents)
    texts = [doc.page_content for doc in chunked_documents]
    embeddings=embedding_manager.generate_embedding(texts)
    vectorStore.update_vectorStore(chunked_documents,embeddings)

    retreiver=Retrieval()

    retreived_result=retreiver.retrieve("What are Python dictionaries and how are they used",vectorStore)

    context = "\n\n".join(
    doc["content"] for doc in retreived_result)

    prompt=f"Explain me usage of dictionaries by refering to {context}"

    ans=llm.invoke(prompt)
    print(ans.content)

    







if __name__=="__main__":
    main()