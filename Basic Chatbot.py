import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot, nice to meet you!"]
    ],
    [
        r"how are you?|how you doing?|i am doing well,how about you?",
        ["I'm doing well, thanks for asking!", "I'm good, how about you?"]
    ],
    [
        r"sorry (.*)",
        ["No worries!", "No need to apologize"]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear!", "Wonderful!"]
    ],
    [
        r"(.*) age?",
        ["I'm an AI assistant. I don't have an age!", "As an AI, I don't have an age in the same way humans do."]
    ],
    [
        r"what (.*) want ?",
        ["I want to have a nice conversation with you!", "I want to help you however I can!"]
    ],
    [
        r"(.*) created you ?",
        ["I was created by Mubashira Kousar.", "Mubashira Kousar developed me."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm an AI assistant. I don't have a physical location.", "As software, I don't exist in a physical city."]
    ],
    [
        r"how is weather in (.*)?",
        ["I don't actually have information about the weather. I'm Claude, an AI assistant created by Anthropic to be helpful, harmless, and honest."]
    ],
    [
        r"i am doing internship in (.*)",
        ["%1 is a great company, I'm sure you're doing very interesting work!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day.", "Bye, it was nice talking to you!"]
    ],
    [
        r"(.*)",
        ["I'm afraid I don't understand. Could you please rephrase?", "I'm not sure I follow. Can you provide more details?"]
    ]
]

def chatbot():
    print("Hello! I'm Claude, an AI assistant created by Mubashira Kousar. How can I help you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()