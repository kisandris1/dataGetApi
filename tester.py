import RequestData
import time

start = time.perf_counter()

print(len(RequestData.DiabAPIreq(username="test", collection="ohiodataset")))

endreq = time.perf_counter()
ms1 = (endreq - start)
print("done " + str(ms1))