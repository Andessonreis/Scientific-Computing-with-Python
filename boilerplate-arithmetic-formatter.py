# This entrypoint file to be used in development. Start by reading README.md
from pytest import main


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    top_line = ""
    bottom_line = ""
    answer_line = ""
    dash_line = ""

    for problem in problems:
        parts = problem.split()
        opr1 = parts[0]
        operator = parts[1]
        opr2 = parts[2]

        # verificar se o operador é válido
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # verificar quais operadores contêm dígitos
        if not opr1.isdigit() or not opr2.isdigit():
            return "Error: Numbers must only contain digits."

        # verificar se contém no máximo 4 dígitos
        if len(opr1) > 4 or len(opr2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # alinhar completamente o problema
        length = max(len(opr1), len(opr2)) + 2

        # montar as linhas
        top_line += opr1.rjust(length) + "   "
        bottom_line += operator + opr2.rjust(length - 1) + "   "
        dash_line += "-" * length + "   "

        if show_answers:
            if operator == '+':
                answer = str(int(opr1) + int(opr2))
            else:
                answer = str(int(opr1) - int(opr2))

            answer_line += answer.rjust(length) + "   "

    arranged_problems += top_line.rstrip() + "\n"
    arranged_problems += bottom_line.rstrip() + "\n"
    arranged_problems += dash_line.rstrip()

    if show_answers:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems


if __name__ == "__main__":
    #print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

    # Run unit tests automatically
    main(['-vv'])
