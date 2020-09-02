from typing import Dict, Union


def get_coordinates(_text: str) -> Dict[str, int]:
    coordinates = {"x": 0, "y": 0, "z": 0}
    x = ""
    y = ""
    z = ""
    for i in range(_text.index("x: ") + 3, _text.index(",y:")):
        x = x + _text[i]
    coordinates["x"] = int(x)

    for i in range(_text.index("y: ") + 3, _text.index(",z:")):
        y = y + _text[i]
    coordinates["y"] = int(y)

    for i in range(_text.index("z: ") + 3, _text.index(")")):
        z = z + _text[i]
    coordinates["z"] = int(z)

    return coordinates


def get_event(event_text: str) -> Dict[str, Union[Dict[str, str], str, Dict[str, int]]]:
    arr = event_text.split(" ")
    hour = {"hours": arr[0][1] + arr[0][2], "minutes": arr[0][4] + arr[0][5]}

    event = {
        "time": hour,
        "player": arr[1],
        "inventoryType": arr[3],
        "coordinates": get_coordinates(event_text),
        "dimension": arr[9]}
    return event
