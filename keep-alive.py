import requests
import logging

url = 'https://scotty-webapp.onrender.com'
response = requests.get(url)
logging.info('Service called with response code {}'.format(response.status_code))