import os
import time
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import socket
import psutil

while True:
    def jianca():
        print('[+]Write a port to a file')
        querys = os.popen('netstat  -an').read()
        wsd = open('netstat.txt', 'w')
        wsd.write(querys)
        wsd.close()


    jianca()


    def swsd():
        global usd, ow
        wsd = open('netstat.txt', 'r')
        swd = wsd.read()
        odf = re.findall(
            '(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9]):(3389)',
            swd)
        usd = odf[0]
        print('[+]Query the IP address of a remote connection')
        df = usd[0], usd[1], usd[1], usd[3]
        wdst = ".".join(df)
        ow = wdst + ":" + usd[4]
        print(usd[0], '.', usd[1], '.', usd[2], '.', usd[3] + ":", usd[4])


    swsd()


    def ipdw():
        global wdf, ip, timsd
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dw = s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        print('[+]loacl IP:', ip)
        wdf = os.popen('tasklist').read()
        timsd = time.strftime('%Y-%m-%d', time.localtime(time.time()))


    ipdw()


    def yunwei():
        global cput, cp
        cput = psutil.cpu_times()
        cp = psutil.disk_io_counters()


    yunwei()


    def stm():
        serder = "搜狐邮箱@sina.cn"
        revw = "收件箱@qq.com"
        zhengwen = '[+]Query the IP address of a remote connection''{}\n' \
                   '[+]loacl IP:{}\n' \
                   '[+]A program running in the background:{}\n' \
                   '[+]The user / system / idle time of statistical CPU:{}\n' \
                   '[+]Disk I/O usage{}\n' \
                   '[+]Last send time:{}\n'.format(ow, ip, wdf, cput, cp, timsd)
        msg = MIMEText(zhengwen)
        msg['From'] = Header('你的搜狐邮箱@sina.cn')
        msg['TO'] = Header('收件箱@qq.com', 'utf-8')
        sub = "实时监控"
        msg['subject'] = Header(sub, 'utf-8')
        try:
            smtp = smtplib.SMTP()
            smtp.connect('smtp.sina.cn', 25)
            smtp.login('搜狐邮箱@sina.cn', '登录密码')
            smtp.sendmail(serder, revw, msg.as_string())
            print('[+]发送出')
        except Exception as g:
            print('[-]发送失败，原因:', g)


    stm()

    time.sleep(3600)