import pandas as pd
import sys
import os

class CleanUp(object):

    def __init__(self, subject):
        self.subject = subject

    def generate_data(self, processed):
        directory = 'data/subjects/'+self.subject+'/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        processed['data_final'].to_csv(directory + self.subject+'_final.csv', index = False)
        processed['random'].to_csv(directory + self.subject+'_random.csv', index = False)
        processed['streaming1'].to_csv(directory + self.subject+'_orignal1.csv', index = False)
        processed['streaming2'].to_csv(directory + self.subject+'_orignal2.csv', index = False)
        print('Data Cleaned up!')

    def process_data(self):
        '''
        :parameter: streaming: takes streaming data after new datetime column is added
        :parameter: random: takes random number data after new datetime column is added
        :return: dataframe that merges target and streaming dataframe
        '''
        streaming1= pd.read_csv('data/streaming1.csv')
        streaming2= pd.read_csv('data/streaming2.csv')
        random = pd.read_csv('data/random.csv')
        streaming1['New_Date_Time'] = streaming1['Date_Time'].str[:21]
        #streaming2['New_Date_Time'] = streaming2['Date_Time'].str[:22]
        random['New_Date_Time'] = random['Date_Time'].str[:21]

        merged = pd.merge(streaming1,random, how = 'left', left_on = 'New_Date_Time', right_on = 'New_Date_Time')
        merged['Target'] = merged['Target'].ffill()
        merged.dropna(subset=['Target'], inplace = True)
        merged = merged[merged.Target != '99']
        merged = merged[['Date_Time_x', 'CH_1_mV', 'CH_2_mV', 'New_Date_Time','Target']]
        merged.reset_index(inplace = True, drop = True)

        # convert to datetime
        merged['Date_Time'] = pd.to_datetime(merged['Date_Time_x'])
        merged.drop(['Date_Time_x'], inplace =True, axis = 1)
        merged['Subject'] = self.subject
        merged = merged[['Subject','Date_Time', 'CH_1_mV', 'CH_2_mV','Target']]

        streaming2['Date_Time'] = pd.to_datetime(streaming2['Date_Time'])
        # select max and min timestamps from data
        mask = (streaming2['Date_Time'] >= merged['Date_Time'].min()) & (streaming2['Date_Time'] <= merged['Date_Time'].max())
        streaming2_update = streaming2.loc[mask]
        streaming2_update.reset_index(inplace = True, drop = True)
        streaming2_update = streaming2_update.drop(['Date_Time'], axis = 1)

        #Concatenate both data from streaming
        data_final = pd.concat([merged, streaming2_update], ignore_index = False, axis =1 ).fillna('NA')
        data_final = data_final[['Subject','Date_Time', 'CH_1_mV', 'CH_2_mV','CH_3_mV', 'CH_4_mV','Target']]

        #data_final
        ret = {'data_final': data_final, 'random': random, 'streaming1':streaming1, 'streaming2': streaming2}

        return ret
