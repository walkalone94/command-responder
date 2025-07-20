#!/usr/bin/env python3

from cortexutils.responder import Responder
import subprocess

class IptablesBlockResponder(Responder):
    def __init__(self):
        Responder.__init__(self)

    def run(self):
        ip = self.get_param("data", None)
        if not ip:
            self.report({"error": "No IP provided"})
            return

        # SSH 접속 정보
        firewall_host = "10.0.0.146"
        firewall_user = "alma"

        # 원격 명령어
        remote_cmd = f"sudo iptables -A INPUT -s {ip} -j DROP"

        # 전체 SSH 명령 구성
        cmd = f"ssh -o StrictHostKeyChecking=no {firewall_user}@{firewall_host} '{remote_cmd}'"

        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            self.report({
                "status": "blocked",
                "ip": ip,
                "host": firewall_host,
                "command": remote_cmd,
                "output": output.decode()
            })
        except subprocess.CalledProcessError as e:
            self.report({
                "status": "error",
                "ip": ip,
                "host": firewall_host,
                "command": remote_cmd,
                "error": e.output.decode()
            })
