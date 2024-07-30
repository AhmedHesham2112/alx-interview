#!/usr/bin/python3
"""Lock Boxes"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    keysCollected = [0]
    for key in keysCollected:
        for boxKey in boxes[key]:
            if boxKey not in keysCollected and boxKey < len(boxes):
                keysCollected.append(boxKey)
    if len(keysCollected) == len(boxes):
        return True
    return False
