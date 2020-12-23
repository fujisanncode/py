import paramiko
import json


def upload():
    # 本地json文件读取为字典格式
    with open('../local/config.json', 'r', encoding='utf-8') as config:
        load = json.load(config)
    # 字典中读取变量
    dev_ = load['dev']
    host = dev_['host']
    port = dev_['port']
    username = dev_['username']
    password = dev_['password']
    local_path = dev_['local_path']
    server_path = dev_['server_path']
    # 通过sftp协议连接服务器
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    client = paramiko.SFTPClient.from_transport(transport)
    # 上传文件
    client.put(local_path, server_path)
    client.close()


upload()
