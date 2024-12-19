import requests
response = requests.get(f'https://projects.fivethirtyeight.com/nba-player-ratings/')
response

import logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename='logfile.log', 
 format='[%(asctime)s][%(levelname)s] %(message)s',
 datefmt= '%y-%m-%d %H:%M',
 level= logging.INFO)

logger.info('Task.')

import pandas as pd
import sqlite3

# Create connection to database file
con = sqlite3.connect('NBA_Anthony.db')
# create dataframes
df = pd.read_csv('CollegeBasketballPlayers2009-2021.csv', index_col=False)
df = df[df.player_name.str.contains("Anthony")]
df.to_sql('NBA Sport', con, if_exists='replace')

df.info

import pytest 

def add_sixtyonethousands():
    return x + 62

def test_add_sixtyonethousands():
    assert add_sixtyonethousands(62)== 61062

import pytest

def add_fourhoundred(x):
    return x + 72

def test_add_fourhundred():
    assert add_fourhundred(72)==472

import logging
logging.basicConfig(
filename= 'VS-code', 
 format='[%(asctime)s][%(levelname)s] %(message)s',
 level= logging.DEBUG,
 datefmt= '%y-%m-%d %H:%M')

logger.debug('This is a debug-level log record.')
logger.info('This is an level log record.')
logger.warning('I have a bad feeling about this...')