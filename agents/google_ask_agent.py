
"""Sample Google Ask Agent - v1: Basic skeleton"""
class GoogleAskAgent:
    def __init__(self, name="AskAgent"):
        self.name = name

    def ask(self, question: str) -> str:
        """Ask a question (simulated Google search)."""
        return f"[Google] Results for: {question}"

if __name__ == "__main__":
    agent = GoogleAskAgent()
    print(agent.ask("What is Python?"))
