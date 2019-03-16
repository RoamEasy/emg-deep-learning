import os
import sys
from multiprocessing import Pool
from data_cleanup import CleanUp

#sudo rfcomm bind 0 00:06:66:66:97:57  ***
#sudo rfcomm bind 1 00:06:66:66:94:B3  ***
# ex to run: sudo python main_script.py word 50

processes = ('interface.py ' +sys.argv[1]+ ' '+sys.argv[2], 'exgSquareWave512Hz_1.py /dev/rfcomm0', 'exgSquareWave512Hz_2.py /dev/rfcomm1')

def run_process(process):
    os.system('sudo python {}'.format(process))

try:
    pool = Pool(processes=3)
    pool.map(run_process, processes)

except KeyboardInterrupt:
    pool.close()
    pool.join()
