import re

#原子：正则表达式中实现匹配的基本单位
#元字符：正则表达式中具有特殊含义的字符

#以普通字符作为原子（匹配一个普通字符）
# a="湖南湖北广东广西"
# pat="湖北"
# result=re.search(pat,a)
# print(result)


#匹配通用字符
#\w 任意字母/数字/下划线 
#\W 和小写w相反 
#\d 十进制数字
#\D 除了十进制数以外的值
#\s 空白字符 
#\S 非空白字符 

# b="136892763900"
# pat2="1\d\d\d\d\d\d\d\d\d\d"
# print(re.search(pat2,b))

# c="@@@@@@@@@@##@!_tdyuhdihdiw"
# pat3=r"\W\w\w"
# print(re.search(pat3,c))



