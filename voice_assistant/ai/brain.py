"""
LLM brain - Language model interaction
"""
def generate_response(user_input):
    """
    Simulates AI response.

    Replace this later with real LLM (API or local model).
    """

    print("🤖 Thinking...")

    # Simple placeholder logic
    if "hello" in user_input.lower():
        return "Hello! How can I help you?"
    
    if "time" in user_input.lower():
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M')}"

    return "I didn't understand that, but I'm learning."
def generate_response(user_input):
    """
    Simulates AI response.

    Replace this later with real LLM (API or local model).
    """

    print("🤖 Thinking...")

    # Simple placeholder logic
    if "hello" in user_input.lower():
        return "Hello! How can I help you?"
    
    if "time" in user_input.lower():
        import datetime
        return f"The current time is {datetime.datetime.now().strftime('%H:%M')}"

    return "I didn't understand that, but I'm learning."