import os
import sys
from multiprocessing import Pool
from data_cleanup import CleanUp

processes = ('interface.py', 'exgSquareWave512Hz_1.py /dev/rfcomm2')

def run_process(process):
    os.system('sudo python {}'.format(process))

try:
    pool = Pool(processes=2)
    pool.map(run_process, processes)

except KeyboardInterrupt:
    pool.terminate()
    pool.join()
    subject = sys.argv[1]
    data = CleanUp(subject)
    complete,random, streaming = data.process_data()
    complete.to_csv('data/subjects/'+subject+'/'+subject+'_final.csv', index = False)
    random.to_csv('data/subjects/'+subject+'/'+subject+'_random.csv', index = False)
    streaming.to_csv('data/subjects/'+subject+'/'+subject+'_orignal.csv', index = False)
    print('Data Cleaned up!')
