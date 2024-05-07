import ollama

def get_embedding(text):
    return ollama.embeddings(model='nomic-embed-text:latest', prompt=text)['embedding']