import datetime
import requests
import csv

from data_phase.data_extraction import *
from data_phase.data_cleaning import *
######             EXTRACTION       #############
history = list_snapshots()
print(type(history))
print('history collected')
history[5000]
count = 0
for hour_data in range(5000, 5011):
    print(hour_data)
    result = collect_data(history[hour_data])
    create_csv(result)
    count += 1
    