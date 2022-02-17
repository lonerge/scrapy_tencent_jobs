# scrapy_tencent_jobs
利用scrapy框架爬取腾讯招聘信息

> 主要思路:
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
    
    


>>> 1.
内容填充        < br >
2.
        内容填充          < br >
3.
        内容填充         

>> 方法2: < br >
>>> 1.
        内容填充         < br >
2.
        内容填充          < br >
3.
        内容填充          < br >
4.
        内容填充          < br >
5.
        内容填充          < br >
6.
内容填充

>> 方法3: < br >
>> > 1.
        内容填充          < br >
2.
        内容填充          < br >
3.
        内容填充         < br >
4.
        内容填充      

>   一.项目开始:
>>  
    1.创建scrapy项目: 
    scrapy startproject tencent        

    2.查看需要爬取的目标字段,进行建模:
    < br >
    
    3.内容填充         

> 二.       < br >

1.
        内容填充         < br >
2.
        内容填充         

   

> 遇到的问题: < br >
>>         内容填充         


        内容填充         
        
        内容填充         
        
        内容填充         
        

>>         内容填充         
< br >

>>         内容填充         





