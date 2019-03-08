import os
import sys
from multiprocessing import Pool
from data_cleanup import CleanUp

processes = ('interface.py', 'exgSquareWave512Hz_1.py /dev/rfcomm0', 'exgSquareWave512Hz_2.py /dev/rfcomm1')

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
    complete,random, streaming1, streaming2 = data.process_data()
    complete.to_csv('data/subjects/'+subject+'/'+subject+'_final.csv', index = False)
    random.to_csv('data/subjects/'+subject+'/'+subject+'_random.csv', index = False)
    streaming1.to_csv('data/subjects/'+subject+'/'+subject+'_orignal1.csv', index = False)
    streaming2.to_csv('data/subjects/'+subject+'/'+subject+'_orignal2.csv', index = False)
    print('Data Cleaned up!')
