from langchain.text_splitter import RecursiveCharacterTextSplitter
def read_data() -> str:
    with open("data.md", "r", encoding="utf-8") as f:
        return f.read()
def get_chunks() -> list[str]:
    # 1️⃣ 定义示例文本（可替换为你自己的内容）
    # text = """
    # RAG（Retrieval-Augmented Generation）是将外部知识与大语言模型结合的一种技术方式，
    # 通过“先检索、再生成”的流程，让模型能结合知识库回答问题。
    # 而文本切分，就是其中的关键第一步。
    # """
    text = read_data()
    # 2️⃣ 初始化分块器（推荐配置）
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", "。"],  # 语义感知分段，自定义分割符
        chunk_size=500,   ## 最大长度，每段最大长度（字符数）
        chunk_overlap=100  ## 重叠长度，相邻 chunk 的重叠长度
    )
    # 3️⃣ 执行分块
    chunks = text_splitter.split_text(text)
    result = []
    # 4️⃣ 输出查看：前几个 chunk 结果
    # print(f"总共分成 {len(chunks)} 块：\n")
    for i, chunk in enumerate(chunks):
        result.append(f"{chunk}")
        # print(f"第 {i+1} 块内容：\n{chunk}\n{'-'*30}")
    return result

if __name__ == '__main__':
    chunks = get_chunks()
    for c in chunks:
        print(c)
        print("--------------")