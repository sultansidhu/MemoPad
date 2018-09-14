"""

Represents the Class used to define the Node which is used in the LinkedList

****************************************************************
Author: Abhi Kapoor and Sultan Sidhu
Date: September 9, 2018
Location: University of Toronto
Purpose: Defines the Node class used as part of LinkedList
data structure
****************************************************************


"""

from typing import Union, Any
import Memo


class LLNode:
    """
    A Node to be used in a LinkedList.

    next - The successor to this LinkedListNode
    value - The data represented by this LinkedListNode.
    """

    next: Union["LLNode", None]
    value: object

    def __init__(self, value: "Memo",
                 next: Union["LLNode", None] = None) -> None:
        """
        Initialize this LinkedListNode with the value value and successor next.

        >>> LLNode(3).value
        3
        >>> LLNode(3).next is None
        True
        """

        self.value = value
        self.next = next

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedListNode.

        >>> print(LLNode(3))
        3 ->
        """
        return "{} -> ".format(self.value)

