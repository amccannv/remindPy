##
# This set of functions allows you to send emails or texts (through email)
# through your GMail account. It is useful for long programs or simulations
# when you may want to leave your computer and receive a notification when
# it has finished.
#
# example call:
#
# 	from SendEmail import sendMessage
#
# 	sendMessage('johnDoe', 'hunter2', 'janeDoe@gmail.com', 'Test Subject', 'Test Body')
#
# To send a text message, consider the following link:
# https://www.techwyse.com/blog/online-innovation/send-sms-through-email-to-usa-and-canada/
#
# example receiver for text notification:
#
# 	'9991234567@txt.bell.ca'
#
# Developed by Andrew McCann, 2016.
##


# Imports.
import smtplib
from email.mime.text import MIMEText

# Generate, encrypt, and login to GMail server.
def createServer(gmailUser, gmailPass):

	smtpserver = smtplib.SMTP(host = "smtp.gmail.com", port = 587)
	smtpserver.ehlo()
	smtpserver.starttls() # begins encrypted transport
	smtpserver.ehlo() # ehlo() ensures connection
	smtpserver.login(gmailUser, gmailPass)

	return smtpserver

# Create email object to send.
def createEmail(body, subject, sender, receiver):
	
	email = MIMEText(body)
	email['Subject'] = subject
	email['From'] = sender
	email['To'] = receiver

	return email

# Sends the message, call this function to send a reminder.
def sendMessage(gmailUser, gmailPass, receiver, subject = '', body):

	# Generate, encrypt, and login to GMail server.
	smtpserver = createServer(gmailUser, gmailPass)

	# Create email.
	email = createEmail(body, subject, gmailUser + '@gmail.com', receiver)

	# Send email and close connection.
	smtpserver.send_message(email)
	smtpserver.quit()