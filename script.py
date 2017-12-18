import embeddings

emb = embeddings.EmbeddingsDictionary (250000)
#
# geek = emb.embed("geek")
# neighbors = emb.emb2neighbors(geek)
# for i in neighbors[1]:
#     print(emb.words[i])
#
# print('\n')
#
# Tokyo = emb.embed("Tokyo")
# neighbors = emb.emb2neighbors(Tokyo)
# for i in neighbors[1]:
#     print(emb.words[i])

print('\n')

emb.analogy('King', 'woman', 'man')
