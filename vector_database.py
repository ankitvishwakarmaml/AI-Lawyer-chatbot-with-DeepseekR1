from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


file_path = 'pdfs/'
def upload_pdf(file):
    with open(file_path+file.name ,'wb') as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

#objects = load_pdf('universal_declaration_of_human_rights.pdf')
#
#print(len(objects))
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
        
    )
    
    text_chunks = text_splitter.split_documents(documents)
    
    return text_chunks


test_load = load_pdf('universal_declaration_of_human_rights.pdf')
test_chunk =create_chunks(test_load)
#print("Pdf count: ", len(test_load))
#
#print("Chunks count: ", len(test_chunk))
ollama_model_name ='deepseek-r1:14b'
def embedding_texts(ollama_model_name):
    embeddingmodel = OllamaEmbeddings(model=ollama_model_name)
    return embeddingmodel


FAISS_DB_PATH = "vectorstore/database"

database = FAISS.from_documents(test_chunk, embedding_texts(ollama_model_name))
database.save_local(FAISS_DB_PATH)
