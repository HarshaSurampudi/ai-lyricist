from qdrant_client import QdrantClient
from embedding import get_embedding

client = QdrantClient(url="http://localhost:6333")

query = input("What type of song are you looking for? : ")
vector = get_embedding(query)

search_result = client.search(
    collection_name="instructions",
    query_vector=vector,
    limit=3
)


for result in search_result:
    print(result.payload['url'])
    print(result.payload['instructions'])
    print("----")
