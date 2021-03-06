from typing import Dict, Union


def get_coordinates(_text: str) -> Dict[str, int]:
    coordinates = {"x": 0, "y": 0, "z": 0}
    x = ""
    y = ""
    z = ""
    try:
        for i in range(_text.index("x:") + 3, _text.index(",y:")):
            x = x + _text[i]

        coordinates["x"] = int(x)
    except ValueError:
        print("cant trnsform coordinates to integer insted got : %s" % x)

    try:
        for i in range(_text.index("y:") + 3, _text.index(",z:")):
            y = y + _text[i]

        coordinates["y"] = int(y)
    except ValueError:
        print("cant trnsform coordinates to integer insted got : %s" % y)
    try:
        for i in range(_text.index("z:") + 3, _text.index(")")):
            z = z + _text[i]

        coordinates["z"] = int(z)
    except ValueError:
        print("cant trnsform coordinates to integer insted got : %s" % z)
    return coordinates


def get_event(event_text: str) -> Dict[str, Union[Dict[str, str], str, Dict[str, int]]]:
    arr = event_text.split(" ")
    hour = {"hours": 00, "minutes": 00 }
    try:
        hour = {"hours": arr[0][1] + arr[0][2], "minutes": arr[0][4] + arr[0][5]}
    except IndexError:
        print("String too short when reading time")
    try:
        if event_text.index("InventoryOpenEvent") >= 0:
            event = {
                "time": hour,
                "player": arr[1],
                "inventoryType": arr[3],
                "coordinates": get_coordinates(event_text),
                "dimension": arr[9]}
    except IndexError:
        print("Its not an inventory event, so it cant be transformed into a dictionary")
        event = {
            "time": hour,
            "player": "null",
            "inventoryType": "null",
            "coordinates": "null",
            "dimension": "null"}
    except ValueError:
        print("Its not an inventory event, so it cant be transformed into a dictionary")
        event = {
            "time": hour,
            "player": "null",
            "inventoryType": "null",
            "coordinates": "null",
            "dimension": "null"}
    return event
