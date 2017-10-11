from instapy import InstaPy
session = InstaPy(username='juanchoabdon', password='juanchoabdon1aA', nogui=True)
session.login()
session.set_do_follow(enabled=True, percentage=10)
session.follow_user_followers(['freddiervega'], amount=500, random=False, sleep_delay=01)
session.set_sleep_reduce(01)
session.end()
