
import signal
from langchain.chains import create_retrieval_chain
from langchain.chains import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_ollama import OllamaLLM
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from colorama import Fore


llm = OllamaLLM(model="llama3.2")

embed_model = OllamaEmbeddings(model="nomic-embed-text")

loader = PyPDFLoader("./data/MYTH-Die_Macht_der_Mythen.pdf") # Note: Die Ansichten und Behauptungen im Buch stellen in keiner Weise die Realität dar und dienen der Unterhaltung. Visit www.drachenzahm.com

documents = loader.load()

vector_store = Chroma(embedding_function=embed_model)
vector_store.add_documents(documents)

retriever = vector_store.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="map_reduce", # "map_reduce", "refine" oder "stuff"
    return_source_documents=True,
    verbose=True
)

system_template = """
Answer any use questions based solely on the context below:

<context>
{context}
</context>
"""

human_template = """{input}"""

retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
])

combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

def signal_handler(signum, frame):
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, signal_handler)

def chat_loop():
    print(Fore.BLUE + "Willkommen! 'exit' um zu beenden.")
    print("Beispiel-Fragen: Wer sind Graue?, Wer sind Anunnaki?, Wie werden Erscheinungen beschrieben?, Wer ist Dracula?, Was sind Formwandler und was zeichnet sie aus?, Erzähl mir was von Shangri-La?")
    print(Fore.RED + "Note: Die Ansichten und Behauptungen im Buch stellen in keiner Weise die Realität dar und dienen der Unterhaltung, visit www.drachenzahm.com")
    while True:
        try:
            user_input = input(Fore.GREEN + "User: ")
            if user_input.lower() == 'exit':
                print(Fore.WHITE + "Bye!")
                break

            response = retrieval_chain.invoke({"input": user_input})
            print(Fore.WHITE + response["answer"].replace("\n", " ").replace("*", "\n*"))
        except:
            print(Fore.RED + "Error")

chat_loop()

