#控制台显示乱码与保存文件乱码

## 控制台乱码
1.str
  unicodestring =u'\u642d\u5efa\u5e76\u884c\u5904'<br>
  print unicodestring <br>
  这时显示为中文(控制台会自动转化为utf8)<br>
  unicodestring ='\u642d\u5efa\u5e76\u884c\u5904'<br>
  print unicodestring <br>
  这时显示乱码<br>
  string = '\u642d\u5efa\u5e76\u884c'							<br>
  deal_str = string.decode("unicode-escape").encode('UTF-8')				<br>
  print deal_str									<br>
  先将str转化为u'\u642d\u5efa\u5e76\u884c\u5904'（即unicode 解码）（再转化为‘utf8’ 转码）	<br>
										 	<br>
2.list与dict										<br>
  list =[u'\u773c', u'\u8179\u90e8', u'\u4e94\u5b98', u'\u53e3\u8154', u'\u8179\u90e8',u'\u53e3\u8154'] <br>
  2.1
  str_symptom = str(list).replace('u\'','\'')
  print str_symptom.decode("unicode-escape") .encode('UTF-8')<br>
  2.2
  print list[0],list[1]



## 文件保存乱码

主要是list与dict 在保存为文件时乱码
import json
import sys


reload(sys)
sys.setdefaultencoding('utf-8')

line = json.dumps(dict(item))
self.filename.write(line.decode("unicode-escape").decode('utf-8'))


