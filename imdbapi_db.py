import pandas as pd
import requests
import time
import json
import csv
import os

print('开始运行')

os.chdir('#') #文件目录

data = []

#电影基础资料下载地址：https://datasets.imdbws.com/ 文件名：title.basics.tsv.gz（用于获取电影的编号） 文件格式是tsv，读取原理与csv相同
tconst = pd.read_csv('~.csv', delimiter=',', encoding='utf-8') #输入文件名称，文件来源见说明
df = pd.DataFrame(tconst)
row_num = df.shape[0] #读取行数

for m in range(0, row_num): #报错时修改这里
    tt = df.iloc[m, 0]
    print(tt)
    
    #先登录账号
    url = "https://imdb-api.com/en/API/Title/#/"+str(tt) #自行申请账号获取token
    response = requests.request("GET", url)
    
    info = json.loads(response.text.encode('utf8'))

    id = info['id'] #编号
    title = info['title'] #名称
    originalTitle = info['originalTitle'] #原始名称
    fullTitle = info['fullTitle'] #全名
    type = info['type'] #类型
    year = info['year'] #年份
    image = info['image'] #图片
    releaseDate = info['releaseDate'] #发布日期
    runtimeMins = info['runtimeMins'] #时长（分钟）
    runtimeStr = info['runtimeStr'] #时长（小时）
    plot = info['plot'] #情节概括
    plotLocal = info['plotLocal']
    plotLocalIsRtl = info['plotLocalIsRtl']
    awards = info['awards'] #已获奖项
    directors = info['directors'] #导演
    directorList = info['directorList'] #导演列表
    writers = info['writers'] #编剧
    writerList = info['writerList'] #编剧列表
    stars = info['stars'] #明星
    starList = info['starList'] #明星列表
    actorList = info['actorList'] #演员列表
    #fullCast = info['fullcast'] #全部演员，加入会报错
    genres = info['genres'] #艺术风格
    genreList = info['genreList'] #艺术风格列表
    companies = info['companies'] #公司
    companyList = info['companyList'] #公司列表
    countries = info['countries'] #国家
    countryList = info['countryList'] #国家列表
    languages = info['languages'] #语言
    languageList = info['languageList'] #语言列表
    contentRating = info['contentRating'] #内容评级
    imDbRating = info['imDbRating'] #imDb评分
    imDbRatingVotes = info['imDbRatingVotes'] #imDb评分票数
    metacriticRating = info['metacriticRating'] #影评人评分
    ratings = info['ratings']
    wikipedia = info['wikipedia'] #维基百科
    posters = info['posters'] #海报
    images = info['images'] #图片
    trailer = info['trailer'] #预告片
    boxOffice_budget = info['boxOffice']['budget'] #预算
    boxOffice_openingWeekendUSA = info['boxOffice']['openingWeekendUSA'] #美国首周末票房
    boxOffice_grossUSA = info['boxOffice']['grossUSA'] #美国总票房
    boxOffice_cumulativeWorldwideGross = info['boxOffice']['cumulativeWorldwideGross'] #累计全球票房
    tagline = info['tagline'] #标语
    keywords = info['keywords'] #关键词
    keywordList = info['keywordList'] #关键词列表

    data.append([id, title, originalTitle, fullTitle, type, year, image, releaseDate, runtimeMins, runtimeStr, plot, plotLocal, plotLocalIsRtl, awards, directors, directorList, writers, writerList, stars, starList, actorList, genres, genreList, companies, companyList, countries, countryList, languages, languageList, contentRating, imDbRating, imDbRatingVotes, metacriticRating, ratings, wikipedia, posters, images, trailer, boxOffice_budget, boxOffice_openingWeekendUSA, boxOffice_grossUSA, boxOffice_cumulativeWorldwideGross, tagline, keywords, keywordList])

print('查找已完成')
with open('~.csv', 'a', newline='', encoding='utf-8') as csvfile:
    #第一次写入用w，往后使用a
    writer = csv.writer(csvfile)
    #header只需要第一次写入
    #writer.writerow(['id', 'title', 'originalTitle', 'fullTitle', 'type', 'year', 'image', 'releaseDate', 'runtimeMins', 'runtimeStr', 'plot', 'plotLocal', 'plotLocalIsRtl', 'awards', 'directors', 'directorList', 'writers', 'writerList', 'stars', 'starList', 'actorList', 'genres', 'genreList', 'companies', 'companyList', 'countries', 'countryList', 'languages', 'languageList', 'contentRating', 'imDbRating', 'imDbRatingVotes', 'metacriticRating', 'ratings', 'wikipedia', 'posters', 'images', 'trailer', 'boxOffice_budget', 'boxOffice_openingWeekendUSA', 'boxOffice_grossUSA', 'boxOffice_cumulativeWorldwideGross', 'tagline', 'keywords', 'keywordList'])
    for row in data:
        writer.writerow(row)
