class Profile(object):
    def __init__(self, name = "", followers = 0, posts = 0):
        self.name = name
        self.followers = followers
        self.posts = posts
    #getty bois
    def getName(self):
        return self.name
    def getFollowers(self):
        return self.followers
    def getPosts(self):
        return self.posts
    #setty bois
    def setName(self, name):
        self.name = name
    def setFollowers(self, followers):
        self.followers = followers
    def setPosts(self, posts):
        self.posts = posts






