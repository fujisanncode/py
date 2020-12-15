import os
import pandas

'''
  TCP    0.0.0.0:8012           0.0.0.0:0              LISTENING       13172
  TCP    [::]:8012              [::]:0                 LISTENING       13172
'''


def kill_port(port):
    # 过滤端口找到进程
    s_port = 'netstat -aon | findstr %s' % port
    popen = os.popen(s_port)
    split = popen.read().split('\n')
    data = []
    for line in split:
        # 如果为空则跳过
        if not line:
            continue
        # 遍历line分割的数组并保留非空的值列表
        temp = [str1 for str1 in line.split(" ") if str1]
        data.append(temp)
    parse_cmd(data)


def parse_cmd(data):
    columns = ['type', 'secret', 'open', 'status', 'pid']
    # 用指定数组结构解析数组
    frame = pandas.DataFrame(data=data, columns=list(columns))
    for index in range(len(data)):
        pid = frame.loc[index, 'pid']
        kill_pid(pid)


def kill_pid(pid):
    # 杀死进程
    s_pid = 'taskkill -f -pid %s' % pid
    print(s_pid)
    popen = os.popen(s_pid)
    print(popen)


kill_port(8012)
