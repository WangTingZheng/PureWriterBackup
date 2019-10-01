# coding=utf-8
import app.epub as epub
import app.database as db
metadata={'identifier':'123','title':'test','language':'zh-cn','author':'wtz'}
txt1={'head':'this is a head','main':'this is main'}
txt2={'head':'this is a head2','main':'this is main2'}
txt= [txt1,txt2]
x=[]


res=db.return_paga()

num=0
for i in res:
    i = str(i)
    i = i.replace("('","").replace("\\n\\u3000\\u3000","\n").replace("\\u3000\\u3000","").replace("',)","")
    tx={'head':'this is a head','main':'this is main'}
    tx['head']='head'+str(num)
    tx['main']=i
    num =num+1
    x.append(tx)
epub.main(metadata,x,len(x))
