# Abstract LLM client. Replace implementation with your chosen provider.
class LLMClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    async def explain_step(self, problem_statement: str) -> str:
        # Return a simple stub explanation
        return "Think about adding the two numbers."

# Example factory (could read environment variables)
def get_llm_client():
    return LLMClient()
