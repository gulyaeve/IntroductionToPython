import pexpect


if __name__ == '__main__':
    ssh = pexpect.spawn("ssh eugene@0.0.0.0")
    ssh.expect(["Password", "password"])
    ssh.sendline("1")
    ssh.expect("[>#~]")
    ssh.sendline("uptime")
    ssh.expect("")
    out = ssh.before.decode("utf-8")
    print(out)
    # sh = pexpect.spawn("sh")
    # out = sh.before
    # print(out)
