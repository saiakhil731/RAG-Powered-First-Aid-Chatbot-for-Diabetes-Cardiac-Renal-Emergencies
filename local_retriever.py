import faiss
import pickle
from sentence_transformers import SentenceTransformer

class LocalRetriever:
    def __init__(self, index_path='data/faiss_index', model_name='all-MiniLM-L6-v2'):
        self.index = faiss.read_index(index_path + '.index')
        with open(index_path + '.pkl', 'rb') as f:
            self.snippets = pickle.load(f)
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding, top_k)
        return [(self.snippets[i], distances[0][rank]) for rank, i in enumerate(indices[0])]
