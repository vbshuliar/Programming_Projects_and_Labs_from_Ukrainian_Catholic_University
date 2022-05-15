"""The main module."""
from arrays import Array
from arrayqueue import ArrayQueue
from people import TicketAgent, Passenger
from random import random


class TicketCounterSimulation:
    """Ticket counter simulation."""

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """Initializes a class object."""
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self._passengerQ = ArrayQueue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """Runs."""
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)
        self.printResults()

    def _handleArrival(self, curTime):
        """Handles arrival."""
        time = random()
        if self._arriveProb > time:
            temp = Passenger(self._numPassengers, curTime)
            self._passengerQ.add(temp)
            self._numPassengers = self._numPassengers + 1

    def _handleBeginService(curTime):
        """Handles begin service."""
        

    def _handleEndService(curTime):
        """Handles end service."""
        pass

    def printResults(self):
        """Prints the results."""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("")
        print("Number of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)


if __name__ == "__main__":
    print(random())
