
"""Sample Google Ask Agent - v7: Simple ranking"""
from datetime import datetime
from typing import List
class GoogleAskAgent:
    def __init__(self, name="AskAgent"):
        self.name = name
        self.history = []
        self._cache = {}

    def _simulate_results(self, question: str):
        # simulated ranked results
        base = question.strip().lower().replace(" ", "-")
        return [
            {"title": f"{question} - Overview", "url": f"https://example.com/{base}", "score": 0.95},
            {"title": f"{question} tutorial", "url": f"https://example.com/{base}-tutorial", "score": 0.82},
            {"title": f"{question} FAQ", "url": f"https://example.com/{base}-faq", "score": 0.71},
        ]

    def ask(self, question: str) -> str:
        if not question or not question.strip():
            raise ValueError("question must be non-empty")
        if question in self._cache:
            return self._cache[question] + " (cached)"
        results = self._simulate_results(question)
        top = sorted(results, key=lambda x: x["score"], reverse=True)[0]
        answer = f"Best: {top['title']} ({top['url']}) score={top['score']}"
        self._cache[question] = answer
        self.history.append({"q": question, "a": answer})
        return answer

    def ask_batch(self, questions: List[str]):
        return [self.ask(q) for q in questions]
