import smtplib
toaddrs = 'loic8400@gmail.com'
fromaddrs = 'Statue8166@gmail.com'
message = 'lol'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('', '')
  for i in range(20):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)
