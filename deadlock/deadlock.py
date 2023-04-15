class Message:

    def __init__(self,initiator,_from,_to):
        self.initiator = initiator
        self._from = _from
        self._to = _to
    
    def toString(self):
        print("("+str(self.initiator)+","+str(self._from)+","+str(self._to)+")")

if __name__ == "__main__":

    n = int(input("Enter number of processes: "))

    print("Enter wait for graph")

    wait_for = []

    for i in range(n):
        k=[]
        for j in range(n):
            inp = int(input())
            k.append(inp)
        wait_for.append(k)
    
    print("Wait for graph")

    for i in wait_for:
        print(i)
    
    init = int(input("Enter the process initiating probe: "))

    dep = []

    for i in range(n):
        for j in range(n):
            if wait_for[i][j] == 1:
                dep.append(Message(init,i,j))
    deadlock = False

    for i in dep:
        i.toString()

    for i in dep:
        for j in dep:
            if i.initiator == j._to:
                deadlock = True
                break
        if deadlock:
            break
    
    if deadlock:
        print("deadlock detected")
    else:
        print("no deadlock detected")
