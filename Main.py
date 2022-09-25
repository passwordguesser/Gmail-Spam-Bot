import smtplib
toaddrs = ''
fromaddrs = ''
message = ''
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('', '')
  for i in range(20):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)
