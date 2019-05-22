from requests_html import HTMLSession

def get_baidu_news_titles():
    ans_news_titles = []
    urls = "http://news.baidu.com/"
    session = HTMLSession()
    rsp = session.get(urls)
    head_title = rsp.html.find("#pane-news > div > ul > li.hdline0 > strong > a")
    titles = [head_title[0].full_text,]
    anotherTitles = rsp.html.find("#pane-news > ul:nth-child(n) > li.bold-item > a")
    for iTitles in anotherTitles:
        titles.append(iTitles.full_text)
    session.close()
    return titles

def get_wangyi_news_titles():
    ans_news_titles = []
    urls = "https://news.163.com/"
    session = HTMLSession()
    rsp = session.get(urls)
    head_title = rsp.html.find("#js_top_news > h2.top_news_title > a")
    titles = [head_title[0].full_text,]
    anotherTitles = rsp.html.find("#pane-news > ul:nth-child(n) > li.bold-item > a")
    for iTitles in anotherTitles:
        titles.append(iTitles.full_text)

    session.close()
    return titles

if __name__ == "__main__":
    heads_titles = get_news_titles()
    print(heads_titles)

