
"""Sample Google Ask Agent - v9: Logging + stats"""
import argparse, logging
from typing import List
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("ask_agent")

class GoogleAskAgent:
    """Ask Google (simulated), with cache, history and stats."""
    VERSION = "0.9.0"
    def __init__(self, name="AskAgent"):
        self.name = name
        self.history = []
        self._cache = {}

    def _simulate_results(self, question: str):
        base = question.strip().lower().replace(" ", "-")
        return [
            {"title": f"{question} - Overview", "url": f"https://example.com/{base}", "score": 0.95},
            {"title": f"{question} tutorial", "url": f"https://example.com/{base}-tutorial", "score": 0.82},
        ]

    def ask(self, question: str) -> str:
        log.info("ask: %s", question)
        if not question or not question.strip():
            raise ValueError("question must be non-empty")
        if question in self._cache:
            log.info("cache hit")
            return self._cache[question] + " (cached)"
        top = sorted(self._simulate_results(question), key=lambda x: x["score"], reverse=True)[0]
        answer = f"[v{self.VERSION}] Best: {top['title']} ({top['url']})"
        self._cache[question] = answer
        self.history.append({"q": question, "a": answer})
        return answer

    def ask_batch(self, questions: List[str]):
        return [self.ask(q) for q in questions]

    def stats(self):
        return {"queries": len(self.history), "cached": len(self._cache)}
