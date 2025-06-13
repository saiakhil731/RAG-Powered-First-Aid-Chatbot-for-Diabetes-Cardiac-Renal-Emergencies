# RAG-Powered-First-Aid-Chatbot-for-Diabetes-Cardiac-Renal-Emergencies
A Retrieval-Augmented Generation (RAG) chatbot for giving first-aid advice on diabetes, cardiac, and renal emergencies. Combines local knowledge and web search for accurate triage and response.
##  Setup
1. Install dependencies:
pip install -r requirements.txt

2. Prepare data:
Place your 60-sentence knowledge base in data/medical_snippets.csv

3. Build FAISS index:
from embedding_loader import build_index
build_index("data/medical_snippets.csv")

## Design Trade-offs
**Keyword-based triage:** fast, interpretable, but less nuanced than ML classification.
**FAISS index:** allows fast local retrieval, but corpus is small.
**Web search (Serper.dev):** adds freshness, but results may vary.
**Rule-based fusion:** prioritizes relevance but doesn’t learn from feedback.
**250-word generator:** clear and bounded, but lacks conversation memory.
