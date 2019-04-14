#!/bin/bash
# 让脚本遇到错误就退出

# 设置变量
PROJECT_DIR=~/phyweb/
EXECUTABLE_JAR_PATH=~/phyweb/target/phyweb-0.0.1-SNAPSHOT.jar

cd ${PROJECT_DIR}

echo "step 1:"
mvn clean

echo "step 2:"
mvn install

echo "step 3:"
re_install() {
    service phyweb stop
    rm /etc/init.d/phyweb
    systemctl daemon-reload
    cp ${EXECUTABLE_JAR_PATH} /etc/init.d/phyweb
    systemctl daemon-reload
    return 0;
}
re_install;

echo "step 4:"
service phyweb start

echo "Nice, deploy success~~~"

