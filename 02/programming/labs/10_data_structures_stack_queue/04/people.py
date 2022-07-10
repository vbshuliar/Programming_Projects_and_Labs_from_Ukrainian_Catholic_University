"""People."""


class Passenger:
    """Passenger."""

    def __init__(self, idNum, arrivalTime):
        """Initializes a passanger."""
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    def idNum(self):
        """Returns ID number."""
        return self._idNum

    def timeArrived(self):
        """Return arriving time."""
        return self._arrivalTime


class TicketAgent:
    """Ticket agent."""

    def __init__(self, idNum):
        """Initializes a ticket agent."""
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    def idNum(self):
        """Return ticket ID number."""
        return self._idNum

    def isFree(self):
        """Determines if the ticket agent is free to assist a passenger."""
        return self._passenger is None

    def isFinished(self, curTime):
        """Determines if the ticket agent has finished helping the passenger."""
        return self._passenger is not None and self._stopTime == curTime

    def startService(self, passenger, stopTime):
        """Indicates the ticket agent has begun assisting a passenger."""
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        """Indicates the ticket agent has finished helping the passenger."""
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
