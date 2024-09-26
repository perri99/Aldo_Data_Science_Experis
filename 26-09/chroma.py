import chromadb

client = chromadb.PersistentClient(path = '/savechroma')

print(client.heartbeat()/(10**9 * 60 *60 *24)) #controlla connettività server chroma)