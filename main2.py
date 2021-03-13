"""Powered by deep-translator and TMDB
Design by David Zhou For Raspberry Pi 4B and dCloud XT(X86)
PS: Paddle and Papago is not working with python 3.8, so use fallback mode"""
if __name__ =='__main__':
    from deep_translator import GoogleTranslator
    userinput = userinputfr = str(input("请输入英文进行翻译: "))
    from tmdbv3api import TV
    from tmdbv3api import Movie
    from tmdbv3api import TMDb
    tmdb = TMDb()
    tmdb.api_key = 'your TMDB API here'
    tmdb.language = 'zh'
    tv = TV()
    movie = Movie()
    movies = movie.search(userinput)
    show = tv.search(userinput)
    print('\n')
    for result in movies:
        print(result.title)
        quit()
    for result in show:
        print(result.name)
        quit()
    translated1 = GoogleTranslator(source='en', target='ja').translate(userinput) 
    translated2 = GoogleTranslator(source='ja', target='zh').translate(translated1) 
    print("中文:",translated2)