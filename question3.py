import threading


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_thread(n):
    result = factorial(n)
    print(f"The factorial of {n} is: {result}")

# Main program
if __name__ == "__main__":
    # Read the integer input
    n = int(input("Enter an integer: "))

    # Create a thread for factorial calculation
    thread = threading.Thread(target=factorial_thread, args=(n,))

    # Start the thread
    thread.start()

    # Wait for the thread to finish
    thread.join()

    print("Factorial calculation completed.")
