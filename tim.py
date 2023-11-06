from tqdm import tqdm
import time
a=[3,4,22,78]
for i in tqdm(a):
    time.sleep(1)
print("for loop finished")