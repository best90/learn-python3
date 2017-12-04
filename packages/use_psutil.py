#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil

#cpu逻辑数量
print(psutil.cpu_count())
#cpu物理核心
print(psutil.cpu_count(logical=False))
#cpu的用户、系统、空闲时间
print(psutil.cpu_times())

for x in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))

#物理内存信息
print(psutil.virtual_memory())
#交换内存信息
print(psutil.swap_memory())

#磁盘分区信息
print(psutil.disk_partitions())
#磁盘使用情况
print(psutil.disk_usage('/'))
#磁盘io
print(psutil.disk_io_counters())

#获取网络读写字节、包的个数
print(psutil.net_io_counters())
#获取网络接口信息
print(psutil.net_if_addrs())
#获取网络端口状态
print(psutil.net_if_stats())
#当前网络连接信息
print(psutil.net_connections())

#所有进程id
print(psutil.pids())

p = psutil.Process(7688)
#进程名称
print(p.name())
#进程路径
print(p.exe())
#进程工作目录
print(p.cwd())
#进程启动的命令行
print(p.cmdline())
# 父进程id
print(p.ppid())
# 父进程
print(p.parent())
# 子进程
print(p.children())
# 进程状态
print(p.status())
#进程用户名
print(p.username())
# 进程创建时间
print(p.create_time())
#进程终端
print(p.terminal())
# 进程使用的cpu时间
print(p.cpu_times())
#进程使用的内存
print(p.memory_info())
# 进程打开的文件
print(p.open_files())
# 进程相关的网络连接
print(p.connections())
# 进程的线程数量
print(p.num_threads())
#所有线程信息
print(p.threads())
# 进程环境变量
print(p.environ())
# 结束进程
print(p.terminate())