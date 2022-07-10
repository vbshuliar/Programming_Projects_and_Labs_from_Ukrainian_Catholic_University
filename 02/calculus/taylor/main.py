"""Taylor approximation module."""

from math import log, factorial
import matplotlib.pyplot as plt


def calculate(n, x):
    """Calculates."""
    r = 0
    try:
        for _ in range(-1, n):
            r += (((x - 1) ** (_)) * (-2) * ((log(2)) ** (1 + _))) / factorial(1 + _)
    except OverflowError:
        return "Too big inputs!"
    return r


def epsilon(e, x):
    """Finds n."""
    n, eq = 0, (2**x) / (1 - x)
    try:
        while True:
            if abs(calculate(n, x) - eq) <= e:
                return n
            n += 1
    except:
        return "Sorry. It cannot be found."


def get_number():
    """Gets number from user."""
    try:
        return float(input(">>> "))
    except ValueError:
        print("Wrong input!")
        return get_number()


def visualize(x):
    """Generates graph."""
    n = epsilon(10 ** (-3), x)
    dots, results = [], []
    for _ in range(n):
        dots.append(_)
        results.append(calculate(_, x))
    plt.plot(
        dots,
        results,
        color="black",
        linewidth=2,
        marker=".",
        markersize=10,
        markerfacecolor="grey",
    )
    plt.ylim(min(results), max(results))
    plt.xlim(1, n)
    plt.title(f"x = {x}")
    plt.xlabel("n")
    plt.ylabel("Value")
    plt.show()


if __name__ == "__main__":
    print("Enter x:")
    x = get_number()
    while x == 1:
        print("Division by zero. Try another number.")
        x = get_number()
    print("Enter n:")
    n = round(get_number())
    print(f"n = {n}: {calculate(n, x)}")
    print(f"n = 1: {calculate(1, x)}")
    print(f"n = 5: {calculate(5, x)}")
    print(f"n = 10: {calculate(10, x)}")
    print(f"n = 25: {calculate(25, x)}")
    print(f"n = 50: {calculate(50, x)}")
    print(f"10^(-1): n = {epsilon(10**(-1), x)}")
    print(f"10^(-3): n = {epsilon(10**(-3), x)}")
    print(f"10^(-6): n = {epsilon(10**(-6), x)}")
    print("Type anything to generate visualizer:")
    _ = input(">>> ")
    visualize(x)
