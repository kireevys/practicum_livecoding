from math import floor


def addition(a: int, b: int) -> int:
    return a + b


def subtraction(a: int, b: int) -> int:
    return a - b


def division(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError


def multiplication(a: int, b: int) -> int:
    return a * b


def _splitter(inp: str, sign: str) -> (int, int):
    a, b = map(int, inp.split(sign))
    return a, b


def calculation_by_str(inp: str):
    if "+" in inp:
        a, b = _splitter(inp, "+")
        return addition(a, b)
    elif "-" in inp:
        a, b = map(int, inp.rsplit("-", 1))
        return subtraction(a, b)
    elif "/" in inp:
        a, b = _splitter(inp, "/")
        return int(floor(division(a, b)))
    elif "*" in inp:
        a, b = _splitter(inp, "*")
        return int(floor(multiplication(a, b)))
    else:
        raise ValueError


class Input:
    def ask(self, question: str) -> str:
        return input(question)


class Output:
    def out(self, str: str) -> None:
        return print(str)


def main(inputer: Input, outputer: Output):
    question = inputer.ask("Введите запрос: ")
    answer = calculation_by_str(question)
    outputer.out(f"Ответ: {answer}")


if __name__ == "__main__":
    main(Input(), Output())
