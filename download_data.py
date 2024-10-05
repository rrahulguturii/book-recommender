Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # download_data.py
import os
import requests
import pickle

def download_and_save_data(url, filename):
  """Downloads data from the given URL and saves it to a file."""
  response = requests.get(url)
  with open(filename, 'wb') as f:
    f.write(response.content)

  # Load the downloaded data (optional)
  with open(filename, 'rb') as f:
    data = pickle.load(f)
  return data

# Example usage in app.py
from download_data import download_and_save_data

books_pkl_url = os.environ.get('BOOKS_PKL_URL')
download_and_save_data(books_pkl_url, 'books.pkl')