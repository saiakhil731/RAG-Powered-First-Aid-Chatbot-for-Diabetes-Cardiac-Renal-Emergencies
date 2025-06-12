import requests

class WebRetriever:
    def __init__(self, api_key, max_results=5):
        self.api_key = api_key
        self.max_results = max_results
        self.url = "https://google.serper.dev/search"

    def search(self, query):
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        data = {"q": query}
        response = requests.post(self.url, headers=headers, json=data)

        if response.status_code != 200:
            raise Exception(f"Serper API error: {response.status_code} — {response.text}")

        results = response.json().get("organic", [])[:self.max_results]
        return [
            {
                "title": r.get("title"),
                "snippet": r.get("snippet"),
                "link": r.get("link")
            } for r in results
        ]
