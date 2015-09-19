## hdfs-over-ftp-slider
Configuration files to run [hdfs-over-ftp](https://github.com/jpbelleau/hdfs-over-ftp) on [Apache Slider](http://slider.incubator.apache.org/)

### Features
* No configuration files or keystore in application package
* Ports defined per component
* Port exports can be found on the application master under http://nodemgr:port/ws/v1/slider/publisher/slider/componentinstancedata

### Package configuration
* Set log configuration in package/templates/log4j.xml.j2 (set to file in app log directory by default)
* Create tarball (no compression) of jar and dependency jars then copy to package/files/
* Set tarball name in metainfo.xml
* Create and copy keystore to HDFS path accessible by user submitting Slider job
* Create zip file - include:
    - metainfo.xml
    - package/files/
    - package/scripts/
    - package/templates/

### Instance configuration

#### appConfig.json
* application.def - set HDFS path where this package will be put
* java_home - JDK home
* site.global.hdfs_bin - hdfs command binary
* site.global.keystore_in_hdfs - keystore file on HDFS
* site.hdfsftp prefixed items - will be stored in hdfs-over-ftp.properties file in application root
* site.usersprops items - will be stored in users.properties file in application root

#### resources.json
* Set resource requirements - YARN minimum still applies

### Running
slider create hdfsftp --template appConfig.json --resources resources.json

### License
Apache License 2.0
