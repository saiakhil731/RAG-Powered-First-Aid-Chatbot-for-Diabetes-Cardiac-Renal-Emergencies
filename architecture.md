#  Architecture Overview
## Components

1. **Triage Module**
   - Classifies condition from symptom text using keyword rules.

2. **Local Retriever**
   - Uses FAISS and Sentence Transformers to find relevant sentences.

3. **Web Retriever**
   - Calls Serper.dev (Google Search API) for real-time results.

4. **Fusion Ranker**
   - Combines local + web data and scores for relevance.

5. **Answer Generator**
   - Summarizes condition, first-aid steps, key medicines.

## Data Flow

                          User Query
                              ↓
                TriageClassifier (condition)
                              ↓
                LocalRetriever + WebRetriever
                              ↓
                FusionRanker (top docs)
                              ↓
          AnswerGenerator (final 250-word response)

## Example Tools Used

- Model: all-MiniLM-L6-v2 (Sentence Transformers)
- Search: Serper.dev API
- Indexing: FAISS FlatL2
