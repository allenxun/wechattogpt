# wechattogpt
************************************************************

# 项目说明

## nginx文件夹
- nginx的配置文件在`/etc/nginx/nginx.conf`

## systemctl_config系统服务配置
- system在`/etc/systemd/system/`下

## ubuntu_env文件夹
- mysql docker的配置文件
- 其中command.log是命令的一些记录，并不准确
- docker-compose.yml是docker的启动文件
>
    docker-compose up -d

## uwsgi文件夹
- uwsgi的配置文件

## wechatapi文件夹
- static是静态文件，暂时无用
- mytask准备写定时任务
- api是微信公众号转发的应用
- wechatapi是项目的主要文件
- manage.py是项目的启动文件
>
    python manage.py runserver

************************************************************

# 项目运行

- 按照ubuntu_env文件夹下的command.log文件的顺序执行命令即可
- 启动顺序：
>
    docker-compose up -d
    systemctl start uwsgi
    systemctl start nginx

************************************************************

# 项目进度

## django项目
- 暂时不会更新

## chatGPT脚本
- 新建支持chatGPT会话脚本，用于日常问答
- 可能会偷个懒用django来处理数据库，因此django的数据库会冗余一些