# send-mail-with-python
Sending an email with python

-- The Login --

  server.login('your-mail', 'password')
    -->enter your mail
    -->when you activated the two-step verification you have to go to https://myaccount.google.com/apppasswords and login. 
       There you can create a password for the email service. Copy this and paste it into passwort
 
 
-- Fill in all fields (Subject, body)
s

-- Send the Mail

   server.sendmail('from-mail', 'to-mail', msg)
    -->here you have to replace "from-mail" with your own mail
       and to-mail with the mail you want to send the email to.
