import os
import sys
from multiprocessing import Pool
from data_cleanup import CleanUp

#sudo rfcomm bind 0 00:06:66:66:94:B3  ***
#sudo rfcomm bind 1 00:06:66:66:97:57  ***

processes = ('interface.py ' +sys.argv[2], 'exgSquareWave512Hz_0.py /dev/rfcomm0', 'exgSquareWave512Hz_1.py /dev/rfcomm2')


def run_process(process):
    os.system('sudo python {}'.format(process))

try:

    pool = Pool(processes=3)
    pool.map(run_process, processes)

except KeyboardInterrupt:
    pool.terminate()
    pool.join()
    subject = sys.argv[1]
    data = CleanUp(subject)
    processed = data.process_data()
    directory = 'data/subjects/'+subject+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    processed['data_final'].to_csv('data/subjects/'+subject+'/'+subject+'_final.csv', index = False)
    processed['random'].to_csv('data/subjects/'+subject+'/'+subject+'_random.csv', index = False)
    processed['streaming1'].to_csv('data/subjects/'+subject+'/'+subject+'_orignal1.csv', index = False)
    processed['streaming2'].to_csv('data/subjects/'+subject+'/'+subject+'_orignal2.csv', index = False)
    print('Data Cleaned up!')
