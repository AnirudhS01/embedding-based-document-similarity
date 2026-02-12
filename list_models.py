from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

model_list = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

for model in model_list.models.list():
    if "embedding" in model.name:
        print(model.name)