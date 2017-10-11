from instapy import InstaPy

session = InstaPy(username='juanchoabdon', password='juanchoabdon1aA', nogui=True) 


session.like_by_tags(['#tech', '#js'], amount=100)


session.login()


session.end()
