import time
#open()打开函数 语法：open(name,mode,encoding)
#name：文件名，可以是绝对路径或相对路径。
#mode：打开模式，可选参数，默认值为r，表示以只读方式打开文件。
#encoding：编码格式，可选参数，默认值为None，表示系统默认编码。
f =  open("D:/测试.txt","r",encoding="UTF-8")
print(type(f)) #打印文件对象类型

#读取文件——read()方法
#print(f"读取10个字节的结果：{f.read(10)}")
#print(f"读取剩余所有字节的结果：{f.read()}")

#读取文件——readlines()方法
#lines = f.readlines()  # 读取文件的全部行，封装到列表中
#print(f"lines对象的类型：{type(lines)}")
#print(f"lines对象内容：{lines}")

#读取文件——readline()方法  每次读取一行
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"line1：{line1}")
# print(f"line2：{line2}")
# print(f"line3：{line3}") 

#for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}") 

#关闭文件
#time.sleep(5100)
f.close()

print("-----------------------")
#with open  语法操作文件
with open("D:/测试.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}") 

f.close        

  #文件的写入操作
# 打开文件，不存在的文件
f = open("D:/测试2.txt","w",encoding="UTF-8")
#write()方法写入文件
f.write("hello world\n")
#flush刷新
f.flush()      #将内存中积攒的内容写入到文件的硬盘中
#time.sleep(500000)
f.close()      #关闭文件  close()方法内置了flush功能

#打开一个存在的文件
f = open("D:/测试2.txt","w",encoding="UTF-8")   #w模式打开文件，文件不存在则创建，存在则清空文件内容
#write()方法写入文件
f.write("hello world!!!!!!!!\n")
f.close()      #关闭文件


# #文件追加
# #打开文件，不存在的文件
# f = open("D:/测试3.txt","a",encoding="UTF-8")
# #write()方法写入文件
# f.write("hello world\n")
# #flush刷新
# f.flush()    
# #close关闭
# f.close()      #关闭文件

#打开一个存在的文件
f = open("D:/测试3.txt","a",encoding="UTF-8")  
#write写入，flush刷新，close关闭
f.write("hello world!!!!!!!!\n")
f.close()      