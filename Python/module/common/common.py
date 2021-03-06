"""
# common fonction for all
## credit
- Entat Baptiste
"""
import os
from typing import Union
import builtins


def input(msg="") -> str:
    """# debug fonction for pyteste"""
    return builtins.input(msg)


#entry section
def entry(returnType: str,
          failureMsg: str = "",
          blackList: list = ["", "isspace()"]) -> Union[int, str, bool]:
    """
    # entry
    returnType -> "int", "str", "bool", "char"
    failureMsg -> 
    blackList -> illegal char, "isspace()" -> all space
    - int -> just number
    - str -> all
    - bool -> "yes" "y" "Y" "oui" "Oui" "o" "O" ; "no" "n" "N" "non" "Non"
    - char -> just on char
    """
    if returnType != "int" and returnType != "str" and returnType != "bool" and returnType != "char":
        raise NotImplementedError("returnType specified are not implemented")
    while True:
        check = True
        buff = input()
        if returnType == "int":  #int
            for char in blackList:  #Check black list
                if char == "isspace()":
                    if buff.isspace() == True:
                        print(failureMsg)
                        check = False
                        break
                else:
                    if buff == char:
                        print(failureMsg)
                        check = False
                        break
            if check == False:
                continue
            try:
                int(buff)
            except:
                print(failureMsg)
                continue
            return int(buff)
        elif returnType == "str":  #str
            for char in blackList:  #Check black list
                if char == "isspace()":
                    if buff.isspace() == True:
                        print(failureMsg)
                        check = False
                        break
                else:
                    if buff == char:
                        print(failureMsg)
                        check = False
                        break
            if check == False:
                continue
            else:
                return buff
        elif returnType == "bool":  #bool
            for char in blackList:  #Check black list
                if char == "isspace()":
                    if buff.isspace() == True:
                        print(failureMsg)
                        check = False
                        break
                else:
                    if buff == char:
                        print(failureMsg)
                        check = False
                        break
            if check == False:
                continue
            if buff == "yes" or buff == "Yes" or buff == "y" or buff == "Y" or buff == "oui" or buff == "Oui" or buff == "o" or buff == "O":
                return True
            elif buff == "no" or buff == "No" or buff == "n" or buff == "N" or buff == "non" or buff == "Non":
                return False
            else:
                continue
        elif returnType == "char":  #char
            for char in blackList:  #Check black list
                if char == "isspace()":
                    if buff.isspace() == True:
                        check = False
                        break
                else:
                    if buff == char:
                        check = False
                        break
            if check == False:
                print(failureMsg)
                continue
            if len(buff) != 1:
                print(failureMsg)
                continue
            else:
                return buff

        else:
            raise NotImplementedError()


#clear screen
def cls():
    """
    clear console
    - Window and Linux supported
    """
    os.system('cls' if os.name == 'nt' else 'clear')
