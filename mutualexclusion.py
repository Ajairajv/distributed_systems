import threading
import time

class CriticalSection:
    def __init__(self):
        self.sem = threading.Semaphore()
    def process_1(self):
        while True:
            print("Process 1: Entry section")
            self.sem.acquire()
            self.critical_section()
            self.sem.release()
            print("Process 1: Critical section over")
            time.sleep(3)
    def process_2(self):
        while True:
            print("Process 2: Entry section")
            self.sem.acquire()
            self.critical_section()
            self.sem.release()
            print("Process 2: Critical section over")
            time.sleep(3)
    def critical_section(self):
        print("Entered critical section! Performing operation on shared resource...")
    def main(self):
        t1 = threading.Thread(target=self.process_1)
        t1.start()
        t2 = threading.Thread(target=self.process_2)
        t2.start()
if __name__ == "__main__":
    c = CriticalSection()
    c.main()
