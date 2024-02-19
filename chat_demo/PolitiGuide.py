import streamlit as st
from openai import OpenAI
from main import Query, Context
from streamlit_modal import Modal

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    subject = st.selectbox("学科：", ["马克思主义基本原理", "毛泽东思想和中国特色社会主义理论体系概论", "思想道德与法治", "中国近代史纲要", "全学科"], key="theme")

st.title("📚 PolitiGuide")
# st.title(subject)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "可以问我一切关于政治的内容。"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])



if prompt := st.chat_input(placeholder="剩余价值学说的概念是什么？"):
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt) 
    context = Context(prompt, subject)
    
    msg = "答案出处："
    for document in context[:-1]:
        title = f'《{document.metadata["source"].replace(".pdf", "").replace(r"./", "").strip()}》{document.metadata["page"]}页'
        msg = msg + title + "、" 
    msg = msg + f'《{context[-1].metadata["source"].replace(".pdf", "").replace(r"./", "").strip()}》{context[-1].metadata["page"]}页。'
    st.chat_message("assistant").write(msg)
    ans = Query(context, prompt)
    # msg = msg + "[显示原文](http://localhost:8502/Contexts)"
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(ans)

