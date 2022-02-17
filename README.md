# scrapy_tencent_jobs
利用scrapy框架爬取腾讯招聘信息

> 一.主要思路:
>>  
    1.创建scrapy项目      

    2.查看目标字段,进行建模:
    
    3.创建爬虫一,提取主要数据:
              name:招聘主信息名
              link:招聘信息详情链接
              date:发布日期
              city:城市
              resp:岗位职责
              
    4.创建爬虫二,提取全部数据(这里需要使用scrapy.Request()方法里面的meta传参):
              name:招聘主信息名
              link:招聘信息详情链接
              date:发布日期
              city:城市
              resp:岗位职责
              require:岗位要求
              postid:岗位id
              
    5.给两个爬虫实现翻页功能
    
    6.实现两个管道分别服务两个爬虫,开启管道
    
    7.开启爬虫
          
>   一.项目开始:
>   
>   1.创建scrapy项目: 
    
>>
    scrapy startproject tencent
>>

>   2.查看需要爬取的目标字段,进行建模:
>>
    items.py
>>  
>    
>   3.创建爬虫1: 
    
>>
    scrapy genspider simple tencent.com
>>  

>    
>   4.完善爬虫1: 
    
>>
    simple.py
>>  

>    
>   5.创建爬虫2: 
    
>>
    scrapy genspider whole tencent.com
>>  

>    
>   6.完善爬虫2: 
    
>>
    whole.py
>>  

>    
>   7.分别编写两个管道: 
    
>>
    pipelines.py
>>  

>    
>   8.开启管道: 
    
>>

    ITEM_PIPELINES = {'tencent.pipelines.WholePipeline': 300,'tencent.pipelines.SimplePipeline': 301,}

>>  

>    
>   9.开启爬虫: 
    
>>
    scrapy crawl 爬虫名
>> 

   

> 遇到的问题: 
> 
>> 1.腾讯招聘页的目标数据并不是在简单的首页html文件中,而是隐藏在一个名为: Query?timestamp=******* 的xhr文件中(返回的响应是json格式)
>> 
>> 2.含有目标的详情页的地址为: https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=+'十三位时间戳'+'postId'+&language=zh-cn
>>
>> 3.pipelines里管道类的process_item函数必须要返回item对象,不然下一个管道取的值为None
       






