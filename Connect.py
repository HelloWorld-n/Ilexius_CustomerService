#!/bin/python3
import pymysql
import requests
import os


UPCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DOWNCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
BASIC_ALPHANUM = UPCASE + DOWNCASE + DIGITS

HOST = "127.0.0.1"
PORT = "3306"
SQL_USERNAME = "root"
SQL_PASSWORD = "myPassword"

def connectSql():
	return pymysql.connect(
		host=HOST, 
		port=int(PORT), 
		user=SQL_USERNAME,
		password=SQL_PASSWORD,
		cursorclass=pymysql.cursors.DictCursor
	)

			
