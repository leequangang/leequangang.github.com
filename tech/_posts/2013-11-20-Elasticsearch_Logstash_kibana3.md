---
layout: post
title: "Elasticsearch & Logstash & Kibana 日志管理系统"
tags: [Elasticsearch, Logstash, Kibana]
published: ture
---


## Elasticsearch & Logstash & Kibana 日志管理系统

- This will become a table of contents (this text will be scraped).
{:toc}

注:Elasticsearch与Logstash需要安装Java虚拟机，Kibana需要一个Web服务器。本身Logstash中内置也一个Elasticsearch和Kibana。

### Elasticsearch

Github项目地址[https://github.com/elasticsearch/elasticsearch](https://github.com/elasticsearch/elasticsearch)

[2013-11-26止最新版0.90.7](https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.7.zip)
(2014.7看到的是1.2.2版 [Download](http://www.elasticsearch.org/download))
默认端口:9200。

[5分钟教程](http://www.elasticsearchtutorial.com/elasticsearch-in-5-minutes.html)
是模式自由的，随便给它个日志就会自动解析，但是最好是自定义一个映射表mapping，定义好各字段的数据类型。

####《ElasticSearch Server》中2.2 Mapping中例子

1. 新建索引库: curl -XPOST http://localhost:9200/library

2. 导入mapping: curl -XPOST http://localhost:9200/library/book/_mapping -d @mapping.json

3. 批量执行导入数据命令：curl -XPOST http://localhost:9200/library/book/_bulk --data-binary @documents.json

4. 查看数据：curl -XGET http://localhost:9200/library/book/_search?pretty=true

**注意：** 书中的mapping导入会出错，提示 boolean 型数据不能 be tokenized ，把最后的 "available" 字段改成 "not_analyzed"的即可。library 相当于建了一个数据库，book 是该数据库中的一张表，mapping 是这个表的结构（字段的类型、索引方式、存储方式等等），定义好这些后往表里面插入一条记录 ES 就会按照 mapping 定义的格式把记录进行分词、创建索引、存储等工作。


#### 使用基本流程：

1. 安装，用到中文可以安装[集成ik的ES版本](https://github.com/medcl/elasticsearch-rtf),启动方式见下面内容。查看是否启动,浏览器输入 http://localhost:9200/

2. 新建索引库curl -XPOST 'http://localhost:9200/twitter/tweet'

3. 上传定义的mapping，curl -XPOST http://localhost:9200/index/fulltext/_mapping -d 'mapping的内容'

4. 插入Json格式数据，curl -XPOST 'http://localhost:9200/twitter/tweet' -d 'Json格式数据'

5. 刷新生效，curl -XPOST 'http://localhost:9200/twitter/tweet/_refresh'

6. 查询，curl -XPOST http://localhost:9200/test/my/_search -d 'Json格式的查询语句'

7. 删除索引库 curl -XDELETE http://localhost:9200/test/


#### RESTful语法

GET用来获取资源，POST用来新建资源（也可以用于更新资源），PUT用来更新资源，DELETE用来删除资源。

./bin/elasticsearch -f

返回结果中的took是值执行时间 微妙

关闭/开启索引  
- curl -XPOST 'localhost:9200/my_index/_close'
- curl -XPOST 'localhost:9200/my_index/_open'

检测索引、表是否存在。返回200说明存在，返回404说明不存在（API中使用-XHEAD，但是无返回结果）
- curl -I 'http://localhost:9200/twitter'
- curl -I 'http://localhost:9200/twitter/tweet'

清除缓存
- curl -XPOST 'http://localhost:9200/twitter/_cache/clear'

刷新执行
- curl -XPOST 'http://localhost:9200/twitter/_refresh'

输入Json文本
curl -XPOST 'http://IP:9200/test' -d @lane.json

ElasticSearch expects a JSON _object_, not an array 每个文件一条记录，要是一个文件有多条记录就要用到[bulk API](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-bulk.html)。其中Json文件中每条记录要用`\n`换行分隔

~~~
curl -s -XPOST localhost:9200/_bulk --data-binary @test.json

{"index" : {"_index" : "country", "_type" : "city"}}
{"nation" : "China", "city" : "Tianjin", "year" : ["2011", "2012", "2013"]}
{"index" : {"_index" : "country", "_type" : "city"}}
{"nation" : "USA", "city" : "Califorlia", "year" : ["2012", "2014", "2015"]}
{"index" : {"_index" : "country", "_type" : "city"}}
{"nation" : "China", "city" : "Beijing", "year" : ["2012", "2014", "2015"]}
~~~

`-s /--silent        Silent mode. Don't output anything不输出信息`

`curl -XPOST 'localhost:9200/_refresh' 刷新写入`

各种[River plugin](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-plugins.html)把数据传入ES
[JDBC River Plugin](https://github.com/jprante/elasticsearch-river-jdbc)可以将Mysql的数据传入ES
[Quick Start](https://github.com/jprante/elasticsearch-river-jdbc/wiki/Quickstart)


SELECT * FROM table into outfile 'test.csv' fields terminated by '\t';

pyes包


（1）get是从服务器上获取数据，post是向服务器传送数据。

（2）在客户端，Get方式在通过URL提交数据，数据在URL中可以看到；POST方式，数据放置在HTML HEADER内提交。

（3） 对于get方式，服务器端用Request.QueryString获取变量的值，对于post方式，服务器端用Request.Form获取提交的数据。

（4） GET方式提交的数据最多只能有1024字节，而POST则没有此限制。

（5）   安全性问题。正如在（1）中提到，使用 Get 的时候，参数会显示在地址栏上，而 Post 不会。所以，如果这些数据是中文数据而且是非敏感数据，那么使用 get；如果用户输入的数据不是中文字符而且包含敏感数据，那么还是使用 post为好。

#### 版本1.0

bin/elasticsearch 前台启动  
bin/elasticsearch -d 后台启动

#### 安装Marvel 监控插件

- 运行`bin/plugin -i elasticsearch/marvel/latest`

- 打开查看`http://any-server-in-cluster:9200/_plugin/marvel/`


安装libcurl  `sudo apt-get install libcurl4-openssl-dev`
编译 `gcc post.c -lcurl`


查询所有索引 curl -XGET http://localhost:9200/test/my/_search?pretty=true

只输出单条记录的源字段，不包含头信息 curl -XGET 'http://localhost:9200/twitter/tweet/1/_source'

#### 插件

安装header--管理ES集群的，暂可不用


1. elasticsearch/bin/下运行`./plugin -install mobz/elasticsearch-head`

2. open http://localhost:9200/_plugin/head/

安装中文分词ik----安装未成功，可以使用集成ik版的ES
http://www.dongming8.cn/?p=16

mapping "enabled" : false禁用内容解析
"index" : "not_analyzed"
[mapping中字段格式](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/mapping-core-types.html)
string, integer/long, float/double, boolean, and null, byte, short, binary
如果是数值则在Json文件中可不加“”

~~~~
{
    "tweet" : {
        "properties" : {
            "message" : {
                "type" : "string",
                "store" : "yes",//存储方便以后重新加载
                "index" : "analyzed",//解析成可检索的词，not_analyzed就作为整体检索，no则不检索，Defaults to analyzed
                "null_value" : "na"//如果有null的值就存储为na
                "similarity" : "BM25"//计算相似度的算法 默认是TF/IDF
            }
        }
    }
}
~~~~

#### 集成版ES

集成ik版
[https://github.com/medcl/elasticsearch-rtf](https://github.com/medcl/elasticsearch-rtf)

git clone git://github.com/medcl/elasticsearch-rtf.git es
其中bin下的plgin没有运行权限需要添加
linux下运行
cd elasticsearch/bin/service
./elasticsearch console
[内置了elasticsearch-servicewrapper](https://github.com/elasticsearch/elasticsearch-servicewrapper)，有一些方便启动的具体用法

~~~~
./elasticsearch [参数]
console 在前台运行es
start 在后台运行es
stop 停止es
install 使es作为服务在服务器启动时自动启动
remove 取消启动时自动启动
~~~~


search?语句后添加pretty=true就是返回Json格式的结果，添加format=yaml就是返回yaml格式,什么都不加返回也是Json格式
human=false关闭统计信息的可读性，如1kb变成1024，默认是true，就看想输出给计算机监控程序还是工作人员。

op_type=create或者_create：如果不存在就插入

~~~~
/twitter/tweet/1?op_type=create' -d '{  //或者
/twitter/tweet/1/_create' -d '{`
~~~~

`twitter/tweet/1?timestamp=2009-11-15T14%3A12%3A12 -d '`时间戳如果不在外部指定，或者包含在_source中，则系统会自动按照ES处理的时间分配_timestamp.在mapping中定义格式

~~~~
{
    "tweet" : {//表名
        "_timestamp" : {
            "enabled" : true,//默认是关闭的 store：no ，index：not_analyzed
            "path" : "post_date",//可以指定字段，如指定post_date为timestamp,不过这样会耗费少量解析时间
            "format" : "YYYY-MM-dd"//默认格式是dateOptionalTime，可指定时间格式(http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/mapping-date-format.html)
        }
    }
}
~~~~

设置ttl来赋予生存时间，过期的会自动销毁

~~~
{
    "from" : 0, "size" : 10,//从第几个开始，返回几个结果
    "query" : {
        "term" : { "user" : "kimchy" }
    }
}
~~~

~~~
{
    "sort" : [//排序规则
        { "post_date" : {"order" : "asc"}},
        "user",
        { "name" : "desc" },
        { "age" : "desc" },
        "_score"
    ],
    "query" : {
        "term" : { "user" : "kimchy" }
    }
}
~~~

~~~~
{
    "fields" : ["user", "postDate"],//返回的字段，前提是存储过的，[]只返回匹配的_id与_type
    "query" : {
        "term" : { "user" : "kimchy" }
    }
}
~~~~

~~~~
{
    "indices_boost" : {//设置不同索引表的权重
        "index1" : 1.4,
        "index2" : 1.3
    }
}
~~~~


### Logstash

[Logstash](https://download.elasticsearch.org/logstash/logstash/logstash-1.2.2-flatjar.jar) will give you a way to read, parse logs as well as push them into ES.

java -jar logstash-1.2.2-flatjar.jar agent -f apache.conf -- web
注意 -- 与web之间的空格，在paper的vps上运行可以，但是在dlp64上运行出错，不知原因？


测试写入日志
nc 162.211.127.177 3333 < apache.log

http://162.211.127.177:9292/index.html#/dashboard/file/logstash.json

在IE下查看

port:9292
`logstash-1.2.2-flatjar\vendor\kibana\app\dashboards`下的logstash.json重命名为default.json就是logstash内置的Kibana界面，其他的.json是可以用户定制的界面

### Kibana

kibana是一个功能强大的elasticsearch数据显示客户端，logstash已经内置了kibana，你也可以单独部署kibana，最新版的kibana3是纯html+js客户端，可以很方便的部署到Apache、Nginx等Http服务器。
可以修改config.js来配置elasticsearch的地址和索引。
看到一个kibana介绍页面，将logstash.json重命名为default.json后就是一个可查询的页面

修改配置
http://blog.csdn.net/zhangyake88/article/details/15808923
默认的是检索所有的数据库



[kibana增加中国地图](http://blog.sectop.org/)

1. 将map.cn.js文件放到/panels/map/lib/目录下。

2. 修改/panels/map/editor.html,将['world','europe','usa']修改成['world','europe','usa','cn']即可



map选择国家码的字段，bettermap选择坐标字段，地图的要chrome下查看

**Logstash集成了Elasticsearch和Kibana以及一个内置web服务器，Elasticsearch+Kibana+web服务器也可以搭建一个日志分析系统**


基于Lucene的分布式搜索引擎Solr、ElasticSearch
让mysql no sql化

ElasticSearch（简称 ES） 是一个基于 Lucene 构建的开源，分布式，RESTful 搜索引擎。 设计用于云计算中，能够达到搜索实时、稳定、可靠和快速，并且安装使用方便。 支持通过 HTTP 请求，使用 JSON 进行数据索引。 搜索有两种方法，一种是使用Filter进行搜索，一种是使用Query进行搜索，
- ES根据设置的ID来设置对象，如果没有则插入，有则更新。每更新一次，对应的version加1.
 ES					SQL
 聚合功能Facet --> group by
 搜索功能Filter、Query --> like
 批量操作Bulk
 
 
`ulimit -a` 用来显示当前的各种用户进程限制。Linux对于每个用户，系统限制其最大进程数。在linux系统中，使用了非root用户启动的elasticsearch，但Linux对这些非特权用户打开的文件格式做了限制。导致elasticsearch报错。
 
修改方法，使用root编辑/etc/security/limits.conf，在最后面增加
elasticsearch soft nofile 32000  
elasticsearch hard nofile 32000 
修改之后，切换到elasticsearch用户，使用命令ulimit -Sn查看。
最后重启elasticsearch。
http://www.elasticsearch.org/tutorials/too-many-open-files/
http://blog.zuobus.com/archives/65.html


### References
[1] [exploring elasticsearch][r1]

[r1]: http://exploringelasticsearch.com/

[2] [ElasticSearch文档][r2]

[r2]: http://www.dongming8.cn/?page_id=156


[^id]: 这是脚注