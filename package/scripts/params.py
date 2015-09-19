#!/usr/bin/env python

from resource_management import *

config = Script.get_config()

java64_home = config['hostLevelParams']['java_home']
hdfs_bin = config['configurations']['global']['hdfs_bin']
app_root = config['configurations']['global']['app_root']
app_user = config['configurations']['global']['app_user']
user_group = config['configurations']['global']['user_group']
log_dir = config['configurations']['global']['app_log_dir']
java_opts = config['configurations']['global']['java_opts']
jmxport = config['configurations']['global']['jmxport']
pid_file = config['configurations']['global']['pid_file']
this_host = config['configurations']['global']['host']
keystore_in_hdfs = config['configurations']['global']['keystore_in_hdfs']

keystore_file = config['configurations']['hdfsftp']['ssl-keystore-file']
