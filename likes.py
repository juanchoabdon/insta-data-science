from instapy import InstaPy

session = InstaPy(username='juanchoabdon', password='juanchoabdon1aA', nogui=True) 


session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)


session.login()


session.end()
