import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)

ob.ehlo()
ob.starttls()
ob.login('pratigyapandey345@gmail.com','******')
subject = 'test python'
body = 'Hope This mail finds you well'
message = "subject:{}\n\n{}".format(subject,body)
listadd=['xyz@gmail.com','abc@gmail.com']
ob.sendmail('pratigyapandey345@gmail.com',listadd,message)
print('send mail')
ob.quit()