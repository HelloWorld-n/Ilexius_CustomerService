#!/usr/bin/python3
import cgitb, cgi
import HtmlTableUtil
import pymysql
import datetime
import Connect

print("content-type:text/html\n\n")
cgitb.enable(logdir="./.logs.txt")

form = cgi.FieldStorage(environ={'REQUEST_METHOD':'POST'})

isAdminAccount = False

print("""
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="css/main.css">
		<style>
			table[main] {
				width: 90%;
			}

			textarea {
				width: 50rem;
				height: 10rem;
			}
		</style>
		<script src="js/CookieUtil.js"></script>
		<title>TicketCreator</title>
	</head>

	<body>
		<h1><a href="index.py">Main</a> / <a href="viewTickets.py">View tickets</a> / View Single ticket</h1>
""")
if True:
			db = Connect.connectSql()
			try:
			
				cursor = db.cursor()
				cursor.execute("USE db;")
				cursor.execute(
					(
						"SELECT * FROM tickets WHERE id = %s"
					),
					[
						form["id"].value,
					]
				)
				data = cursor.fetchall()

				try:
					cursor.execute(
						(
							"SELECT * FROM users WHERE ("
								"username = %s"
							") AND ("
								"password = %s"
							") AND ("
								"isAdmin = true"
							")"
						),
						[
							form["username"].value,
							form["password"].value,
						]
					)
					data = cursor.fetchall()
				except KeyError:
					data = []


				if form["submit"].value == "comment":
					if len(data) > 0:
						cursor.execute(
							"UPDATE tickets "
							"SET comment=%s "
							"WHERE id=%s",
							[form["comment"].value, int(form["id"].value.replace("/", ""))]
						)
						print("<h1 class=\"success\">Comment changed!</h1>")
					else:
						print("<h1 class=\"failure\">This account is not admin!</h1>")
				elif form["submit"].value in ["hide", "archive"]:
					if len(data) > 0:
						cursor.execute(
							"UPDATE tickets "
							"SET hidden=True "
							"WHERE id=%s",
							[int(form["id"].value.replace("/", ""))]
						)
						print("<h1 class=\"success\">Comment archieved!</h1>")
					else:
						print("<h1 class=\"failure\">This account is not admin!</h1>")
				
				cursor.execute(
					"SELECT * FROM tickets WHERE id=%s",
					form["id"].value
				)
				data = cursor.fetchall()

				for item in ["hidden"]:
					if item in data:
						data[item] = bool(data[item])

				for item in data:
					print(HtmlTableUtil.html_table(item, tableTags="main"))
				
				db.commit()
			except Exception as exception:
				db.rollback()
				print("<h1 class=\"failure\">There has been problem!</h1>")
				print(exception)
				db.close()

try: 
	db = Connect.connectSql()
	cursor = db.cursor()
	cursor.execute("USE db;")
	cursor.execute(
		(
			"SELECT * FROM users WHERE ("
				"username = %s"
			") AND ("
				"password = %s"
			") AND ("
				"isAdmin = true"
			")"
		),
		[
			form["username"].value,
			form["password"].value,
		]
	)
	db.rollback()
	db.close()
	data = cursor.fetchall()
	if len(data) > 0:

		isAdminAccount = True
		print("""
			<br>
			<form id="alter" method="post" action="viewSingleTicket.py">
				<input hidden name="id" value=""" + form["id"].value + """>
				<input hidden id="username" name="username">
				<input hidden id="password" name="password">
				<script> 

					let data = CookieUtil.getCookie()
					if(data["username"]){
						document.querySelectorAll("form#alter #username")[0].value = data["username"]
						document.querySelectorAll("form#alter #password")[0].value = data["password"]
					}
				</script>
				<div>
					<textarea name="comment"></textarea>
				</div>
				<div>
					<button type="submit" name="submit" value="comment" class="link-button">
						Comment!
					</button>
					<button type="submit" name="submit" value="hide" class="link-button">
						Archive!
					</button>
				</div>
			</form>
		""")
	else:
		"""
			Account is not admin.
		"""
except KeyError:
	"""
		Account is not even account.
	"""

if not isAdminAccount:
	print("""
		<br><br>
		<div>Current account is not admin.</div>
		<div>To alter data: <a href="logIn.py" onclick="CookieUtil.clearCookie()">Log in as admin.</a></div>
	""")
print("""
	</body>

</html>
""")
