FROM python:3.5-alpine

RUN cp /etc/apk/repositories /etc/apk/repositories.bak

RUN echo "http://mirrors.aliyun.com/alpine/v3.4/main/" > /etc/apk/repositories

RUN apk update && \
    apk add --no-cache \
        vim

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./requirements.txt /requirements.txt
RUN pip install -i http://pypi.douban.com/simple \
        --trusted-host=pypi.douban.com -r /requirements.txt

WORKDIR /usr/src/app

ADD . .

# vim config.  tab == 4 spaces
RUN echo ""         >> /etc/vim/vimrc &&        \
    echo "set nu"   >> /etc/vim/vimrc &&        \
    echo "set ts=4" >> /etc/vim/vimrc &&        \
    echo "set expandtab" >> /etc/vim/vimrc &&   \
    echo "set autoindent" >> /etc/vim/vimrc


# ### entrypoints
CMD sh entrypoint.sh

