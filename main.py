import os
from utils.utils import get_yuotube_date, create_database, save_data_to_database
from config import config


def main():
    api_key = os.getenv('API_KEY')
    channel_ids = [
        'UC-OVMPlMA3-YCIeg4z5z23A',  # moscowpython
        'UCwHL6WHUarjGfUM_586me8w',  # highload
    ]
    params = config()

    data = get_yuotube_date(api_key, channel_ids)
    create_database('youtube', params)
    save_data_to_database(data, 'youtube', params)


if __name__ == '__main__':
    main()
