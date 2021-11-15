from typing import List


def checkio(game_result: List[str]) -> str:

    for i in range(3):
        if sum(game_result[i]) == 3:
            return "X"
        elif sum(game_result[i]) == 30:
            return "0"
        if sum(game_result[i][j] for j in range(3)) == 3:
            return "X"
        elif sum(game_result[i][j] for j in range(3)) == 30:
            return "0"
    
    if game_result[0][0] + game_result[1][1] + game_result[2][2] == 3:
        return "X"
    if game_result[0][0] + game_result[1][1] + game_result[2][2] == 30:
        return "0"
    if game_result[0][2] + game_result[1][1] + game_result[0][2] == 3:
        return "X"
    if game_result[0][2] + game_result[1][1] + game_result[0][2] == 30:
        return "0"

    return "D"


if __name__ == "__main__":
    print("Example:")
    print(checkio(["X.O", "XX.", "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "X wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "O wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "X wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
