from collections import deque
class Friend:
    def __init__(self, email):
        self.email = email
        self.friends = []

    def add_friendship(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def can_be_connected(self, friend):
        queue = deque([self])
        visit = []
        
        while queue:
            cur = queue.popleft()
            visit.append(cur)
            for cfriend in cur.friends:
                if cfriend == friend:
                    return True
                if cfriend not in visit:
                    queue.append(cfriend)
        return False

if __name__ == "__main__":
    a = Friend("A")
    b = Friend("B")
    c = Friend("C")
    
    a.add_friendship(b)
    b.add_friendship(c)
    
    print (a.can_be_connected(c))