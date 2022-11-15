from typing import List

def checkio(game_result: List[str]) -> str:
    for i in range(3):
        if len(set(game_result[i])) == 1 and game_result[i][0] != ".":
            return game_result[i][0]

        if len(set([game_result[0][i],game_result[1][i],game_result[2][i]]  )) == 1 and game_result[0][i] != ".":
            return game_result[0][i]

    if len(set([game_result[0][0],game_result[1][1],game_result[2][2]]  )) == 1 and game_result[0][0] != ".":
        return game_result[0][0]
    if len(set([game_result[0][2],game_result[1][1],game_result[2][0]]  )) == 1 and game_result[0][2] != ".":
        return game_result[0][2]

    return "D"





if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["...","XXX","OO."]) == "X", "X wins"
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
