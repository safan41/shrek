import praw
reddit = praw.Reddit(client_id='FvsbeaJuTBqqvA',
                     client_secret='730UrhjmPn3qwp_4STdnVk7l2K0',
                     password='maryhadalittlelamb',
                     user_agent='testscript by /u/fakebot3',
                     username='pabloitoman')
hot = list(reddit.subreddit('dankmemes').hot())
linkd = []
thelink = []
finlink = []
for sub in hot:
    linkd.append(sub.shortlink)
for id in linkd:
    if linkd.index(id) <= 10:
        thelink.append(id + "\n")
sh = ''.join(thelink)
finlink.append(sh)
shs = ''.join(finlink)
mgs = "Here's what hot on r/dankmemes \n" + shs
print(mgs)