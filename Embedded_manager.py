from sentence_transformers import SentenceTransformer


class Embedded_manager:
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



def main():
    embedded_manager=Embedded_manager()

if __name__=="__main__":
    main()