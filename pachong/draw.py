from wordcloud import WordCloud
import jieba
import time

seg_list = jieba.cut("Python123！Python123为你提供优秀的 Python 学习工具、教程、平台和更好的学习体验。", cut_all=True)
word_split = " ".join(seg_list)
print(word_split)
# 显示中文需要的字体，以下是 Windows 系统的设置
# MacOS 中 font_path 可以设置为："/System/Library/fonts/PingFang.ttc"
my_wordclud = WordCloud(background_color='white', font_path = 'C:\Windows\Fonts\simhei.ttf', max_words = 100, width = 1600, height = 800)
# 产生词云
my_wordclud = my_wordclud.generate(word_split)
# 以当前时间为名称存储词云图片
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time())) 
my_wordclud.to_file(now + '.png')