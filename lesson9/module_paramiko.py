import paramiko


if __name__ == '__main__':
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname="0.0.0.0",
        port=22,
        username="eugene",
        password="1",
        allow_agent=False,
    )

    ssh = client.invoke_shell()
    ssh.send("mkdir ~/folder_from_ssh\n")
    ssh.recv(3000)

    client.close()

