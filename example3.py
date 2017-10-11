
from instapy import InstaPy
session = InstaPy(username='juanchoabdon', password='juanchoabdon1aA')
session.login()

session.set_do_follow(enabled=True, percentage=10)
session.like_by_tags(['#tech','#entrepreneurship','#programming'], amount=100)
session.follow_user_followers(['cvandercito'], amount=500, random=False, sleep_delay= 01)
session.set_sleep_reduce(01)

session.end()
