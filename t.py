# _*_coding:utf-8_*_
from tkitMarker import *
import tkitFile
tfile=tkitFile.File()
text="烈火如歌#作者#这不知名女作家明晓溪经典小说《烈火如歌》已改编成电视剧，并于3月1日开播，主演有周渝民、迪丽热巴、张彬彬、刘芮麟等，人们对剧中的两位新疆美女充满了期待"
P=Pre()
P.args['dropout1']=0.2
P.args['dropout_ratio']=0.2
P.args['rnn_layer']=2
tj=tkitFile.Json(file_path='data/dev.json')
for item in tj.auto_load():
    # print(item['text'])
    print("###"*20)
    its=[]
    for line in zip(item['text'],item['label']):
        its.append(line)
    print(its)

    text= ''.join(item['text'])
    result=P.pre([text])
    print(result)


# {"text": ["烈火如歌#作者#这不知名女作家明晓溪经典小说《烈火如歌》已改编成电视剧，并于3月1日开播，主演有周渝民、迪丽热巴、张彬彬、刘芮麟等，人们对剧中的两位新疆美女充满了期待"], "label": ["KKKKXPPXOOOOOOOB-描述M-描述E-描述OOOOOB-实体M-实体M-实体E-实体OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"]}

# {"text": ["陆垚知马俐#主演#据悉，电影《陆垚知马俐》由文章执导，包贝尔、宋佳、朱亚文、焦俊艳主演，将在7月15日全国上映，并由北京听见时代娱乐传媒有限公司担当该片的独家音乐战略合作伙伴"],
#  "label": ["KKKKKXPPXOOOOOOB-实体M-实体M-实体M-实体E-实体OOOOOOOOOOOOOOOOOOB-描述M-描述E-描述B-关系E-关系OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"]}
