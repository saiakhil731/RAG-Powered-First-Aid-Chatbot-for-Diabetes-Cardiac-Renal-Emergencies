class TriageClassifier:
    def __init__(self):
        self.condition_keywords = {
            "hypoglycemia": ["shaky", "sweating", "sugar crashed", "< 70 mg", "glucometer"],
            "heart failure": ["swelling ankles", "shortness of breath", "heart failure"],
            "angina": ["angina", "nitroglycerin", "chest discomfort"],
            "acute kidney injury": ["creatinine", "urinated", "AKI"],
            "CKD": ["CKD", "chronic kidney"],
            "hyperkalemia": ["potassium", "6.1 mmol"],
        }

    def classify(self, user_input):
        user_input = user_input.lower()
        matches = {}
        for condition, keywords in self.condition_keywords.items():
            for word in keywords:
                if word in user_input:
                    matches[condition] = matches.get(condition, 0) + 1
        if not matches:
            return "unknown", {}
        return max(matches, key=matches.get), matches
