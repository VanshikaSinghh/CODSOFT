#Chatbot in python
import re

class RuleBasedChatbot:
    def __init__(self):
        # Define patterns and responses
        self.rules = {
            r'\bhi\b|\bhello\b|\bhey\b': 'Hello! How can I help you today?',
            r'\bhow are you\b': 'Well, I\'m just a bot, but I\'m doing great! How can I help you?',
            r'\bwhat is your name\b': 'I do not have a name, I\'m a chatbot created to help you. What can I do for you?',
            r'\bbye\b|\bgoodbye\b': 'Goodbye! Have an awesome day!',
            r'\bwhat (is|are) (you|your) (name|age)\b': 'I don\'t have a name or age. I\'m here to assist you with your questions.',
            r'\bhelp\b': 'Sure, I can help you! What do you need assistance with?',
            r'\bcan you connect me with the delivery agency\b|\bcan you tell me my order details\b|\b tell me about my order\b|\border details\b': 'Sure, you will recieve a call on your registered phone number related to your query in a short while. Is there anything else?',
            r'\bno thank you\b|\bno\b|\bnope\b': 'Thank you for your patience and time, we will surely connect with you shortly.',
            r'\bwhen will my order arrive?\b|\bwhere is my order?\b': 'you can check everything you need to know about your order from our webiste in the orders section.Is there anything else?.',
            r'\bwhat is the return and exchange procedure?\b|\breturn and exchange policy\b|\bI need to return my product \b': 'As mentioned in our website, all our items are fresh eatables from stores.Hence they cannot be returned or exhanged.But we can arrange a refund if you received an expired or wrong product.Visit our website for more options or we will call you back shortly.Is there anything else?',
            r'\byes\b|\byeah\b|\byes please\b': 'Sure, what else can i help you with?',
        }
    
    def get_response(self, user_input):
        # Iterate through rules to find a match
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return response
        return 'I\'m sorry, I didn\'t understand that.'

def main():
    bot = RuleBasedChatbot()
    print("Chatbot: Hi! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if re.search(r'\bbye\b|\bgoodbye\b', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye! Have an awesome day !")
            break
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()