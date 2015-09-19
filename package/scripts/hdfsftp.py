#!/usr/bin/env python

import sys
from resource_management import *

class HDFSFTP(Script):
  def install(self, env):
    self.install_packages(env)

  def configure(self, env):
    import os
    import params
    env.set_params(params)

    keystore_path = params.app_root + "/" + params.keystore_file

    File(format("{params.log_dir}/hdfs-over-ftp.log"),
      mode=0666,
      owner=params.app_user,
      group=params.user_group
    )

    TemplateConfig(format("{app_root}/log4j.xml"), owner = params.app_user, group = params.user_group)
    #TemplateConfig(format("{app_root}/hdfs-over-ftp.properties"), owner = params.app_user, group = params.user_group)

    PropertiesFile(format("{app_root}/hdfs-over-ftp.properties"),
      properties = params.config['configurations']['hdfsftp'],
      owner = params.app_user,
      group = params.user_group
    )

    PropertiesFile(format("{app_root}/users.properties"),
      properties = params.config['configurations']['usersprops'],
      owner = params.app_user,
      group = params.user_group
    )

    if not os.path.exists(keystore_path):
      Execute(format("{hdfs_bin} dfs -get {keystore_in_hdfs} {keystore_path}"),
               user=params.app_user)
      File(keystore_path,
            mode=0600,
            group=params.app_user,
            owner=params.user_group,
            replace=False)

  def start(self, env):
    import params
    env.set_params(params)
    self.configure(env)
    process_cmd = format("{java64_home}/jre/bin/java {params.java_opts} -Dcom.sun.management.jmxremote.port={params.jmxport} -Dcom.sun.management.jmxremote.rmi.port={params.jmxport} -cp {params.app_root}/:{params.app_root}/lib/* org.apache.hadoop.contrib.ftp.HdfsOverFtpServer --approot {params.app_root} > {params.log_dir}/hdfsftp-output.log 2>&1")

    #user=params.app_user,
    Execute(process_cmd,
        logoutput=True,
        wait_for_finish=False,
        pid_file=params.pid_file
    )

  def stop(self, env):
    import params
    env.set_params(params)

  def status(self, env):
    import params
    env.set_params(params)
    check_process_status(params.pid_file)

if __name__ == "__main__":
  HDFSFTP().execute()
