#import required librarys
import logging
import threading
import time

#ask the user how many threads to run
while True:
    try:
        threadAmount = int(input("How many Threads? (1-8): "))
        break
    except:
        print("Enter a number stupid")

#define the number generating thread
def thread_function(name):
    logging.info("Thread %s: starting", name)
    #defines how to check if the card if valid using the Luhn Algorithm
    def checkLuhn(cardNo):
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False     

        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNo[i]) - ord('0')

            if isSecond:
                d = d * 2

            # We add two digits to handle
            # cases that make two digits after
            # doubling
            nSum += d // 10
            nSum += d % 10

            isSecond = not isSecond

        return (nSum % 10 == 0)
    def listtostring(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    cardNoArr = []
    counter = 0
    counter2 = 0
    #defines what ranges to use for each thread
    ave1 = [4000000000000000,4125000000000000,4250000000000000,4375000000000000,4500000000000000,4625000000000000,4750000000000000,4875000000000000]
    ave2 = [4125000000000000,4250000000000000,4375000000000000,4500000000000000,4625000000000000,4750000000000000,4875000000000000,5000000000000000]
    f = open("cards{}.txt".format(index), "a+")
    f.close()
    
    f = open("cards{}.txt".format(index), "r")
    
    

    #defines the start and endpoint of this particular thread by getting it from the array using the index variable
    lines = f.read().splitlines()
    try:
        startN = int(lastline)
        lastline = lines[-2]
    except:
        startN = int(ave1[index])
    endN = int(ave2[index])
    logging.info("Thread {0}: Start: {1}".format(index,startN))
    logging.info("Thread {0}: End: {1}".format(index,endN))
    #opens the cardfile for this particular thread
    cardfile = open("cards{}.txt".format(index), "a+")
    #starts to check card numbers using the range provided in startN and endN
    for cardNoint, _ in enumerate(range(startN,endN), start=startN):
        cardNo = str(cardNoint)
        if (checkLuhn(cardNo)):
            counter += 1
            if counter < 10000:
                cardNoArr.append(cardNo)
                cardNoArr.append("\n")
            else:
                cardfile.write(listtostring(cardNoArr))
                cardNoArr = []
    #logs when thread finishes
    logging.info("Thread %s: finished",index)

if __name__ == "__main__":
    #sets up some logging stuff
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    #runs the amount of threads defined by threadAmount
    threads = []
    for index in range(threadAmount):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
        time.sleep(1)
