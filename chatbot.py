import random
import re
import time

class SimpleChatbot:
    def __init__(self):
        self.name = "PyBot"
        self.responses = {
            r"hi|hello|hey": [
                "Hello there! How can I help you today?",
                "Hi! Nice to meet you. What's on your mind?",
                "Hey! How are you doing?"
            ],
            r"how are you": [
                "I'm doing well, thanks for asking! How about you?",
                "I'm great! How can I assist you today?",
                "All systems operational! What can I help with?"
            ],
            r"what is your name|who are you": [
                f"I'm {self.name}, your friendly Python chatbot!",
                f"My name is {self.name}. How can I assist you?",
                f"I go by {self.name}. What would you like to talk about?"
            ],
            r"bye|goodbye|exit": [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye for now! Come back soon!"
            ],
            r"thanks|thank you": [
                "You're welcome!",
                "Happy to help!",
                "Anytime! Need anything else?"
            ],
            r"weather": [
                "I can't check the weather yet, but I hope it's nice where you are!",
                "Would be great to tell you the weather, but I don't have those capabilities yet.",
                "Weather forecasting is beyond my current abilities, sorry!"
            ],
            r"help": [
                "I can chat about simple topics. Try asking me who I am, how I'm doing, or say hello!",
                "Need help? I'm a simple chatbot. I can respond to greetings and some basic queries.",
                "I'm here to chat! I respond to greetings, questions about myself, and goodbyes."
            ],
            r"joke": [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What's a computer's favorite snack? Microchips!",
                "Why did the Python programmer wear glasses? Because he couldn't C#!"
            ]
        }
        self.fallback_responses = [
            "Interesting! Tell me more about that.",
            "I'm not sure I understand. Could you rephrase that?",
            "That's something I haven't learned about yet.",
            "Let's talk about something else. Ask me about something simple!"
        ]

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for empty input
        if not user_input:
            return "It seems you didn't type anything. How can I help you?"
        
        # Check if input matches any pattern
        for pattern, responses in self.responses.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # Default fallback
        return random.choice(self.fallback_responses)

    def run(self):
        print(f"\n{self.name}: Hello! I'm {self.name}, your friendly chatbot. Type 'exit' to end our conversation.")
        
        while True:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ["exit", "bye", "goodbye"]:
                print(f"\n{self.name}: {random.choice(self.responses[r'bye|goodbye|exit'])}")
                break
                
            # Simulate "thinking" with a small delay
            print(f"\n{self.name} is typing", end="")
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="", flush=True)
            time.sleep(0.3)
            print()
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.run()