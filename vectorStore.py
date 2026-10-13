import chromadb

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