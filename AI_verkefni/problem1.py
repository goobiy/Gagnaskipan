import sys
import datetime

def main():
    history = []
    new_history = {}

    current = -1  # index into history

    print("Browser ready. Commands: visit <page>, back, forward, quit")
    print("-" * 50)

    for line in sys.stdin:
        cmd = line.strip()
        if not cmd:
            continue

        parts = cmd.split(maxsplit=1)
        action = parts[0].lower()

        if action == "quit":
            break

        elif action == "visit":
            if len(parts) < 2:
                print("<error: no page specified>")
                continue
            page = parts[1]
            # visiting clears forward history
            current += 1
            history = history[:current]
            history.append(page)
            date = datetime.datetime.now()
            new_history[page] = date
            print(page)

        elif action == "back":
            if current <= 0:
                print("<error: no previous page to go back to>")
            else:
                current -= 1
                print(history[current])

        elif action == "forward":
            if current >= len(history) - 1:
                print("<error: no next page to go forward to>")
            else:
                current += 1
                print(history[current])
        elif action == "history":
            if not history:
                print("Error, no pages visited")
                continue
            seen = set()
            for pg in reversed(history):
                if pg not in seen:
                    seen.add(pg)
                    print(pg, new_history[pg])

        else:
            print(f"<error: unknown command '{action}'>")

if __name__ == "__main__":
    main()
# ```

# To run it interactively:
# ```
# python browser.py
# ```

# Or pipe in a file of commands:
# ```
# python browser.py < commands.txt