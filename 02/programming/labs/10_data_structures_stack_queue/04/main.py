"""The main module."""
from arrays import Array
from arrayqueue import ArrayQueue
from people import TicketAgent, Passenger
from random import random, seed


class TicketCounterSimulation:
    """Ticket counter simulation."""

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """Initializes a class object."""
        self._arriveProb = 1 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self._passengerQ = ArrayQueue()
        self._theAgents = Array(numAgents)
        self._totalWaitTime = 0
        self._numPassengers = 0
        for _ in range(numAgents):
            self._theAgents[_] = TicketAgent(_ + 1)

    def run(self):
        """Runs."""
        for _ in range(self._numMinutes + 1):
            self._handleArrival(_)
            self._handleBeginService(_)
            self._handleEndService(_)
        self.printResults()

    def _handleArrival(self, curTime):
        """Handles arrival."""
        random_time = random()
        if self._arriveProb > random_time:
            temp = Passenger(self._numPassengers, curTime)
            self._passengerQ.add(temp)
            self._numPassengers = self._numPassengers + 1

    def _handleBeginService(self, curTime):
        """Handles begin service."""
        while self._passengerQ.isEmpty() is False:
            for _ in self._theAgents:
                if _.isFree():
                    temp = self._passengerQ.pop()
                    self._totalWaitTime = (
                        self._totalWaitTime - temp.timeArrived() + curTime
                    )
                    _.startService(temp, curTime + self._serviceTime)
                    break
            break

    def _handleEndService(self, curTime):
        """Handles end service."""
        for _ in self._theAgents:
            if _.isFinished(curTime) is False:
                continue
            _.stopService()

    def printResults(self):
        """Prints the results."""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed
        print("\nNumber of passengers served = ", numServed)
        print("Number of passengers remaining in line = %d" % len(self._passengerQ))
        print("The average wait time was %4.2f minutes." % avgWait)


if __name__ == "__main__":
    seed(4500)
    TicketCounterSimulation(2, 100, 2, 3).run()
    TicketCounterSimulation(2, 10000, 2, 3).run()
    TicketCounterSimulation(2, 100, 2, 4).run()
    TicketCounterSimulation(3, 100, 2, 3).run()
