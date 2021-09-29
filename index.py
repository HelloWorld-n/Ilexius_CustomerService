#!/usr/bin/python3
import cgitb
import CookieUtil
print("content-type:text/html\n\n")
cgitb.enable()

print("""
<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="css/main.css">
	<title>Hello, world!</title>
	<script src="js/CookieUtil.js"></script>
	<script>
		let data = CookieUtil.getCookie()
	</script>
</head>

<body>
	
	<h1 style="font-weight: 100;">Main</h1>
	<script>
		
		if(data["username"]){
			document.write(`
				<h2>Welcome, @${data["username"]}!</h2>
			`)
		}
	</script>
	<div><a href="createTicket.py">Create new ticket.</a></div>
	<div><a href="viewTickets.py">View existing tickets.</a></div>
	<script> 
		
		if(data["username"]) {
			document.write(`
				<div><a href="index.py" onclick="CookieUtil.clearCookie()">Log out.</a></div>
			`)
		} else {
			document.write(`
				<div><a href="createAccount.py">Create account.</a></div>
				<div><a href="logIn.py">Log in.</a></div>
			`)
		}
	</script>

	""")

print("""
</body>
</html>
""")
