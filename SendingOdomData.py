import paramiko
import time
import os


while (True):
	host1,user1,pwrd1 = '10.0.0.3', 'agilex', 'agx'
	host2,user2,pwrd2 = '10.0.0.4', 'agilex','agx'

	client1 = paramiko.SSHClient()
	client2 = paramiko.SSHClient()

	client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client1.connect(host1, username=user1, password = pwrd1)
	ftp = client1.open_sftp()
	remote_file_path ='/home/agilex/agilex_ws/odom_data_.txt'
	local_file_path = 'odom_data_.txt'
	ftp.get(remote_file_path, local_file_path)
	ftp.close()
