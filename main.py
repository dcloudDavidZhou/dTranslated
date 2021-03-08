"""Powered by deep-translaotr and Jieba AI Model
Design by David Zhou For Raspberry Pi 4B and dCloud XT(X86)
PS: Paddle and Papago is not working with python 3.8, so use fallback mode"""
if __name__ =='__main__':
    """替换词典影视"""
    udb1 = "战栗杀机"
    uda1 = "香蕉鱼"
    udb2 = "偶像梦幻祭"
    uda2 = "合奏之星"
    """替换词典游戏"""
    gab1 = "偶像梦幻祭2"
    gaa1 = "Ensemble Stars 音乐"
    # ここは main 软件's begin
    import jieba
    from deep_translator import GoogleTranslator
    userinput = str(input("请输入中文进行翻译: "))
    userinput = userinput.replace(gab1, gaa1)
    userinput = userinput.replace(udb1, uda1)
    userinput = userinput.replace(udb2, uda2)
    jieba = jieba.cut(userinput) 
    jieba = (" ".join(jieba))
    #print (jieba)
    #print ("完成")
    translated1 = GoogleTranslator(source='zh', target='ja').translate(jieba) 
    translated2 = GoogleTranslator(source='zh', target='en').translate(translated1) 
    #print ("英语:",translateden,'\n'+"日语:",translatedja)
    print ('\n')
    print("英语:",translated2)
