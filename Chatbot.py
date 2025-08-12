def simple_chatbot():
    print("Hello!! I'm a Smiple Chatbot. \nHow can I help you today?")

    while True:
        user_input =input("You:")

        if "hello" in user_input:
            print("Chatbot: Hi there! \nHow can I assist you?")

        elif "Bye" in user_input:
            print("Chatbot: Goodbye!! Have a nice day")

        else:
            print("Chatbot: Sorry!! I'm Unavailable at this moment.")

simple_chatbot()