from textwrap import shorten

DISCLAIMER = (
    "⚠️ This information is for educational purposes only and is not a substitute for professional medical advice.\n\n"
)

class AnswerGenerator:
    def __init__(self, word_limit=250):
        self.word_limit = word_limit

    def extract_medicine(self, text):
        meds = []
        for word in ["glucose", "glucagon", "insulin", "aspirin", "nitroglycerin", "potassium"]:
            if word in text.lower():
                meds.append(word)
        return list(set(meds))

    def generate(self, query, condition, docs, web=None):
        evidence = "\n".join([f"- {shorten(doc[0], width=180)}" for doc in docs])
        all_text = " ".join([doc[0] for doc in docs])
        meds = self.extract_medicine(all_text)

        msg = DISCLAIMER
        msg += f"**Likely Condition:** {condition.title()}\n\n"
        msg += f"**First-Aid Steps:**\n{evidence}\n\n"
        if meds:
            msg += f"**Key Medicines:** {', '.join(meds)}\n\n"
        if web:
            links = [f"[{i+1}]({r['link']}) - {shorten(r['snippet'], 100)}" for i, r in enumerate(web)]
            msg += "**Citations:**\n" + "\n".join(links)

        return " ".join(msg.split()[:self.word_limit]) + "..."
