from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError("GOOGLE_API_KEY not found")


documents = [
    "aws stands for amazon web services",
    "gcp stands for google cloud platform",
    "azure stands for microsoft azure"
]

query = "what does aws stand for?"
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001",dimension=300)

#we need to create embeddings for each doc and also the user query
doc_embeddings = embedding_model.embed_documents(documents)
# print(doc_embeddings)


query_embedding = embedding_model.embed_query(query)
query_array = np.array(query_embedding)
print(query_array.shape)
print(query_array.size)
# print(query_embedding)

score = cosine_similarity([query_embedding], doc_embeddings)[0]

index, respective_score = sorted(list(enumerate(score)), key= lambda x:x[1])[-1]
print("")
print("The query is " + query)
print(documents[index])
print("The similarity score for the above query from the docs provided is " + str(respective_score))
print(" ")