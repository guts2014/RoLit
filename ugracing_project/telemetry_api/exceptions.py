__author__ = 'Vlad Iulian Schnakovszki'

# Using this because: http://stackoverflow.com/questions/1272138/baseexception-message-deprecated-in-python-2-6
class MyException(Exception):
    def _get_message(self):
        return self._message
    def _set_message(self, message):
        self._message = message
    message = property(_get_message, _set_message)