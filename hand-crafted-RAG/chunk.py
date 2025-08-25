# chunk.py
def read_data() -> str:
    with open("西游记小说.txt", "r", encoding="utf-8") as f:
        return f.read()

# 分块函数
# 更加复杂的分块算法示例（有机会研究）
# https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html
def get_chunks() -> list[str]:
    content = read_data()
    chunks = content.split('\n\n')

    result = []
    header = ""
    for c in chunks:
        if c.startswith("#"):
            header += f"{c}\n"
        else:
            result.append(f"{header}{c}")
            header = ""

    return result


if __name__ == '__main__':
    chunks = get_chunks()
    for c in chunks:
        print(c)
        print("--------------")