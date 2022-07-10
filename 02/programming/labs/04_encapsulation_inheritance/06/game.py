"""Ternopil."""
from random import uniform, choice


class Person:
    """Person."""

    def __init__(self, name, street):
        """Receives information."""
        self.level = None
        self.name = name
        self.street = street

    def describe(self):
        """Returns description."""
        return print(
            f"""
--------------------
[> {self.name} <]
--------------------
{self.name} will let you cross the
{self.street} street only if you
{self.description}
"""
        )

    def link(self, level):
        """Links levels."""
        self.level = level

    def forward(self):
        """
        Forward.
        >>> lvl_4 = Python("Karpenko")
        >>> lvl_3 = Teacher("Myru", lvl_4)
        >>> lvl_2 = Dealer("Yunosti", lvl_3)
        >>> lvl_1 = Mathematician("Drahomanova", lvl_2)
        >>> current = lvl_1
        >>> current = current.forward()
        >>> current
        """
        return self.level


class Mathematician(Person):
    """Angry mathematician."""

    def __init__(self, street):
        """Receives information."""
        super().__init__("Angry Mathematician", street)
        self.description = "solve mathematical equation."

    def play(self):
        """Play."""
        x = round(uniform(5, 15))
        y = round(uniform(5, 15))
        z = choice(["+", "-", "*"])
        answer = eval(f"{x}{z}{y}")
        print(f"{x} {z} {y} = ?")
        thought = input(">>> ")
        if thought == str(answer):
            return True
        return False


class Dealer(Person):
    """Casino dealer."""

    def __init__(self, street):
        """Receives information."""
        super().__init__("Casino Dealer", street)
        self.description = "guess the right color on roulette (3 attempts)."

    def play(self):
        """Play."""
        attempts = 3
        colors = ["Blue", "Red"]
        while attempts > 0:
            print(f"Choose color: {colors}")
            decision = input(">>> ")
            correct = choice(colors)
            if decision == correct:
                return True
            print(
                f"Wrong! You have {attempts} more attempts. Right answer was {correct}.\n"
            )
            attempts -= 1
        return False


class Teacher(Person):
    """English teacher."""

    def __init__(self, street):
        """Receives information."""
        super().__init__("English Teacher", street)
        self.description = "correctly rewrite sentence without mistakes."

    def play(self):
        """Play."""
        first = choice(choice([["I"], ["He", "She", "It"], ["You", "We", "They"]]))
        if first == "I":
            second = choice(["is", "are"])
            correct = "I am"
        elif first in ["He", "She", "It"]:
            second = choice(["am", "are"])
            correct = f"{first} is"
        else:
            second = choice(["am", "is"])
            correct = f"{first} are"
        print(
            f"""Rewrite this sentence in a correct form.
{first} {second}"""
        )
        answer = input(">>> ")
        if answer == correct:
            return True
        return False


class Python(Person):
    """Evil python."""

    def __init__(self, street):
        """Receives information."""
        super().__init__("Evil Python", street)
        self.description = "answer a question about IT."

    def play(self):
        """Play."""
        questions = {
            "True": [
                "Python was firstly released in 1991",
                "There is a poem about Python",
                "Python is official Google programming language",
                "Python is similar to English",
                "Python initially was a hobby project",
            ],
            "False": [
                "Python was called because of the snake",
                "Python requires compiler",
                "Python needs braces to delimit code",
                "Functions cannot return multiple values",
                "Javascript influenced Python",
            ],
        }
        question = choice(choice(list(questions.values())))
        print(
            f"""Answer True or False:
{question}."""
        )
        answer = input(">>> ")
        if question in list(questions.get(answer)):
            return True
        return False


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
