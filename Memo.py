
"""
Represents the Class Memo, an instance of which represents a single Memo.
Contains the author's name, date created, list of comments, and the message itself as attributes

**********************************************************************
Author: Abhi Kapoor and Sultan Sidhu
Date: September 9, 2018
Location: University of Toronto
Purpose: Defines the Class to be used for Memo creation
**********************************************************************

"""

import datetime


class Memo:

    def __init__(self, message: str, author: str) -> None:
        """
        Creates a new Memo instance
        :param message: Represents the message stored by the Memo
        :param author: Represents the author of this Memo
        """

        self.message = message
        self.author = author
        self.comments_list = []
        self.date_created = self.get_date_and_time()[0]
        self.time_created = self.get_date_and_time()[1]

    def __str__(self):
        """
        Returns a user-friendly String representation of this Memo object
        :return: Str
        """

        return "Message: {} \n Created by: {} \n Date Created: {} \n Time Created: {} \n Comments: {}".format(self.message,
            self.author, self.date_created, self.time_created, self.comments_list)

    def get_date_and_time(self) -> list:
        """
        Obtains the current date from datetime library
        :return: List[str]
        """
        current_date = str(datetime.datetime.now()).split(" ")
        date = current_date[0].split("-")
        time = current_date[1].split(":")

        month = ""
        if date[1] == "01":
            month = "January"
        if date[1] == "02":
            month = "February"
        if date[1] == "03":
            month = "March"
        if date[1] == "04":
            month = "April"
        if date[1] == "05":
            month = "May"
        if date[1] == "06":
            month = "June"
        if date[1] == "07":
            month = "July"
        if date[1] == "08":
            month = "August"
        if date[1] == "09":
            month = "September"
        if date[1] == "10":
            month = "October"
        if date[1] == "11":
            month = "November"
        if date[1] == "12":
            month = "December"

        dateCreated = date[-1] + " " + month + " " + date[0]
        timeCreated = time[0] + " : " + time[1]

        return [dateCreated, timeCreated]









