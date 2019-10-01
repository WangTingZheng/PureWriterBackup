# coding=utf-8
import app.epub as epub
import app.database as db
metadata={'identifier':'123','title':'test','language':'zh-cn','author':'wtz'}

res = db.return_paga()
tit = db.return_title()
for j in range(len(tit)):
    tit[j]=str(tit[j])
    tit[j]= tit[j].replace("('","").replace("',)","")


for i in range(len(res)):
    res[i]=str(res[i])
    res[i] = res[i].replace("('","").replace("',)","").replace("\\u3000\\u3000","<p style=\"text-indent:2em\">",1).replace("\\n\\u3000\\u3000","</p><p style=\"text-indent:2em\">")
    res[i] = res[i].replace("\\n","</p><p>").replace("</p>","",1)
    res[i]=res[i]+"</p>"



epub.main(metadata,res,tit)
