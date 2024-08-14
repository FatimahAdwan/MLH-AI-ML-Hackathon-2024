from pieces_copilot_sdk.client import PiecesClient

client = PiecesClient(config = {"baseUrl":"http://localhost:1000"})

def main():
    print("Hello World")
    question = "What is a baby dog called?"
    try:
        response = client.ask_question(question)
        print(f"Question: {question}")
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error asking question: {e}")

if __name__ == "__main__":
    main()
