
"""Sample Google Ask Agent - v5: Error handling"""
from datetime import datetime
class GoogleAskAgent:
    def __init__(self, name="AskAgent"):
        self.name = name
        self.history = []
        self._cache = {}

    def _format(self, question, results):
        ts = datetime.now().isoformat(timespec='seconds')
        return f"[{ts}] Google Search: '{question}' -> {results}"

    def ask(self, question: str) -> str:
        if not question or not question.strip():
            raise ValueError("question must be non-empty")
        try:
            if question in self._cache:
                return self._cache[question] + " (cached)"
            raw = f"Top 3 hits for '{question.strip()}' (simulated)"
            answer = self._format(question, raw)
            self._cache[question] = answer
            self.history.append({"q": question, "a": answer})
            return answer
        except Exception as e:
            return f"[Error] {e}"
