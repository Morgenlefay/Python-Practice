# WordCloud.py
import jieba
import imageio
import wordcloud

# 读取文件
file = open('WordCloud/红楼梦.txt','rt', encoding = 'utf-8')
text = file.read()
file.close()

ls = jieba.cut(text) #分词
txt = " ".join(ls)

stopwords = {'我们':0, '你们':0, '他们':0, '那里':0, '这里':0, '一个':0} #噪声词
mk =imageio.imread("WordCloud/love.jpeg")
color_new = wordcloud.ImageColorGenerator(mk)

w = wordcloud.WordCloud()
w = wordcloud.WordCloud(font_path = 'WordCloud/msyh.ttf',
                        width = 1000,
                        height = 700,
                        stopwords = stopwords,
                        background_color = 'white',
                        contour_color = 'gray',
                        color_func = color_new,
                        mask = mk,
                        max_words = 100)
w.generate(txt)
w.to_file("txt.eps")
