#!/usr/bin/python3
import cgitb
print("content-type:text/html\n\n")
cgitb.enable()

import datetime

now = datetime.datetime.now()

def toStep_30minutes(arg):
	return arg.replace(minute=(0 if arg.minute < 30 else 30), second=0, microsecond=0) 

print("""
<!DOCTYPE html>
<html lang="en">

	<head>
		<meta charset="UTF-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" href="css/main.css">
		<style>
			table.stdin,
			table.stdin tbody,
			table.stdin tr,

			table.stdin td {
				border: 0px;
			}

			:root {
				--stdin-input-width: 30rem;
				--stdin-input-height: 5rem;
			}

			table.stdin input:not([type="submit"]) {
				width: var(--stdin-input-width);
			}

			table.stdin textarea {
				width: var(--stdin-input-width);
				height: var(--stdin-input-height);
			}

			table.stdin td.data-invalid {
				border: 4px var(--red) !important;
			}
		</style>
		<title>TicketCreator</title>
		<script src="js/CookieUtil.js"></script>
		<script>
			let data = CookieUtil.getCookie()
		</script>
	</head>

	<body>
		<h1><a href="index.py">Main</a> / Create ticket</h1>
		<form action="createTicket_statusReport.py" method="POST">
			<table class="stdin">
				<tbody>
					<tr>
						<td>Name: </td>
						<td><input id="name" name="name" required /></td>
						<script>
							document.getElementById("name").value = data["username"]
						</script>
					</tr>
					<tr>
						<td>Phone number: </td>
						<td><input id="phoneNumber" name="phoneNumber" type="tel" /></td>
					</tr>
					<tr>
						<td>Company: </td>
						<td><input id="company" name="company" /></td>
					</tr>
					<tr>
						<td>Email: </td>
						<td><input id="email" name="email" type="email" required /></td>
					</tr>
					<tr>
						<td>Subject: </td>
						<td><input id="subject" name="subject" required /></td>
					</tr>
					<tr>
						<td>Problem description: </td>
						<td>
							<textarea id="problemDescription" name="problemDescription"
								required></textarea>
						</td>
					</tr>
					<tr>
						<td>Date and time for callback: </td>
						<td>
							<input id="timeForCallback" name="timeForCallback" type="datetime-local"
								min=""" + toStep_30minutes(now).isoformat() + """ step="1800" />
						</td>
					</tr>
					<tr>
						<td rowspan="2"><input type="submit"></td>
					</tr>
				</tbody>
			</table>
			
		</form>
	</body>
	<script>
		function toIsoString(date) {
			var tzo = -date.getTimezoneOffset(),
			dif = tzo >= 0 ? '+' : '-',
			pad = function(num) {
				var norm = Math.floor(Math.abs(num))
				return (norm < 10 ? '0' : '') + norm
			}

			return (
				date.getFullYear() +
				'-' + pad(date.getMonth() + 1) +
				'-' + pad(date.getDate()) +
				'T' + pad(date.getHours()) +
				':' + pad(date.getMinutes()) +
				':' + pad(date.getSeconds()) +
				dif + pad(tzo / 60) +
				':' + pad(tzo % 60)
			)
		}



		function sorted(arg) {
			for (let i = 0; i < arg.length; i++) {
				if (arg[i] > arg[i + 1]) {
					return false
				}
			}
			return true
		}

		const picker = document.getElementById("timeForCallback");

		let lastValidTimeForCallback = ""
		picker.addEventListener("focusout", function (e) {
			let chosenTime = new Date(this.value)
			let weekday = chosenTime.getDay()
			let smallTime = toIsoString(chosenTime).substring(11, 16)
			let mistakeHappened = false

			function onMistake(mistake) {
				e.preventDefault()
				picker.value = lastValidTimeForCallback
				mistakeHappened = true
				alert(mistake)
			}
			
			if ([0].includes(weekday)) {
				onMistake("Day can not be sunday.")
			} else if ([6].includes(weekday)) {
				if (!sorted(["08:00", smallTime, "13:00"])) {
					onMistake("Valid saturday time from 08:00 to 13:00.")
				}
			} else {
				if (!sorted(["08:00", smallTime, "20:00"])) {
					onMistake("Valid time from 08:00 to 20:00.")
				}
			}

			if (!mistakeHappened) {
				lastValidTimeForCallback = picker.value
			}

		})
	</script>

</html>
""")
