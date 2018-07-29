centos:7
MAINTAINER The apitest Project <vyasrohitvyas@gmail.com>

RUN  yum install -y \
     epel-release \
     git

RUN yum install -y python-pip

RUN mkdir -p /testapi && cd /testapi && git clone https://github.com/maveric-tellrv/apitest.git


RUN pip install -r /testapi/apitest/requirement.txt


CMD ["/bin/bash", "-c" ,"cd /testapi/apitest/ && behave features/apitest/test2.feature "]
