FROM python:3.5-alpine

ENV TZ=Asia/Shanghai

ADD ./requirements.txt /requirements.txt

RUN cp /etc/apk/repositories /etc/apk/repositories.bak && \
    echo "http://mirrors.aliyun.com/alpine/v3.4/main/" > /etc/apk/repositories && \
    apk update && \
    apk add --no-cache vim && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    pip install -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com -r /requirements.txt && \
    echo ""               >> /etc/vim/vimrc && \
    echo "set nu"         >> /etc/vim/vimrc && \
    echo "set ts=4"       >> /etc/vim/vimrc && \
    echo "set expandtab"  >> /etc/vim/vimrc && \
    echo "set autoindent" >> /etc/vim/vimrc

WORKDIR /usr/src/app

ADD . .

ENTRYPOINT ["entrypoint.sh"]
