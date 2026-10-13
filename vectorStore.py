import chromadb
import numpy as np
import uuid
from langchain_core.documents import Document

class VectorStore:
    def __init__(self,collection_name:str="PDF_Collection",persitant_directory:str="./vectorDB"):
        self.collection_name=collection_name
        self.collection=None
        self.client=None
        self.persistant_directory=persitant_directory
        self._initialise_vectorStore()

    def _initialise_vectorStore(self):
        try:
            self.client=chromadb.PersistentClient(path=self.persistant_directory)
            print("Persistant Client Created")
            self.collection=self.client.get_or_create_collection(self.collection_name)
            print("Collection created in vectorStore")

        except Exception as e:
            print(f"Initialisation of vectorStore failed with{e}")

    def update_vectorStore(self,documents:list[Document],embeddings:np.ndarray):
        ids=[]
        documents_list=[]
        embeddings_list=[]
        metadatas=[]
        if documents is None:
            raise ValueError("Documents were not generated")

        if embeddings is None:
            raise ValueError("Embeddings were not generated")
        if len(documents) != len(embeddings):
            raise ValueError("Mismatch in document and embeddings count")
        for i in range(len(documents)):
            document=documents[i]
            embedding=embeddings[i]

            #Create id for adding entries
            id=f"doc_{uuid.uuid4}-{i}"
            ids.append(id)

            #Creating Metadata
            metadata=dict(document.metadata)
            metadata['content_length']=len(document.page_content)
            metadatas.append(metadata)

            documents_list.append(document.page_content)
            embeddings_list.append(embedding.tolist())

        try:
            self.collection.add(ids,embeddings_list,metadatas,documents_list)
            print(f"{len(documents)}  added to vector store")
        except Exception as e:
            print(f"Failed to add documents to vector store with---->{e}")

       

        