from ChatDoctor_API.chat import generate_response

def main():

    print("=== ChatDoctor ===")

    role = input(
        "Role (patient/doctor): "
    )

    while True:

        query = input(
            "\nAsk a question: "
        )

        if query.lower() == "exit":
            break

        response = generate_response(
            query,
            role
        )

        print("\n", response)

if __name__ == "__main__":
    main()
