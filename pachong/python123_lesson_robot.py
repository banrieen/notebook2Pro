import urllib.robotparser
from urllib.parse import urlparse

url = 'https://ai.baidu.com'
def asert_robot_pages(url):
    rp = urllib.robotparser.RobotFileParser()
    domain = urlparse(url).netloc
    rp.set_url('https://' + domain + '/robots.txt')
    rp.read()
    if rp.can_fetch("*", url):
        return True
    else:
        return False
    print(info)

def main(urlList):
    for iUrl in urlList:
        if iUrl and asert_robot_pages(iUrl):
            print("{} can be fetched! ".format(iUrl))


urlList = ['https://ai.baidu.com/product/pingo', 'https://ai.baidu.com/tech/speech/asr']
main(urlList)