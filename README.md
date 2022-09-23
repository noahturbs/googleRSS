# googleRSS.py

uses this library https://github.com/LLukas22/Google-News-Feed

install the necessary module: `pip install google-news-feed`

to run the program type in cmd: `python googleRSS.py`


## example screenshot:





![cmdscreenshot](https://user-images.githubusercontent.com/36610564/191624143-fb0f4e01-d78d-430a-b397-9b98335b209f.png)


![image](https://user-images.githubusercontent.com/36610564/191624476-ae4f41c6-ecb9-4836-9008-9e7ee6e3a386.png)


## Summary:
this library uses RSS requests, which is easier to use than google search engine API. A single request can return 100 articles, but for the sake of readability I only print out 5. (you can change the code to see more articles)

google still doesn't like it if a computer is spam requesting RSS; if you spam it too much with scripts, your ip will be blacklisted.

here is a blogpost of the specifications and limitations of RSS: 
https://web.archive.org/web/20210223173539/https://blog.newscatcherapi.com/google-news-rss/

### Recommendations to upgrade in the near future:

-use a proxy (this can hide your ip so you can make more requests. this can be done with some lines of code, or some kind of virtual machine)

-use a rotating list of proxies


### Recommendations to upgrade in the distant future:

-replace google RSS requests with scraping directly from news websites (dozens or hundreds of websites).

-maintain your own database to store results


