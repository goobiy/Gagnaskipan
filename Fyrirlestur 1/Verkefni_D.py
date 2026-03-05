
WINNER = "Jebb"
LOSER = "Neibb"


def check_row(line_1, line_2, line_3) -> bool:

    if "OOO" in line_1:
        return True
    if "OOO" in line_2:
        return True
    if "OOO" in line_3:
        return True
    
def check_column_and_diag(line_1, line_2, line_3) -> bool:
    
    if "O" in line_1[0] and "O" in line_2[0] and "O" in line_3[0]:
        return True
    elif "O" in line_1[1] and "O" in line_2[1] and "O" in line_3[1]:
        return True
    elif "O" in line_1[2] and "O" in line_2[2] and "O" in line_3[2]:
        return True
    elif "O" in line_1[0] and "O" in line_2[1] and "O" in line_3[2]:
        return True
    elif "O" in line_1[2] and "O" in line_2[1] and "O" in line_3[0]:
        return True
    else:
        return False

def main():

    line_1 = input()

    line_2 = input()
    
    line_3 = input()

    if check_row(line_1,line_2,line_3):
        print(WINNER)

    elif check_column_and_diag(list(line_1),list(line_2),list(line_3)):
        print(WINNER)

    else:
        print(LOSER)
    
main()