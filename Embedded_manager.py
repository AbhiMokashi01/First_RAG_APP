from sentence_transformers import SentenceTransformer
import numpy as np

class Embedding_manager:
    def __init__(self,model_name:str="all-MiniLM-L6-v2"):
        self.model_name=model_name
        self.model=None
        self._load_model()

    def _load_model(self):
        try:
            self.model=SentenceTransformer(self.model_name)
            print(f"Model loaded --->{self.model}")
        except Exception as e:
            print(f"model loading failed with----> {e}")

    def generate_embedding(self,texts:list[str])->np.ndarray:
        try:
            if not self.model:
                raise ValueError("Model not loaded")

            embeddings=self.model.encode(texts,show_progress_bar=True)
            print(f"Embedding done for {len(texts)}")
            return embeddings

        except Exception as e:
            print(f"Embedding failed with --->{e}")




def main():
    embedding_manager=Embedding_manager()
    print(embedding_manager.generate_embedding("Hey how are you"))

if __name__=="__main__":
    main()