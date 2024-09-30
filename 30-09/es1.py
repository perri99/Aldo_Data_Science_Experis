from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import os
#Importazione API
os.environ["OPENAI_API_KEY"] = "test_prova"
#Creiamo un semplice documento da utilizzare:
print('Chatbot sui sottogeneri del metal:\n')
#query = input('Domanda: \n')
query= "Qual è il sottogenere del metal che si colloca tra l'heavy metal classico e l'hardcore punk?"

trash_metal = """
Il thrash metal, una delle prime evoluzioni dell'heavy metal e prima forma di metal estremo 
(di cui costituisce il genere principale assieme a death, doom e black metal), 
è il punto di contatto fra l'heavy metal classico e l'hardcore punk. 
Il genere nacque negli Stati Uniti nei primi anni ottanta grazie a Metallica, Megadeth, Slayer e Anthrax, 
definiti dalla stampa The Big Four of Thrash.
"""
black_metal="""Assieme al death metal, al thrash metal e al doom metal, il black metal rientra nella categoria più oltranzista del genere, il metal estremo. Tra i padri indiscussi del genere vi sono i Venom
 con l'esordio Welcome to Hell e ancor di più con il seguente Black Metal (da cui trae origine il nome), senza escludere l'importante contributo di Bathory (considerati la prima vera band del genere), Hellhammer, Celtic Frost, e Mercyful Fate. Anche se musicalmente più inquadrabili nel metal tradizionale (eccetto i Bathory), questi gruppi sono anche classificati da vari critici (perlopiù anglosassoni) come i primi gruppi del genere.[60]
Dal punto di vista ideologico, il black metal è molto noto per l'ostentazione del culto satanista e la forte avversione nei confronti del Cristianesimo. Il black metal è caratterizzato dall'utilizzo di un cantato in scream più "rauco", dall'uso larghissimo di doppia cassa e blast beat, dal ruolo subordinato del basso, dalla forte distorsione delle chitarre e dall'uso di riff particolari rispetto alla tecnica tradizionale dell'heavy metal."""
death_metal="""Nato a metà anni ottanta, il death metal è un altro genere rientrante nel metal estremo. Rappresenta un'evoluzione del thrash metal, che lega la velocità di quest'ultimo con una maggiore violenza e distorsione, data, fra le altre cose, anche dalle tematiche più legate alla morte, al suicidio e al dolore. Fondamentali iniziatori del genere sono gli Slayer con Hell Awaits e ancor di più con il successivo Reign in Blood, dischi che crearono gli standard stilistici del death metal. Molto importanti sono stati anche i Possessed con l'album Seven Churches, dove comparve una forma grezza di growl che sarà un elemento necessario del genere. Oltre al growl, alcuni gruppi alternano esso con linee vocali scream o, in rari casi, clean (voce pulita)"""
doom_metal="""È il genere più cupo della storia dell'heavy metal, di cui sono considerati precursori anche gli stessi Black Sabbath. Il tipico sound doom metal è caratterizzato da linee di batteria molto lente, cadenzate e sinistre; l'uso della doppia cassa si riduce al minimo e le ritmiche chitarristiche presentano un suono molto oscuro. Grande importanza, per lo sviluppo del genere, hanno rivestito le tastiere, che contribuirono a sprigionare atmosfere sulfuree e d'effetto, il tutto condito da testi che trattano spesso il tema dell'occulto, della sofferenza, dell'odio o del satanismo. Tra i maggiori esponenti di questo genere musicale si possono annoverare: i Paradise Lost, gli Anathema e i My Dying Bride che sono considerati una sorta di "magico trio" che ha contribuito a rendere famoso il doom a livello internazionale; oltre a Moonspell, Electric Wizard, Type O Negative, Tiamat, Candlemass, Cathedral, Pentagram."""
metal_core="""Nella seconda metà degli anni 2000 si è affermato il metalcore, derivato dalla fusione di alcune forme estreme del metal con elementi hardcore punk. Il genere si sviluppò in forma underground negli anni ottanta e novanta, inaugurato da gruppi come Earth Crisis, Converge, Hatebreed e Shai Hulud."""
lista_metal=[black_metal,death_metal,doom_metal,trash_metal,metal_core]
#creiamo una lista più specifica nel caso ci sia la presenza di più parole chiave
lista_specifica=[]
if 'black' in query or 'satanismo' in query:
   lista_specifica.append(black_metal)
if 'doom' in query or 'black sabbath' in query:
   lista_specifica.append(doom_metal)
if 'death' in query:
   lista_specifica.append(death_metal)
if 'thrash' in query or 'metallica' in query:
   lista_specifica.append(trash_metal)
if 'core' in query or 'watching the abyss' in query:
   lista_specifica.append(metal_core)

#scegliamo la lista più appropriata da usare 
if len(lista_specifica)==0:
   lista_da_usare=lista_metal
else:
   lista_da_usare=lista_specifica

#Suddividiamo il documento in parti gestibili:
texts_list=[]
for elemento in lista_da_usare:
  text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
  texts = text_splitter.split_text(elemento)
  texts_list.append(texts)
#Creiamo gli embeddings per i chunk di testo e costruiamo l'archivio vettoriale:

embeddings = OpenAIEmbeddings()
vectorstore_list=[]
for pezzo in texts_list:
  vectorstore = FAISS.from_texts(pezzo, embeddings)
  vectorstore_list.append(vectorstore)
#Configuriamo il modello di linguaggio per la generazione delle risposte:

llm = OpenAI(temperature=0)#se aumento temperature aumenta la casualità delle risposte
#Creiamo una catena che combina il recupero dei documenti con la generazione delle risposte:
# Prendiamo il primo vectorstore come base
merged_vectorstore = vectorstore_list[0]

# Aggiungiamo tutti gli altri vectorstore
for vs in vectorstore_list[1:]:
    merged_vectorstore.merge_from(vs)

qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=merged_vectorstore.as_retriever())#DA REPLICARE
#Eseguiamo una query per vedere il sistema in azione:


risposta = qa.run(query)
print("la tua domanda era:", query)
print("Risposta:", risposta)
