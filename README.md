# DEMO

+ 基于RAG任务的考研政治问答系统[PoliticGuide](https://github.com/ustbChengzhao/Langchain_Tutorial/tree/main/PoliticGuide)
+ 邮件格式、语气一键调整系统[Convert Email](https://github.com/ustbChengzhao/Langchain_Tutorial/tree/main/Convert_email)

# Langchain Tutorial

这个仓库包含了一系列Jupyter笔记本，记录了我学习Langchain的过程。每个笔记本都用关键词简要描述，以便于快速复习和参考。

## 第1部分：Model I/O

- [1. Quickstart.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/1.%20quickstart.ipynb): Models、Prompt、Output paesers、Chain
- [1.1 Model IO---Quickstart.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/1.1%20Model%20IO---Quickstart%20.ipynb): Models、Prompt、Output paesers、Chain
- [1.2 Prompt.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/1.2%20Prompt.ipynb): 普通模版PromptTemplate、模版融合Prompt Composition、实例选择题Example Selecttor、部分补全模版Partial prompt templates、Pipeline Prompt
- [1.3 Chat Models.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/1.3%20Chat%20Models.ipynb): 对话Messages、聊天推理、缓存、函数调用
- [1.4 LLMs.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/1.4%20LLMs.ipynb): LLMs同1.3
- [1.5 Output Parser.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/1.5%20Output%20parser.ipynb): CSV、JSON数据解析器

## 第2部分：Retrieval

- [2.1 Document Loader.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/2.1%20Document%20Loader.ipynb): CSV、PDF、JSON文档加载
- [2.2 Text Splitters.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/2.2%20Text%20Splitters.ipynb): 文本分割
- [2.3 Embeddings.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/2.3%20Embeddings.ipynb): 词嵌入技术
- [2.4 Vector Store.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/2.4%20Vector%20Store.ipynb): 词嵌入向量数据库
- [2.5 Retrievers.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/2.5%20Retrievers.ipynb): 词嵌入向量相关度匹配、文档内容检索
- [2.7 Index.ipynb](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/2.7%20Index.ipynb): 内容建立索引，防止重复写入

## 第3部分：LCEL

+ [3.1 RunnableParallel](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/3.1RunnableParallel.ipynb)：处理Runnable的数据，将一个Runnable的输出匹配下一个Runnable的输入格式
+ [3.2 RunnablePassthrough](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/3.2%20RunnablePassthrough.ipynb)：RunnablePassthrough可以获取用户的输入，同时可以在用户的输入上添加额外的键值对
+ [3.3 RunnableLambda](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/3.3%20RunnableLambda.ipynb)：运行自定义函数
+ [3.4 RunnableBranch](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/3.4%20RunnableBranch.ipynb)：动态路由，创建非确定性链，由上一步的输出决定下一步

## 第4部分：Agent

+ [4.0 Agent Quickstart](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/4.0%20Agent%20Quickstart.ipynb)：搭建网路搜索+检索Agent
+ [4.1 Custom agent](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/4.1%20Custom%20agent.ipynb)：自定义Agent
+ [4.2 Definning Custom Tools](https://github.com/ustbChengzhao/Langchain_Tutorial/blob/main/langchain_tutorial/4.2%20Definning%20Custom%20Tools.ipynb)：自定义Tools
