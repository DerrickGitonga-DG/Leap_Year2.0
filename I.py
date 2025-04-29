def show_history() -> None:
    print("\n=== Brief History of Python ===")
    print("=== Created in the year 1991 ===")
    print("=== Python 3 released in 2008 ===")
    print("=== Program that Computes the Average Score of Students ===")


def get_names_score() -> tuple[list[str], list[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

    names_of_students = []
    scores = []

    print("\nEnter student names and their scores:")

    for i in range(count):
        name = input(f"Student {i + 1} name: ").strip()
        if not name:
            name = f"Student {i + 1}"
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    return names_of_students, scores


# Main Program
show_history()
names, scores = get_names_score()

average = sum(scores) / len(scores)
print(f"\nAverage score of students: {average:.2f}")

# 📝 Optional: Display student list with scores
print("\n=== Student List with Scores ===")
for name, score in zip(names, scores):
    print(f"{name}: {score}")
