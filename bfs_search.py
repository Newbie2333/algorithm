from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []
graph["peggy"] = []


def isMongoSeller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if isMongoSeller(person):
                print(person + " is mongo seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
