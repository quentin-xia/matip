#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .command import Command


class Alert(object):
    """
    Allows to work with alerts.

    Use this class to interact with alert prompts.  It contains methods for dismissing, 
    accepting, inputting, and getting text from alert prompts.

    Accepting / Dismissing alert prompts::
    
        Alert(driver).accept()
        Alert(driver).dismiss()

    Inputting a value into an alert prompt:

        name_prompt = Alert(driver)
        name_prompt.send_keys("Willian Shakesphere")
        name_prompt.accept()


    Reading a the text of a prompt for verification:

        alert_text = Alert(driver).text
        self.assertEqual("Do you wish to quit?", alert_text)

    """

    def __init__(self, driver):
        """
        Creates a new Alert.

        :Args:
         - driver: The WebDriver instance which performs user actions.
        """
        self.driver = driver

    @property
    def text(self):
        """
        Gets the text of the Alert.
        """
        return self.driver.execute(Command.GET_ALERT_TEXT)["value"]

    def dismiss(self):
        """
        Dismisses the alert available.
        """
        self.driver.execute(Command.DISMISS_ALERT)

    def accept(self):
        """
        Accepts the alert available.

        Usage::
        Alert(driver).accept() # Confirm a alert dialog.
        """
        self.driver.execute(Command.ACCEPT_ALERT)

    def send_keys(self, keysToSend):
        """
        Send Keys to the Alert.

        :Args:
         - keysToSend: The text to be sent to Alert.

        
        """
        self.driver.execute(Command.SET_ALERT_VALUE, {'text': keysToSend})
