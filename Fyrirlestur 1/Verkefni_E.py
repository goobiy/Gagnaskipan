import sys

babel_dict = {}
output = []

for entry in sys.stdin:
    entry = entry.strip()

    if " " in entry:
        words = entry.split()
        babel_dict[words[1]] = words[0]
    else:

        if entry in babel_dict:
            output.append(babel_dict[entry])
        else:
            output.append("eh")

for i in output:
    print(i)