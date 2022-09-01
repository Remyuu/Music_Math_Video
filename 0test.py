import pickle
class tick:
    name = '牛牛牛'
    age = 10
samp = [1,2,3,'aaa',[12,3],tick()]
with open('te.xxxx','wb') as pickle_file:
   #序列化samp对象，以二进制的方式写到文件
   pickle.dump(samp,pickle_file)
##################################################

with open('te.xxxx','rb') as pickle_file:
   #反序列化对
   samp_read = pickle.load(pickle_file)
   print(samp_read[5].name)

