# utils/file_utils.py
import os
import pandas as pd

def make_path(file_path):
    """
    Creates the directory for the given file path if it doesn't exist.
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return file_path

def load_csv_from_url(url, local_path):
    """
    Downloads a CSV file from a URL and saves it locally.
    """
    try:
        df = pd.read_csv(url)
        df.to_csv(local_path, index=False)
        print(f"CSV file downloaded and saved locally at: {local_path}")
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None