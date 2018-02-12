# -*- coding:utf-8 -*-
# 
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

unicodestring =u'\u642d\u5efa\u5e76\u884c\u5904\u7406\u7ba1\u9053\uff0c\u611f\u53d7GO\u8bed\u8a00\u9b45\u529b'

print unicodestring

utfstr = unicodestring.encode('UTF-8')



dict = {'introduction': u'\u5e26\u4f60\u5feb\u901f\u4e86\u89e3\u52a8\u6548\u8bbe\u8ba1\u4ee5\u53ca\u4f7f\u7528\u52a8\u6548\u5e2e\u6211\u4eec\u63d0\u5347UX',
 'student': u'\u521d\u7ea7',
 'title': u'UI\u52a8\u6548\u5165\u95e8\u77e5\u8bc6\u50a8\u5907',
 'url': u'http://www.imooc.com/learn/926'}

j = json.dumps(dict)
dict2  = j.decode("unicode-escape").decode("utf-8")

filename = open('example.json','w')

filename.write(dict2)
