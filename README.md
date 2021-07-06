# 微博

搜索正文中包含指定关键词的微博
其中关键词位于weibo/settings.py `KEYWORD_LIST`。

## 数据获取

### 操作说明

1. 获取cookie
<https://weibo.com/> -> `F12` -> coockie

1. 修改setting配置
    `weibo/settings.py`: KEYWORD_LIST, START_DATE, END_DATE

1. 启动爬虫

    ```bash
    conda activate weibo
    sh run.sh
    ```

1. 输出
  `./result`, 以关键词划分

### 抓取情况

计划爬取16年以后的数据，共5.5年

- [x] 2021-01-01 ~ 2021-07-03
- [x] 2020-01-01 ~ 2020-12-31
- [ ] 2019-01-01 ~ 2019-12-31
- [ ] 2018-01-01 ~ 2018-12-31
- [ ] 2017-01-01 ~ 2017-12-31
- [ ] 2016-01-01 ~ 2016-12-31

### Ref

- <https://github.com/dataabc/weibo-search>
- <https://github.com/dataabc/weiboSpider>
- <https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/overview.html>
- [爬虫框架Scrapy个人总结](https://www.jianshu.com/p/cecb29c04cd2)

## NLP处理

### Ref

- [使用PySpark处理文本多分类问题](https://blog.csdn.net/hlpower/article/details/102918969)
