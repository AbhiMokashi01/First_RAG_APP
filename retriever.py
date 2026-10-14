from vectorStore import *
from Embedded_manager import *

class Retrieval:
    def retrieve(self,query:str,vectorStore:VectorStore,top_k:int=5,score_threshold:float=0.0):

        retrieved_results=[]
        try:
            #Generate Query Embedding
            embedding_manager=Embedding_manager()
            query_embedding=embedding_manager.generate_embedding([query])[0]

            #Search in vectorstore
            result=vectorStore.collection.query(query_embeddings=[query_embedding.tolist()],n_results=top_k)

            #Returns
            # results={
            #     "ids":[[id1,id2,id3]]
            #     "documents":[[]]
            #     "metadata" :[[]]
            #     "embeddings":[[]]
            #       "distances":[[]]
            #            # }

            ids=result['ids'][0]
            documents=result['documents'][0]
            metadatas=result['metadatas'][0]
            distances=result['distances'][0]


            if result['documents'] and result['documents'][0]:

                for i in range(len(ids)):
                    similariy_score=1-distances[i]

                    if similariy_score>=score_threshold:
                        doc_id=ids[i]
                        document=documents[i]
                        metadata=metadatas[i]
                        distance=distances[i]
                        retrieved_results.append({
                            'id':doc_id,
                            'content':document,
                            'metadata':metadata,
                            'similariy_score':similariy_score,
                            'rank':i+1
                        })

                return retrieved_results

        except Exception as e:
            print(f"failed to retreive result for query->{e}")
            print(f"Error: {type(e).__name__}: {e}")
            raise




def main():
    query="What is the difference between a list and a tuple in Python?"
    retriever_obj=Retrieval()
    vectorStore=VectorStore()
    result=retriever_obj.retrieve(query,vectorStore)
    print(result)

if __name__=="__main__":
    main()