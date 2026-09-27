
"""Sample Google Ask Agent - v2: History tracking"""
class GoogleAskAgent:
    def __init__(self, name="AskAgent"):
        self.name = name
        self.history = []

    def ask(self, question: str) -> str:
        answer = f"[Google] Results for: {question}"
        self.history.append({"q": question, "a": answer})
        return answer

    def get_history(self):
        return self.history

if __name__ == "__main__":
    agent = GoogleAskAgent()
    print(agent.ask("What is Python?"))
    print(agent.get_history())
