#!/bin/sh
mkdir r
chmod ugo+rwx r

mkdir datas
chmod ugo+rwx r

docker build -t sheepkiller/build-rpm .
#docker run --rm -it -v ${PWD}/r:/root/rpmbuild sheepkiller/build-rpm
docker run --rm -it -v ${PWD}/datas:/root/datas sheepkiller/build-rpm
