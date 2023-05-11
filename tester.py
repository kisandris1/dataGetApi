import RequestData
import time
import pandas as pd

start = time.perf_counter()

data = RequestData.DiabAPIreq(username="test", collection="andersondataset")

endreq = time.perf_counter()
ms1 = (endreq - start)
print("done " + str(ms1))