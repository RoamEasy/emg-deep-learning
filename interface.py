from random import randint
import random
from time import sleep
import datetime
import csv
import sys


data_file = open('data/random.csv', mode='w')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(["Date_Time", "Target"])

sleep(10)

samples = int(sys.argv[1])

raw_input("Press Enter to continue...")

try:
    while samples != 0:
        print('relax')
        data_writer.writerow([datetime.datetime.now(), 'relax'])
        sleep(2)
        #rand_val = randint(0,9)
        rand_val = random.choice(['yes','no'])
        print(rand_val)
        data_writer.writerow([datetime.datetime.now(), rand_val])
        sleep(2)
        samples-=1
    data_writer.writerow([datetime.datetime.now(), 99])
    data_file.close()
    print('Done')
except KeyboardInterrupt:
    data_writer.writerow([datetime.datetime.now(), 99])
    data_file.close()
    print('Done')
