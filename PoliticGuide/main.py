from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import ModelScopeEmbeddings
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from operator import itemgetter
from langchain_openai import ChatOpenAI, OpenAI
import os
import getpass
import pinecone
# os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
# os.environ["OPENAI_API_KEY"] = "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"
os.environ["PINECONE_API_KEY"] = "6772fa80-cc57-4283-8820-cb81189c91d4"
def read_pdf(file_path):
    # loader = PyPDFDirectoryLoader(file_path, extract_images=True)
    loader = PyPDFLoader("/Users/apple/Documents/coding/Langchain_Tutorial/PoliticGuide/马克思主义基本原理.pdf", )
    # raw_documents = loader.load()
    # loader = PyPDFLoader("./中国近代史纲要.pdf", )
    # raw_documents += loader.load()
    # loader = PyPDFLoader("./毛泽东思想和中国特色社会主义理论体系概论.pdf", )
    # raw_documents += loader.load()
    # loader = PyPDFLoader("./思想道德与法治.pdf", )
    # raw_documents += loader.load()
    
    # loader = PyPDFLoader(file_path)
    raw_documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=50,
                                     chunk_overlap=0)
    documents = splitter.split_documents(raw_documents)

    embeddings = ModelScopeEmbeddings(model_id="iic/nlp_gte_sentence-embedding_chinese-base")
    embeddings = ModelScopeEmbeddings()
    # db = FAISS.from_documents(documents, embeddings)
    # db.save_local(os.path.join("./db", file_path.replace(".pdf", "") + ".faiss"))
    # db.save_local("./db/all.faiss")
    
    # 使用向量数据库Pinecone存储
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment="gcp-starter",
    )
    docsearch = pinecone.from_documents(documents, embeddings, index_name="politicguide")
    return None
    
def Context(query, subject="全学科"):
    db_path = {"中国近代史纲要": "./db/中国近代史纲要.faiss",
               "马克思主义基本原理": "./db/马克思主义基本原理.faiss",
               "毛泽东思想和中国特色社会主义理论体系概论": "./db/毛泽东思想和中国特色社会主义理论体系概论.faiss",
               "思想道德与法治": "./db/思想道德与法治.faiss",
               "全学科": "./db/all.faiss"}
    
    embeddings = ModelScopeEmbeddings(model_id="iic/nlp_gte_sentence-embedding_chinese-base")
    # db = FAISS.load_local("/Users/apple/Documents/coding/Langchain_Tutorial/chat_demo/faiss/", embeddings)
    db = FAISS.load_local(db_path[subject], embeddings)
    retriever = db.as_retriever(search_kwargs={'k': 3})
    context = retriever.get_relevant_documents(query)
    
    return context

def Query(context, query):
    system_prompt = SystemMessagePromptTemplate.from_template("你是一个乐于助人而且精通政治的助手.")
    # system_prompt = SystemMessage(content="You are a helpful assistent.")
    user_prompt = HumanMessagePromptTemplate.from_template("""根据下面的信息，直接回答问题不要附加任何前缀：
    
    信息：
    {context}
    
    问题: 
    {query}
    
    答案：
    """)

    user_prompt = user_prompt.format(context=context, query=query)
    full_chat_prompt = ChatPromptTemplate.from_messages([system_prompt,
                                                        #  MessagesPlaceholder(variable_name="chat_histroy"),
                                                         user_prompt])
    chat = OpenAI(temperature=0.9)
    # chain = (
    #     {
    #         "context": itemgetter("query") | retriever,
    #         "query": itemgetter("query"),
    #         # "chat_histroy": itemgetter("chat_histroy")
    #     }
    #     | full_chat_prompt | chat
    # )
    chain = full_chat_prompt | chat
    return chain.invoke({"query": query})

def remove_number_and_space(text):
    # 使用strip()方法去除字符串前后的空格
    text = text.strip()
    # 检查字符串是否以数字开头
    while text and text[0].isdigit():
        # 如果是数字，则去除该数字
        text = text[1:]
        text = text.strip()
    return text

def print_pretty(documents):
    document_dict = {}
    for document in documents:
        title = f'{document.metadata["source"].replace(".pdf", "").replace(r"./", "").strip()}\t{document.metadata["page"]}页'
        content = remove_number_and_space(document.page_content)
        document_dict[title] = content
    return document_dict

if __name__ == "__main__":
    read_pdf("./中国近代史纲要.pdf")
    # print(Query("剩余价值学说是什么？")[1].metadata)
    # documents = C("剩余价值学说是什么？")
    # for key, item in print_pretty(documents).items():
    #     print(key)
    #     print(item)
    # query = "剩余价值学说是什么？"
    # context = Context(query, "马克思主义基本原理")
    # msg = "答案出处：\n"
    # for document in context:
    #     title = f'{document.metadata["source"].replace(".pdf", "").replace(r"./", "").strip()}\t{document.metadata["page"]}页'
    #     msg = msg + title + "\n"
    # print(msg)
    # # answer = Query(context, query)
    # # print(answer)