import os
import pandas as pd
from time import sleep, gmtime, strftime
from random import randint
from itertools import cycle

NUM_FILES = 120
DELAY_SECONDS = 1
COUNTS_PER_FILE = 2

data_path = os.path.join(os.getcwd(), "..", "data")
streamtest_path = os.path.join(data_path, "streamtest")

loading_spinner_symbols = ['/','-','\\','|']
spinner = cycle(loading_spinner_symbols)

print("generating...")
for i in range(NUM_FILES):
    randomness_scaler = 1 - abs((i/NUM_FILES) - 0.5)
    df = pd.DataFrame({
        "data_value" : [randint(500, 1000) * randomness_scaler for j in range(COUNTS_PER_FILE)],
        "timestamp" : [strftime("%Y-%m-%d %H:%M:%S", gmtime()) for j in range(COUNTS_PER_FILE)]
    })
    df.to_csv(os.path.join(data_path, f"streamfile{i}.csv"), index=False)
    os.replace(os.path.join(data_path, f"streamfile{i}.csv"), os.path.join(streamtest_path,f"streamfile{i}.csv"))
    print(f"{next(spinner)}", end='\r')
    sleep(DELAY_SECONDS)
print("done!")