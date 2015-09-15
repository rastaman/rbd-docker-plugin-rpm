#!/bin/bash -e

rpmdev-setuptree

cp -p /root/rbd-docker-plugin.spec /root/rpmbuild/SPECS
for i in rbd-docker-plugin-wrapper rbd-docker-plugin.service rbd-docker-plugin.conf
do
    cp -p /root/${i} /root/rpmbuild/SOURCES
done
[ -f /root/rpmbuild/SOURCES/0.1.9.tar.gz ] || \
wget -O /root/rpmbuild/SOURCES/0.1.9.tar.gz https://github.com/yp-engineering/rbd-docker-plugin/archive/0.1.9.tar.gz
wget -O /root/rpmbuild/SOURCES/rbd-docker-plugin_logrotate https://raw.githubusercontent.com/sheepkiller/rbd-docker-plugin/master/logrotate.d/rbd-docker-plugin_logrotate

# Didn't work:
#ls -al /root/rpmbuild/SOURCES/0.1.9.tar.gz
#chown -R root:root /root/rpmbuild/*
#ls -al /root/rpmbuild/SOURCES/0.1.9.tar.gz

rpmbuild -ba /root/rpmbuild/SPECS/rbd-docker-plugin.spec

# Workaround:
cp /root/rpmbuild/SRPMS/rbd-docker-plugin-0.1.9-1.el7.centos.src.rpm /root/datas
cp /root/rpmbuild/RPMS/x86_64/rbd-docker-plugin-0.1.9-1.el7.centos.x86_64.rpm /root/datas
cp /root/rpmbuild/RPMS/x86_64/rbd-docker-plugin-debuginfo-0.1.9-1.el7.centos.x86_64.rpm /root/datas
