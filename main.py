from commands import handle_command
from voice import speak


def main():
    print("Hello! Hinata is ready.")
    print("Type 'exit' to close Hinata.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Hinata: Goodbye!")
            speak("Goodbye!")
            break

        response = handle_command(user_input)
        print(f"Hinata: {response}")
        speak(response)


if __name__ == "__main__":
    main()