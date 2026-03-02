import datetime


class AIService:
    def __init__(self, ai_manager, history_manager):
        """
        Takes any AI manager and any History manager.
        This is called 'Dependency Injection'.
        """
        self.ai = ai_manager
        self.history = history_manager

    def ask(self, user_query):
        # 1. Logic: Check the specialist
        cached_answer = self.history.find_cached_answer(user_query)

        if cached_answer:
            return f"💡 (Cached) {cached_answer}"

        # 2. Logic: If miss, call the cloud
        try:
            completion = self.ai.call_api("user", user_query)
            response_text = completion.choices[0].message.content

            # 3. Logic: Tell history to save it
            log_entry = {
                "timestamp": str(datetime.datetime.now()),
                "prompt": user_query,
                "response": response_text,
                "usage": {"total_tokens": completion.usage.total_tokens}
            }
            self.history.add_entry(log_entry)

            return response_text

        except Exception as e:
            return f"❌ Service Error: {e}"
