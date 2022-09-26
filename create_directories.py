from datetime import datetime
import charlib
import os
import pandas as pd
import configparser


def create_one_dir():
    parent_dir = os.path.join(os.environ['MOGO_FOLDER'], 'GA', 'GA_S3')
    dir = 'test'
    path = os.path.join(parent_dir, dir)
    os.mkdir(path)

def create_multiple_dir():
    parent_dir = os.path.join(os.environ['MOGO_FOLDER'], 'GA', 'GA_S3')
    table_names = ['UAUTCDevice', 'UAUTCEvents', 'UAUTCGeography', 'UAUTCMobileDevices',
                   'UAUTCUsers', 'UAUTCPages', 'UAUTCSources', 'UAUTCTechnology',
                   'UAUTCTimestamp', 'UAUTCUserTypes', 'UAUTCEmailTrackerData', 'UAUTCUUID',
                   'UAUTCGender', 'UAUTCAge']

    for dir in table_names:
        path = os.path.join(parent_dir, dir)
        os.mkdir(path)


if __name__ == '__main__':
    start = datetime.now()
    print(f'Started at {start} with process id {os.getpid()}', flush=True)

    # create_one_dir()
    create_multiple_dir()



    print(f'Total time taken: {datetime.now() - start}', flush=True)
