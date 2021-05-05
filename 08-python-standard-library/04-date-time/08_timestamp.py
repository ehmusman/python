import time

# timestamp
print(time.time())

def processing():
    for i in range(1000000):
        pass


start = time.time()
processing()
end = time.time()
difference = end - start
print(difference)