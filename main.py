# coding=utf-8
import app.epub as epub
metadata={'identifier':'123','title':'test','language':'zh-cn','author':'wtz'}
txt1={'head':'this is a head','main':'this is main'}
txt2={'head':'this is a head2','main':'this is main2'}
txt= [txt1,txt2]

epub.main(metadata,txt,2)