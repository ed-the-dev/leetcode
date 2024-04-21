from typing import List

def calPoints(operations: List[str]) -> int:

    record: list[str] = []

    for operation in operations:
        if operation == 'D':
            record.append(record[-1]*2)
        elif operation == 'C':
            record.pop()
        elif operation == '+':
            record.append(record[-1]+record[-2])
        else:
            record.append(int(operation))

    return sum(record)
            



print(calPoints(["5","-2","4","C","D","9","+","+"]))