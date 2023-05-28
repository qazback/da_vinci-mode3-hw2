import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problem = f"{x} + {y} = "

        for _ in range(3):
            answer = input(problem)
            try:
                answer = int(answer)
            except ValueError:
                print("EEE")
                continue

            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")

        else:
            print(f"Answer: {x + y}")

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level
        except ValueError:
            print("Please enter 1, 2, or 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
