#!/bin/python3
import pymysql
import requests
import os


UPCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DOWNCASE = "abcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"
BASIC_ALPHANUM = UPCASE + DOWNCASE + DIGITS

HOST = "::1"
PORT = "3306"
SQL_USERNAME = "the_user"
SQL_PASSWORD = "the_pass"

def connectSql(
	host: str = HOST, 
	port: str = PORT, 
	username: str = SQL_USERNAME,
	password: str = SQL_PASSWORD,
):
	return pymysql.connect(
		host=host, 
		port=int(port), 
		user=username,
		password=password,
		cursorclass=pymysql.cursors.DictCursor
	)


			
