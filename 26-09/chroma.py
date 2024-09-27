import chromadb
import asyncio

client = chromadb.PersistentClient(path = '/savechroma')

print(client.heartbeat()) #controlla connettività server chroma)

client.reset() #resetta database

# chroma_client = chromadb.HttpClient(host = 'localhost', port = 8000) #port = 8000 oppure 8080
#async preposizione funzionale
async def main():
    client = await chromadb.AsyncHttpClient()
    collection = await client.create_collection(name = 'my_collection')
    await collection.add(documents = ['hello world'], ids = ['id1'])
    