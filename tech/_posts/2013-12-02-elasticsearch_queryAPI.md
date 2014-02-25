---
layout: post
title: "Elasticsearch查询接口"
tags: [Elasticsearch]
published: ture
---


##Elasticsearch 查询接口

- This will become a table of contents (this text will be scraped).
{:toc}


###queries
####match query
接受文本/数值/日期解析并构造查询条件.提供的文本会被分析构建为一个布尔型查询.

~~~~
{
    "match" : {
         "message" : {//字段名，可以是_all
            "query" : "this is a test",//查询语句
            "analyzer" : "my_analyzer",//定义分析器.它会使用mapping中定义的分析器, 如果没有定义则会使用索引的默认分析器
            "operator" : "and",//使用 or 或者 and 来组合布尔子句 (默认为 or).
            "zero_terms_query": "all",//如果去掉停用词分析后没有词语，则全部匹配
            "cutoff_frequency" : 0.001,//[0,1) ?
            "fuzziness": 0.3,//[0,1]模糊查询
            "type" : "phrase",//保持词语的顺序 或者如下
            ["type" : "phrase_prefix",//保持顺序，允许前缀匹配
            "max_expansions" : 10]//允许的前缀词长度
          }
     }

}
~~~~
####multi match query
多字段查询，兼容match的所有选项

~~~~
{
  "multi_match" : {
    "query" : "this is a test",
    "fields" : [ "subject^2", "message" ],//指定字段，通过^支持boosting,如subject的命中会比message中的命中重要2倍
    "use_dis_max":"true",//使用dis_max或者bool，默认true
    "tie_breaker":0//乘数平衡高分字段和低分字段，默认0 ？
  }
}
~~~~
####bool query

~~~~
{
    "bool" : {
        "must" : {//匹配的文档必须满足该查询语句
            "term" : { "user" : "kimchy" }
        },
        "must_not" : {//匹配的文档必须不满足该查询语句. 注意, 不能只用一个 must_not 查询语句来搜索文档.
            "range" : {
                "age" : { "from" : 10, "to" : 20 }
            }
        },
        "should" : [//匹配的文档可以满足该查询语句. 如果一个布尔查询(Bool Query)不包含 must 查询语句, 那么匹配的文档必须满足其中一个或多个 should 查询语句, 可以使用 minimum_number_should_match 参数来设定最低满足的数量.
            {
                "term" : { "tag" : "wow" }
            },
            {
                "term" : { "tag" : "elasticsearch" }
            }
        ],
        "minimum_should_match" : 1,
        "boost" : 1.0//重要性
    }
}
~~~~
####boosting query

~~~~
{
    "boosting" : {
        "positive" : {
            "term" : {
                "field1" : "value1"
            }
        },
        "negative" : {
            "term" : {
                "field2" : "value2"
            }
        },
        "negative_boost" : 0.2
    }
}
~~~~

####common terms query
保留停用词进行查询，分成两类：低频词（重要）、高频词（不重要）。先检索低频词，然后在结果中检索高频词。

~~~~
{
  "common": {
    "body": {//字段
      "query":                "nelly the elephant as a cartoon",//查询语句
      "cutoff_frequency":     0.001,//区别高频与低频的界限，(0.0 .. 1.0)或者真实值>=1
      "low_freq_operator" :"and",//低频词都检索，默认 or
      "high_freq_operator" :"and",//高频词都检索，默认 or
      "minimum_should_match": {
          "low_freq" : 2,//低频词至少命中2次
          "high_freq" : 3//高频词至少命中3次
          }
    }
  }
}
~~~~

####custom filters score query
Replaced by **Function Score Query**.

~~~~
{
    "custom_filters_score" : {
        "query" : {
            "match_all" : {}
        },
        "filters" : [
            {
                "filter" : { "range" : { "age" : {"from" : 0, "to" : 10} } },
                "boost" : "3"
            },
            {
                "filter" : { "range" : { "age" : {"from" : 10, "to" : 20} } },
                "boost" : "2"
            }
        ],
        "score_mode" : "first"//first代表第一次匹配的规则作为最终得分，也可以是min/max/total/avg/multiply做相应计算作为最终结果
    }
}
~~~~

####custom score query
Replaced by **Function Score Query**.

####custom boost factor query
Replaced by **Function Score Query**.

####constant score query
返回一个分值

~~~~
{
    "constant_score" : {
        "filter" : {
            "term" : { "user" : "kimchy"}
        },
        "boost" : 1.2
    }
}
~~~~

