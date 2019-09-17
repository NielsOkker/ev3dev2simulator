import threading

from source.simulator.Main import main


class UserThread(threading.Thread):
    """
    Class representing the thread in which the user code runs.
    """


    def __init__(self, job_handler):
        threading.Thread.__init__(self)
        self.job_handler = job_handler


    def run(self):
        main(self.job_handler)
