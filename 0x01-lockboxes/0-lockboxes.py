#!/usr/bin/python3
"""lockboxes method, pass positive intergers or get an error"""
from collections import deque


def canUnlockAll(boxes):
    """lockboxes method, pass positive intergers or get an error"""
    n = len(boxes)

    opened_boxes = set()

    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        opened_boxes.add(current_box)

        for key in boxes[current_box]:
            if 0 <= key < n and key not in opened_boxes:
                queue.append(key)

    return len(opened_boxes) == n
