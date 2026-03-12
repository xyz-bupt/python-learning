"""
字符串定义规则，并通过规则去验证字符串是否匹配
python正则表达式，使用re模块，并基于re模块中三个基础方法来做正则匹配
分别是：match、search、findall三个基础方法

"""

# re.match(匹配规则, 被匹配字符串)
# 从被匹配字符串开头进行匹配，匹配成功返回匹配对象（包含匹配的信息）,匹配不成功返回空

import re

s = "1python itheima pyhton python"

#match从头匹配
result = re.match("python", s)
print(result)
#print(result.span())
#print(result.group())


#search(匹配规则, 被匹配字符串)
#搜索整个字符串，找出匹配的。从前往后，找到第一个后，就停止，不会继续向后

#search 搜索匹配
result = re.search("python", s)
print(result)

#findall(匹配规则, 被匹配字符串)
#匹配整个字符串，找出全部匹配项

#findall 搜索全部匹配
result = re.findall("python", s)
print(result)





#元字符匹配