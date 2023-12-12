import RequestData
import time
import pandas as pd

start = time.perf_counter()

data = RequestData.DiabAPIreq(username="sotetestkey", collection="andersondataset")
print(len(data))
endreq = time.perf_counter()
ms1 = (endreq - start)
print("done " + str(ms1))

#1533127
#done 64.43663508400005
