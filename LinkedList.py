"""

Represents the Class used to define the LinkedList which is used to store Memo objects

********************************************************************
Author: Abhi Kapoor and Sultan Sidhu
Date: September 9, 2018
Location: University of Toronto
Purpose: Defines the LinkedList class used as a Data Structure
to store Memo objects
********************************************************************


"""

from typing import Union
from Memo import Memo
from LLNode import LLNode


class LinkedList:
    """
    Collection of LinkedListNodes.

    front - first node of this LinkedList
    back - last node of this LinkedList
    size - the number of nodes in this LinkedList (>= 0)
    """
    front: Union[LLNode, None]
    back: Union[LLNode, None]
    size: int

    def __init__(self) -> None:
        """
        Initialize an empty LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.size
        0
        """
        self.front = None
        self.back = None
        self.size = 0

    def prepend(self, value: "Memo") -> None:
        """
        Insert value to the start of this LinkedList (before self.front).

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """

        self.front = LLNode(value, self.front)
        if self.back is None:
            self.back = self.front
        self.size += 1

    def append(self, value: "Memo") -> None:
        """
        Insert value to the end of the LinkedList

        :param value: An object representing an individual Memo
        :return: None
        """

        if self.size == 0:
            new_node = LLNode(value, None)
            self.front = new_node
            self.back = new_node
            self.size += 1
        else:
            new_node = LLNode(value, None)
            self.back.next = new_node
            self.back = new_node
            self.size += 1

    def __str__(self) -> str:
        """
        Return a string representation of this LinkedList.

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> print(lnk)
        1 -> 0 -> |
        """

        cur_node = self.front
        result = ''
        while cur_node is not None:
            result += str(cur_node) + "\n"
            cur_node = cur_node.next
        return result + '|'

