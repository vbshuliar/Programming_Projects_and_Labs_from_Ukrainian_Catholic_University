"""Parses KVED."""

import json


def parse_kved(class_code):
    """Parses KVED."""
    with open("kved_results.json", "w", encoding="UTF-8") as kved:
        json.dump(read_json(class_code), kved, ensure_ascii=False, indent=2)


def read_json(code):
    """Parses json file.
    >>> data = read_json("01.11")
    >>> data['type']
    'class'
    """
    with open("kved.json", "r", encoding="UTF-8") as kved:
        data = json.load(kved)
        for section in data["sections"]:
            for every in section:
                for division in every["divisions"]:
                    for group in division["groups"]:
                        for clas in group["classes"]:
                            if clas["classCode"] == code:
                                dkt = {
                                    "name": clas["className"],
                                    "type": "class",
                                    "parent": {
                                        "name": group["groupName"],
                                        "type": "group",
                                        "num_children": len(group["classes"]),
                                        "parent": {
                                            "name": division["divisionName"],
                                            "type": "division",
                                            "num_children": len(division["groups"]),
                                            "parent": {
                                                "name": every["sectionName"],
                                                "type": "section",
                                                "num_children": len(every["divisions"]),
                                            },
                                        },
                                    },
                                }
                                return dkt
        return -1


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
