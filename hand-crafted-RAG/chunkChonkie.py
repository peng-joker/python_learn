# First import the chunker you want from Chonkie
from chonkie import TokenChunker

# Initialize the chunker
chunker = TokenChunker(
    tokenizer="gpt2",  # Default tokenizer (or use "gpt2", etc.)
    chunk_size=100,    # Maximum tokens per chunk
    chunk_overlap=20  # Overlap between chunks
) # defaults to using GPT2 tokenizer

# Here's some text to chunk
text = """
孙悟空又名孙行者，被花果山众猴尊为美猴王，玉帝封其为“齐天大圣”，有七十二般变化。
原是东胜神洲花果山一块仙石，受日精月华而迸裂成的天产石猴，被众猴推举为水帘洞主，称美猴王。求仙访道，遇须菩提祖师，取姓名为孙悟空。他从须菩提祖师处学到七十二变、分身法、筋斗云等神通。回花果山后，他又从龙宫索取得如意金箍棒，闹阴司又注销了自己和猴属的生死簿籍。太白金星奏准玉帝，对他两次招安，分授弼马温、齐天大圣之衔，但招安只为羁縻，他发现受骗后，两次大闹天宫，并声言“皇帝轮流做，明年到我家。”要玉皇让位，把前去围剿的天兵天将打得大败，后被西天如来佛祖用骗术和法力压他在五行山下受苦五百多年。后受观世音菩萨的规劝，皈依佛门，给唐僧做了大徒弟，又取名孙行者。他受过老君炉和五行山的锻炼，日趋成熟，西行途中不仅有武勇，还有更多智慧以制服妖怪。孙悟空带着紧箍，冒着不辨真伪的师父念紧箍咒的痛苦，保护着肉体凡胎的老和尚，与穷山恶水、妖魔鬼怪相斗，又不免要与取经集体内部师父的软善及猪八戒的挑唆斗争。一般的看，孙悟空的智斗妖魔，如钻肚皮战术，挖老根战术……等等虽难而易，不管怎样凶恶的敌手，最后总能战而胜之。他也有缺点，颇显清高，不善处理内部矛盾，有时不照顾师父的自尊心，又总是嘲弄猪八戒，就使得在猪八戒挑唆下，师父多念几遍紧箍咒，以至两次被驱逐。然而，孙悟空一往无前的精神，什么困难也吓不倒，常常主动找寻妖怪，讲拿几个妖怪玩玩的乐观气势，是取经大业终于成功的坚实保证。如来佛最后封他为“斗战胜佛”是最准确的论功而证得的大功果；他在小说结尾犹恨恨于什么菩萨捉弄人给自己头上戴紧箍，要取下砸碎。这一形象是在长期流传和几代作家创作中丰富发展，后由吴承恩完成的。宋代诗文和说话中已有猴行者的形象，其原型，或认为是淮涡水神无支祁，或认为受印度史诗《罗曼衍那》中神猴哈奴曼影响。
"""

# Chunk some text
chunks = chunker(text)

# Access chunks
for chunk in chunks:
    print(f"Chunk text: {chunk.text}")
    print(f"Token count: {chunk.token_count}")
    print(f"Start index: {chunk.start_index}")
    print(f"End index: {chunk.end_index}")