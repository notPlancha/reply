from pipeop import pipes
from typing import Callable
from pprint import pprint
from dataclasses import dataclass

# noinspection PyTypeChecker,PyArgumentList
@pipes
def pergunta1(lines: list[str]) -> list[str]:
    # vars
    T = int(lines[0])
    each = []
    for i in range(T):
        sec = lines[i*2+1].split(" ")
        third = lines[i*2+2].split(" ")
        each.append({
            "nFriends": sec[0] >> int(),
            "mDays": sec[-1] >> int(),
            "PnIntervals": third,
            "daysSets": []
        })
    out = []
    for caseC, case in enumerate(each):
        toOut = f"Case #{caseC+1}: "
        for friendInt in case["PnIntervals"]:
            currDay = 1
            friendSet = set()
            while currDay <= case["mDays"]:
                friendSet.add(currDay)
                currDay += friendInt >> int()
            case["daysSets"].append(friendSet)
        intersects = set.intersection(*case["daysSets"])
        toOut += intersects >> len() >> str()
        out.append(toOut)

        pprint(each)
    return out

@pipes
def pergunta2(lines: list[str]) -> list[str]:
    class target:
        def __init__(self, l):
            self.x = int(l[0])
            self.y = int(l[1])
            self.value = int(l[2])
    T = int(lines[0])
    lastLine = 1
    each = []
    for i in range(T):
        sec = lines[lastLine+1].split(" ") >> map(int) >> list()
        third = lines[lastLine+2].split(" ") >> map(int) >> list()
        M = sec[1]
        case = {
            "N": sec[0],
            "M": M,
            "startT": target(third)
            "othersT": [lines[lastLine+2+i].split(" ") >> target() for i in range(M+1)]
        }












# noinspection PyTypeChecker,PyArgumentList
@pipes
def main(func: Callable[[list[str]], list[str]], pergunta: str, inputFileName: str):
    with open(rf".\input\{pergunta}\{inputFileName}.txt", "r") as file:
        out: str = "\n".join(file.read().splitlines() >> func)
    with open(rf".\output\{pergunta}\{inputFileName}.txt", "w") as file:
        file.write(out)

if __name__ == "__main__":
    main(pergunta1, "1", "1")