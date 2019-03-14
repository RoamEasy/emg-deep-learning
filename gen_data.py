from data_cleanup import CleanUp
import os

def generate_data(subject):
    process = CleanUp(subject)
    processed = process.process_data()
    directory = 'data/subjects/'+subject+'/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    processed['data_final'].to_csv(directory + subject+'_final.csv', index = False)
    processed['random'].to_csv(directory + subject+'_random.csv', index = False)
    processed['streaming1'].to_csv(directory + subject+'_orignal1.csv', index = False)
    processed['streaming2'].to_csv(directory + subject+'_orignal2.csv', index = False)
    print('Data Cleaned up!')

if __name__ == '__main__':
    subject = raw_input("Enter Subject: ")
    generate_data(subject)
