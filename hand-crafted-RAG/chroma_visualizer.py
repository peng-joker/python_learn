import chromadb
import umap
import plotly.express as px
import pandas as pd
import numpy as np

# 连接到Chroma数据库
client = chromadb.PersistentClient(path="./chromaDbXiYouJi")  # 替换为您的数据库路径

# 获取集合列表
collections = client.list_collections()
print("可用集合:", [col.name for col in collections])

# 选择要可视化的集合
collection_name = "xiyouji"  # 替换为您的集合名称
collection = client.get_collection(collection_name)

# 获取所有向量和对应的元数据
results = collection.get(include=["embeddings", "metadatas", "documents"])
# 提取向量和元数据
embeddings = results["embeddings"]
metadatas = results["metadatas"]
documents = results["documents"]

print(f"检索到 {len(embeddings)} 个向量")

# 使用UMAP进行降维
reducer = umap.UMAP(n_components=3, random_state=42)
embedding_3d = reducer.fit_transform(embeddings)

# 准备可视化数据
df = pd.DataFrame({
    'x': embedding_3d[:, 0],
    'y': embedding_3d[:, 1],
    'z': embedding_3d[:, 2],
})
# print(metadatas)
# 添加元数据（如果有）
# if metadatas and len(metadatas) > 0:
#     print(metadatas[0])
#     for key in metadatas[0].keys():
#         df[key] = [meta.get(key, "") for meta in metadatas]

# 添加文档文本（如果有）
if documents and len(documents) > 0:
    df['document'] = documents

# 创建3D散点图
fig = px.scatter_3d(
    df,
    x='x',
    y='y',
    z='z',
    title=f"Chroma集合 '{collection_name}' 的向量可视化",
    hover_data=df.columns.tolist()  # 悬停时显示所有信息
)

# 更新布局
fig.update_layout(
    scene=dict(
        xaxis_title='UMAP 1',
        yaxis_title='UMAP 2',
        zaxis_title='UMAP 3'
    )
)

# 显示图形
fig.show()

# # 可选：保存为HTML文件
# # fig.write_html("chroma_visualization.html")
#
# # 使用UMAP进行2D降维
# reducer_2d = umap.UMAP(n_components=2, random_state=42)
# embedding_2d = reducer_2d.fit_transform(embeddings)
#
# # 准备2D可视化数据
# df_2d = pd.DataFrame({
#     'x': embedding_2d[:, 0],
#     'y': embedding_2d[:, 1],
# })
#
# # # 添加元数据和文档
# # if metadatas and len(metadatas) > 0:
# #     for key in metadatas[0].keys():
# #         df_2d[key] = [meta.get(key, "") for meta in metadatas]
#
# if documents and len(documents) > 0:
#     df_2d['document'] = documents
#
# # 创建2D散点图
# fig_2d = px.scatter(
#     df_2d,
#     x='x',
#     y='y',
#     title=f"Chroma集合 '{collection_name}' 的2D向量可视化",
#     hover_data=df_2d.columns.tolist()
# )
#
# fig_2d.show()