import re
import numpy as np

class FusionRanker:
    def __init__(self, top_k=5):
        self.top_k = top_k

    def _normalize_scores(self, items, is_local=True):
        if not items:
            return []
        scores = np.array([score for _, score in items])
        if is_local:
            scores = 1 / (scores + 1e-6)
        scores /= scores.max()
        return [(items[i][0], scores[i]) for i in range(len(items))]

    def _keyword_boost(self, query, text):
        q_words = set(re.findall(r'\w+', query.lower()))
        t_words = set(re.findall(r'\w+', text.lower()))
        return len(q_words & t_words) / (len(q_words) + 1)

    def fuse(self, query, local, web):
        norm_local = self._normalize_scores(local, is_local=True)
        norm_web = [(doc['snippet'], 0.7) for doc in web]
        combined = norm_local + norm_web
        scored = [(text, score + 0.2 * self._keyword_boost(query, text)) for text, score in combined]
        return sorted(scored, key=lambda x: x[1], reverse=True)[:self.top_k]

