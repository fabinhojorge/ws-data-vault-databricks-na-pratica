from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np

load_dotenv()

payments_file_location = os.getenv("PAYMENTS_FILES")


class Payments:

    def __init__(self):
        self.user_file_location = payments_file_location

    def get_multiple_rows(self, gen_dt_rows):

        get_user_data = pd.read_csv(self.user_file_location)
        get_user_data.columns = get_user_data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(','').str.replace(')', '')
        get_user_data = get_user_data.replace({np.nan: None})

        user_output = get_user_data[
            [
                'user_id',
                'gender',
                'language',
                'race',
                'job_title',
                'city',
                'country',
                'currency',
                'currency_mode',
                'credit_card_type',
                'subscription_price',
                'time',
                'datetime'
            ]].head(int(gen_dt_rows))

        payments_list = user_output.to_dict('records')
        return payments_list
