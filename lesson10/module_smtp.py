import smtplib


server = smtplib.SMTP(
    host="smtp.google.com",
    port=465
)

server.starttls()
server.login(
    user="vasya@gmail.com",
    password="123"
)

server.sendmail(
    from_addr="vasya@gmail.com",
    to_addrs="petya@gmail.com",
    msg="Subject: Test\n\nHello"
)

server.quit()
