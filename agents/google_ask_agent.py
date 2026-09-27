
"""Sample Google Ask Agent - v3: Formatted results"""
from datetime import datetime
class GoogleAskAgent:
    def __init__(self, name="AskAgent"):
        self.name = name
        self.history = []

    def _format(self, question, results):
        ts = datetime.now().isoformat(timespec='seconds')
        return f"[{ts}] Google Search: '{question}' -> {results}"

    def ask(self, question: str) -> str:
        raw = f"Top 3 hits for '{question}' (simulated)"
        answer = self._format(question, raw)
        self.history.append({"q": question, "a": answer})
        return answer

    def get_history(self):
        return self.history
