import strings
import printError
import sys

################################################################################
def main(inputFile):
    file = open(inputFile, "r")

    for line in file:
        line = line.strip() # Remove trailing '\n' escape character

        if line.upper() == "QUIT" \
        or line.upper() == "EXIT":
            file.close()
            sys.exit()
        else:
            result = Get_Triangle_Type(line)

        print(f"{result}")

    file.close()
################################################################################

################################################################################
def Get_Triangle_Type(line):
    list = line.split()    # Splits the input line into a list
    list.sort()             # Sorts the list elements ascendenly

    errorMsg = ""
    suggestion = strings.strings["SUGGESTION"]

    if 3 == len(list):      # We *might* have a triangle

        # Try to convert each list element to an integer
        try:
            side1 = float(list[0])
            side2 = float(list[1])
            side3 = float(list[2])
        except:
            result     = strings.strings["NOTRIANGLE"]
            errorMsg   = strings.strings["NOPOSITIVENUMBERS"]
            printError.printError(f"({line}): {errorMsg} {suggestion}")
            return result

        # Evaluale the triangle type based on the lengths of its sides
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            result = strings.strings["NOTRIANGLE"]
            errorMsg = strings.strings["NOPOSITIVENUMBERS"]

        elif side1 == side2 and side2 == side3:
            result = strings.strings["EQUILATERAL"]

        elif (side1 == side2 and side2 != side3) \
        or   (side1 != side2 and side2 == side3):
            result = strings.strings["ISOSCELES"]

        elif side1 != side2 and side2 != side3:
            result = strings.strings["SCALENE"]
    else:
        result   = strings.strings["NOTRIANGLE"]
        errorMsg = strings.strings["NOT3SIDES"]

    if "" != errorMsg:
        printError.printError(f"({line}): {errorMsg} {suggestion}")

    return result
################################################################################

################################################################################
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        printError.printError(f"Missing argument: input file")
        print(f"USAGE: {sys.argv[0]} <input_file>")
        sys.exit()
################################################################################