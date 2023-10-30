#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class WeatherChatbot:
    def __init__(self):
        self.greetings = ["Hello! How can I help you with the weather?", "Hi there! What's your weather-related question?"]
        self.goodbyes = ["Thank you for using our weather service. Stay dry!", "Goodbye! Feel free to return if you have more weather questions."]

    def greet(self):
        print(random.choice(self.greetings))

    def say_goodbye(self):
        print(random.choice(self.goodbyes))

    def chat(self):
        self.greet()
        while True:
            user_input = input("You: ").lower()

            if "weather today" in user_input:
                print("Weather Chatbot: The weather today is sunny and clear. The temperature is around 25°C.")
            elif "umbrella" in user_input:
                print("Weather Chatbot: It's a good idea to bring an umbrella today, as there's a chance of rain.")
            elif "weather forecast" in user_input:
                print("Weather Chatbot: The weather forecast for the next few days is partly cloudy with occasional showers.")
            elif "weather in a different city" in user_input:
                print("Weather Chatbot: I'm currently providing weather information for this location only.")
            elif "tell a weather joke" in user_input:
                print("Weather Chatbot: Why did the weather report go to school? To get a little brighter!")
            elif user_input in ["bye", "exit", "quit"]:
                self.say_goodbye()
                break
            else:
                print("Weather Chatbot: I'm here to provide weather-related information. Ask me about the weather today, umbrella recommendations, or the weather forecast.")

# Create and start the chatbot
weather_chatbot = WeatherChatbot()

# Run the chatbot
weather_chatbot.chat()

