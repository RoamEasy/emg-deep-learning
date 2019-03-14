from data_cleanup import CleanUp
import os

class Update(object):

    def __init__(self,subject):
        self.subject = subject

    def generate_data(self):
        process = CleanUp(self.subject)
        processed = process.process_data()
        directory = 'data/subjects/'+self.subject+'/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        processed['data_final'].to_csv(directory + self.subject+'_final.csv', index = False)
        processed['random'].to_csv(directory + self.subject+'_random.csv', index = False)
        processed['streaming1'].to_csv(directory + self.subject+'_orignal1.csv', index = False)
        processed['streaming2'].to_csv(directory + self.subject+'_orignal2.csv', index = False)
        print('Data Cleaned up!')
