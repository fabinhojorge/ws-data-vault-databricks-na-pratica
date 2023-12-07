import os
import pandas as pd
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from datetime import datetime
from src.api.api_requests import Requests

load_dotenv()

size = 100
get_dt_rows = 100
blob_storage_conn_str = os.getenv("BLOB_STORAGE_CONNECTION_STRING")
container_landing = os.getenv("LANDING_CONTAINER_NAME")

params = {'size': size}


class BlobStorage(object):

    @staticmethod
    def write_into_landing_zone_json(entity):

        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day
        hour = datetime.today().hour
        minute = datetime.today().minute
        second = datetime.today().second
        file_name = entity + f'/{entity}_{year}_{month}_{day}_{hour}_{minute}_{second}.json'

        url_requests_api = {'user': 'https://random-data-api.com/api/users/random_user'}
        selected_url = url_requests_api[entity]

        dt_data = Requests.api_get_request(url=selected_url, params=params)
        print(file_name)

        pd_df_data = pd.DataFrame.from_dict(dt_data)
        pd_df_data['user_id'] = Requests().gen_user_id()
        pd_df_data['dt_current_timestamp'] = Requests().gen_timestamp()

        json_data = pd_df_data.to_json(orient="records").encode('utf-8')

        blob_service_client = BlobServiceClient.from_connection_string(blob_storage_conn_str)
        container_client = blob_service_client.get_container_client(container_landing)

        blob_client = container_client.get_blob_client(file_name)
        blob_client.upload_blob(json_data)

    @staticmethod
    def write_all():
        # list of all available urls to write
        # ingest dynamically by calling the first function
        urls_available = [
            'user',
            'restaurant',
            'vehicle',
            'stripe',
            'bank',
            'credit_card',
            'subscription',
            'company',
            'commerce',
            'computer',
            'device',
            'beer',
            'coffee',
            'food',
            'dessert']

        # init conditioner & counter
        count_list = len(urls_available)
        i = 0

        # loop to read all files within the received list
        # invoke function to go over xml files
        while i < count_list:

            # execute first function to ingest into minio storage
            # going over each item into the list
            # print(urls_available[i])
            BlobStorage().write_into_landing_zone_json(entity=urls_available[i])

            # finish count iterable
            i += 1


print(BlobStorage().write_into_landing_zone_json())