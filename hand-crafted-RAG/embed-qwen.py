from openai import OpenAI
import chunkLangChain
import chromadb

chromadb_client = chromadb.PersistentClient("./chromaDb")
chromadb_collection = chromadb_client.get_or_create_collection("joker")

def embed(text: str) -> list[float]:
    client = OpenAI(
        api_key="sk-4fba23d9bae24e29bd117d95071b2d18",  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 百炼服务的base_url
    )

    completion = client.embeddings.create(
        model="text-embedding-v4",
        input=text,
        dimensions=1024,# 指定向量维度（仅 text-embedding-v3及 text-embedding-v4支持该参数）
        encoding_format="float"
    )
    assert completion.data[0]
    assert completion.data[0].embedding
    return completion.data[0].embedding


def create_db() -> None:
    for idx, c in enumerate(chunkLangChain.get_chunks()):
        print(f"Process: {c}")
        embedding = embed(c)
        chromadb_collection.upsert(
            ids=str(idx),
            documents=c,
            embeddings=embedding
        )

def query_db(question: str) -> list[str]:
    question_embedding = embed(question)
    result = chromadb_collection.query(
        query_embeddings=question_embedding,
        n_results=5
    )
    assert result["documents"]
    return result["documents"][0]

def llm_query(content:str):
    client = OpenAI(
        api_key="sk-4fba23d9bae24e29bd117d95071b2d18",  # 如果您没有配置环境变量，请在此处用您的API Key进行替换
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 百炼服务的base_url
    )
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content},
        ],
        # Qwen3模型通过enable_thinking参数控制思考过程（开源版默认True，商业版默认False）
        # 使用Qwen3开源版模型时，若未启用流式输出，请将下行取消注释，否则会报错
        # extra_body={"enable_thinking": False},
    )
    assert completion.choices
    assert completion.choices[0]
    assert completion.choices[0].message
    assert completion.choices[0].message.content
    return completion.choices[0].message.content


if __name__ == '__main__':
    # create_db() # 只需要处理一次
    question = "令狐冲领悟了什么魔法？"
    chunks = query_db(question)
    prompt = "Please answer user's question according to context\n"
    prompt += f"Question: {question}\n"
    prompt += "Context:\n"
    for c in chunks:
        prompt += f"{c}\n"
    print(prompt)
    # 将向量数据库中找到的片段统一丢给LLM；之后统一返回前端
    print(llm_query(prompt))