'''JSON navigator.'''

import json
from twitter1 import tweets
from twitter2 import friends


def main():
    """The main function."""
    print("""
You are Welcome. Here you can navigate
through JSON file (especially from API).

Firstly, choose what you want to do:

1 - Analyze friends
2 - Analyze tweets
""")
    choice = input(">>>")
    while choice not in ['1', '2']:
        print("\nWrong input!\n")
        choice = input(">>>")
    print("\nEnter future JSON file name:\n")
    root = input(">>>")
    if root[-5:] == ".json":
        pass
    else:
        root = root + ".json"
    with open(root, 'w', encoding="UTF-8") as doc:
        if choice == "1":
            json.dump(friends(), doc, indent=2)
        else:
            json.dump(tweets(), doc, indent=2)
    json_navigate(root)
    return print("Finished.")


def json_navigate(root):
    """JSON navigation."""
    with open(root, 'r', encoding='UTF-8') as doc:
        info = json.load(doc)
        data = info
        while type(data) in [list, dict]:
            if len(data) > 0:
                decision = step(data)
                if decision == "again":
                    data = info
                    continue
                elif decision == "exit":
                    return print("\nThank you. Bye!\n")
                try:
                    data = data[decision]
                except (IndexError, KeyError, TypeError) as err:
                    print('\nWrong input! Try again.')
                    continue
            else:
                break
        return print(f'''
That's the last element:

{data}
''')


def step(data):
    """Decides what to do next."""
    if type(data) is dict:
        print(f'''
You are in a dictionary.
Type any key you want.

P.S.:"again" - restart
"exit" - stop running.
''')
        print('\n'.join(list(data.keys())))
    else:
        print(f'''
You are in a list.
Type any index you want.

P.S.:"again" - restart
"exit" - stop running.
''')
        for ind, each in enumerate(data):
            temp = each if len(f"{each}") < 40 else f"{f'{each}'[:40]}..."
            print(f"{ind} - {temp}")
    print()
    decision = input('>>>')
    if decision.isdigit():
        return int(decision)
    return decision


if __name__ == '__main__':
    main()
