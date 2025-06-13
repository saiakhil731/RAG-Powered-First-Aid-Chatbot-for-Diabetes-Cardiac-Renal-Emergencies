import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import pickle

def build_index(data_path='data/medical_snippets.csv', model_name='all-MiniLM-L6-v2'):
    df = pd.read_csv(data_path)
    snippets = df['Sentence'].tolist()

    model = SentenceTransformer(model_name)
    embeddings = model.encode(snippets, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, 'data/faiss_index.index')
    with open('data/faiss_index.pkl', 'wb') as f:
        pickle.dump(snippets, f)
