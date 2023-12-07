from dotenv import load_dotenv
from datetime import datetime
import os
import pandas as pd
import numpy as np

load_dotenv()

pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

rides_files_location = os.getenv("RIDES_FILES")


class Rides:

    def __init__(self):
        self.rides_files_location = rides_files_location

    def get_multiple_rows(self, gen_dt_rows):

        get_rides_data = pd.read_csv(self.rides_files_location)
        get_rides_data.columns = get_rides_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        get_rides_data = get_rides_data.replace({np.nan: None})

        get_rides_data['user_id'] = np.random.randint(0, 1000, size=(len(get_rides_data), 1))
        get_rides_data['dt_current_timestamp'] = str(datetime.now())
        get_rides_data['price'] = get_rides_data['price'].fillna(0)

        df = get_rides_data[['user_id', 'time_stamp', 'source', 'destination', 'distance', 'price', 'surge_multiplier', 'id', 'product_id', 'name', 'cab_type', 'dt_current_timestamp']].sample(int(gen_dt_rows))
        df_dict = df.to_dict('records')

        return df_dict
