#!/bin/python3
from http import cookies
import Connect
import requests

def generateCookie(key, value):
	cookie = cookies.SimpleCookie()
	cookie[key] = value.replace("\\", "\\\\").replace("\;", "\\s").replace("\"", "\\q")
	cookie[key]["path"] = "/"
	return cookie

def setCookie(obj) -> str:
	for key, value in obj.items():	
		cookie = generateCookie(key, value)
		print("""
			<script>
				document.cookie = \"""" + str(cookie) + """\"
			</script>
		""")

def parseCookieText(text):
	return text.replace("\\q", "\"").replace("\\s", ";").replace("\\\\", "\\")


if __name__ == "__main__":
	setCookie({"a": "x", "b": "y"})
