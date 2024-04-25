import  urllib.request   #引入urllib包中的模块request
import  json          #引入json模块
code='101180101'      #郑州市城市编码
#用字符串变量url保存合成的网址
url='http://www.weather.com.cn/data/cityinfo/%s.html'% code 
print('url=',url)
obj=urllib.request.urlopen(url)   #调用函数urlopen()打开给定的网址，结果返回到对象obj中
print('type(obj)=',type(obj))     #输出obj的类型
data_b=obj.read()             #read()从对象obj中读取内容，内容为bytes字节流数据
print('字节流数据=',data_b)
data_s=data_b.decode('utf-8')    #bytes字节流数据转换为字符串类型
print('字符串数据=',data_s)
#调用JSON的函数loads()将data_s中保存的字符串数据转换为字典型数据
data_dict=json.loads(data_s)
print('data_dict=',data_dict)       #输出字典data_dict的内容
rt =data_dict['weatherinfo']       #取得键为“weatherinfo”的内容
print('rt=',rt)                   # rt仍然为字典型变量
#获取城市名称、天气状况、最高温和最低温
my_rt=('%s,%s,%s~%s')% (rt['city'],rt['weather'],rt['temp1'],rt['temp2'])
print(my_rt)
