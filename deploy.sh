#!/bin/bash -e
# 让脚本遇到错误就退出
set -e

# 设置变量
PROJECT_DIR=~/phyweb/
EXECUTABLE_JAR_PATH=~/phyweb/target/phyweb-0.0.1-SNAPSHOT.jar

cd ${PROJECT_DIR}

echo "step 1:"
mvn clean

echo "step 2:"
mvn install

echo "step 3:"
if [ ! -e "/etc/init.d/phyweb" ] ; then
    rm /etc/init.d/phyweb
    ln -s ${EXECUTABLE_JAR_PATH} /etc/init.d/phyweb
    systemctl daemon-reload
else
    systemctl daemon-reload
    service phyweb stop
fi

echo "step 4:"
service phyweb restart

echo "Nice, deploy success~~~"

