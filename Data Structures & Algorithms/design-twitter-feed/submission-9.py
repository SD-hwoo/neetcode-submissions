import heapq

class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.tweets:
            # self.tweets[userId] = heapq.heapify([tweetId])
            self.tweets[userId] = [(self.time, tweetId)]
        else:
            # heapq.heappush(self.tweets[userId], tweetId)
            self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.time += 1
        sorted_tweets = []
        if userId in self.following:
            for user in self.following[userId]:
                slicer = min(len(self.tweets[user]), 10)
                sorted_tweets.extend(self.tweets[user][-slicer:])
        if userId in self.tweets:
            slicer = min(len(self.tweets[userId]), 10)
            sorted_tweets.extend(self.tweets[userId][-slicer:])  
        heapq.heapify_max(sorted_tweets)
        newsfeed = []
        for _ in range(10):
            if sorted_tweets:
                newsfeed.append(heapq.heappop_max(sorted_tweets)[1])
        
        return newsfeed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followerId not in self.following:
            self.following[followerId] = set([followeeId])
        else:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
