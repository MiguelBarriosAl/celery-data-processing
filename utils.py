import os.path

from dask import dataframe as dd
from datetime import date


def processing_data(name_file: str):
    today = date.today()
    data_input = f'data/{name_file}'
    data_output = 'data/output-{}.csv'.format(today)
    ddf = dd.read_csv(data_input)
    ddf_output = ddf.groupby(['Song', 'Date'])['Number_of_Plays'].sum().compute().reset_index() \
        .rename(columns={'Number_of_Plays': 'Number_of_Plays_for_Date'})
    try:
        if os.path.exists(data_output) is False:
            ddf_output.to_csv(data_output)
            print(f'CSV Saved in {data_output}')
        else:
            print(f'CSV already exists in {data_output}')
    except Exception as e:
        print("Error saving output file:", e)


def csv_to_json():
    filename = 'output'
    data_output = file_name_output(filename)
    ddf = dd.read_csv(data_output)
    df = ddf.compute()
    result = df.to_dict('records')
    return result


def file_name_output(filename) -> str:
    today = date.today()
    data_output = 'data/{}-{}.csv'.format(filename, today)
    return data_output
