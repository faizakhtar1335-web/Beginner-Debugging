"""
Week 4 Task: Beginner Debugging and Error Identification
A small, interactive program demonstrating common beginner mistakes
and safer solutions.

Run:
    python beginner_debugging_examples.py
"""

def get_number(prompt: str) -> float:
    """Read a number safely, retrying when the input is invalid."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("That wasn't a number. Try again, for example: 12 or 4.5.")


def divide_numbers() -> None:
    """Demonstrate handling of division by zero."""
    print("\n--- Example 1: Division ---")
    numerator = get_number("Enter the number to divide: ")

    while True:
        denominator = get_number("Enter the divisor (not zero): ")
        if denominator != 0:
            break
        print("A number cannot be divided by zero. Please enter another divisor.")

    print(f"Result: {numerator / denominator:g}")


def calculate_average() -> None:
    """Calculate the average of three valid marks."""
    print("\n--- Example 2: Average of Three Marks ---")
    marks = []

    for subject in ("Maths", "Science", "English"):
        while True:
            mark = get_number(f"Enter {subject} marks (0-100): ")
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Marks must be between 0 and 100.")

    average = sum(marks) / len(marks)
    print(f"Average: {average:.2f}")

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Grade: {grade}")


def check_even_or_odd() -> None:
    """Demonstrate the correct use of the modulo operator."""
    print("\n--- Example 3: Even or Odd ---")
    number = int(get_number("Enter a whole number: "))

    # A number is even when the remainder after division by 2 is zero.
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")


def main() -> None:
    print("Beginner Debugging Examples")
    print("This program demonstrates input validation, safe division,")
    print("correct calculations, and conditional logic.")
    while True:
        print("\nChoose an example:")
        print("1. Safe division")
        print("2. Marks average and grade")
        print("3. Even or odd")
        print("4. Exit")

        choice = input("Your choice (1-4): ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            calculate_average()
        elif choice == "3":
            check_even_or_odd()
        elif choice == "4":
            print("Goodbye. Keep testing your code!")
            break
        else:
            print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