####dis max query？

~~~~
{
    "dis_max" : {
        "tie_breaker" : 0.7,
        "boost" : 1.2,
        "queries" : [
            {
                "term" : { "age" : 34 }
            },
            {
                "term" : { "age" : 35 }
            }
        ]
    }
}
~~~~
####field query？
####filtered query
可以在一个查询的结果上应用一个过滤操作.

~~~~
{
    "filtered" : {
        "query" : {
            "term" : { "tag" : "wow" }
        },
        "filter" : {//该DSL里面的 filter 对象只能使用 filter 元素, 而不能是query类型. 过滤（Filters） 要比查询快很多，因为和查询相比它们不需要执行打分过程, 尤其是当设置缓存过滤结果之后.
            "range" : {
                "age" : { "from" : 10, "to" : 20 }
            }
        }
    }
}
~~~~

####fuzzy like this query

~~~~
{
    "fuzzy_like_this" : {//可简写为flt
        "fields" : ["name.first", "name.last"],//字段列表，默认_all
        "like_text" : "text like this one",//检索词，必须有
        "max_query_terms" : 12,//最大检索词量 默认25
        "ignore_tf" : "false",//忽略词频，默认flase
        "min_similarity" //The minimum similarity of the term variants. Defaults to 0.5.

		"prefix_length" //Length of required common prefix on variant terms. Defaults to 0.

		"boost" //Sets the boost value of the query. Defaults to 1.0.

		"analyzer" //The analyzer that will be used to analyze the text. Defaults to the analyzer associated with the field.
    }
}
~~~~

####fuzzy like this field query
同上，只是应用于单个字段
~~~~
{
    "fuzzy_like_this_field" : {
        "name.first" : {
            "like_text" : "text like this one",
            "max_query_terms" : 12
        }
    }
}
~~~~

####function score query
http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/query-dsl-function-score-query.html

####fuzzy query

~~~~
{
    "fuzzy" : {
        "created" : {
            "value" : "2010-02-05T12:05:07",
            "min_similarity" : "1d"
        }
    }
}
~~~~

####geoshape query
####has child query
####has parent query
####ids query
####indices query
####match all query
A query that matches all documents.

~~~~
{
    "match_all" : { "boost" : 1.2 }
}
~~~~

####more like this query
http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/query-dsl-mlt-query.html  
查找最符合查询条件的文档

~~~~
{
    "more_like_this" : {//简写 mlt
        "fields" : ["name.first", "name.last"],
        "like_text" : "text like this one",
        "min_term_freq" : 1,
        "max_query_terms" : 12
    }
}
~~~~

####more like this field query
同上，只是应用于单个字段

####nested query
嵌套查询

~~~~
{
    "nested" : {
        "path" : "obj1",
        "score_mode" : "avg",
        "query" : {
            "bool" : {
                "must" : [
                    {
                        "match" : {"obj1.name" : "blue"}
                    },
                    {
                        "range" : {"obj1.count" : {"gt" : 5}}
                    }
                ]
            }
        }
    }
}
~~~~

####prefix query

####query string query

http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/query-dsl-query-string-query.html

####range query
返回范围内的查询结果

~~~~
{
    "range" : {
        "age" : {
            "gte" : 10,//大于等于，gt大于
            "lte" : 20,//小于等于，lt小于
            "boost" : 2.0
        }
    }
}
~~~~

####regexp query
支持正则表达式查询  
http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/query-dsl-regexp-query.html

####span first query？
####span multi term query？
####span near query？
####span not query?
####span or query?
####span term query?
####term query
完全匹配一个词

~~~~
{
    "term" : { "user" : "kimchy" }
}
~~~~

####terms query
匹配多个词

~~~~
{
    "terms" : {
        "tags" : [ "blue", "pill" ],
        "minimum_should_match" : 1
    }
}
~~~~

####top children query？
####wildcard query
通配符查询

~~~~
{
    "wildcard" : { "user" : { "value" : "ki*y", "boost" : 2.0 } }
}
~~~~

####minimum should match
整数、负整数、百分数、负百分数、混合。。。

####multi term query rewrite
~~~~

~~~~



###References
[1] [elasticsearch query dsl][r1]

[r1]: http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/query-dsl.html

[2] [elasticsearch 向导 query dsl][r2]

[r2]: http://www.elasticsearch.cn/guide/reference/query-dsl/
