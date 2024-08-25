from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai import MistralAIEmbedding
import getpass
import os


# Initialize MistralAI models
api_key = "eWfdrWhrbEF5NASCvN7URoCQTfQ41V39" #Input your mistral api key
llm = MistralAI(api_key=api_key)
embed_model = MistralAIEmbedding(model_name="mistral-embed", api_key=api_key)

# Set global settings
Settings.llm = llm
Settings.embed_model = embed_model

# Load documents and create index
reader = SimpleDirectoryReader(input_files=['extracted_text.txt'])
documents = reader.load_data()
index = VectorStoreIndex.from_documents(documents)
vector_store = index.storage_context.vector_store

# Optionally: Print vector details
vector_store_dict = vector_store.to_dict()
embedding_dict = vector_store_dict['embedding_dict']
print(f"Number of embeddings: {len(embedding_dict)}")

query_engine = index.as_query_engine(similarity_top_k=4)

from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_input = request.json.get("message")
    print(f"User input: {user_input}")  
    response = query_engine.query(user_input)
    print(f"Query engine response: {response}")  
    if response.response == "Sorry, I don't have an answer for that. Please contact the business directly.":
        response = "Sorry, I don't have an answer for that. Please contact the business directly."
    else:
        response = response.response
    print(f"Final response: {response}")  
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)