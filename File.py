n = input()
adj = dict()
level = dict()


def bfs(s, par):
    level.update(dict([(s, 0)]))
    queue = [s]
    while queue:
        v = queue.pop(0)
        if v in adj:
            for w in adj.get(v):
                if w == par:
                    print("Yes")
                    return
                if level.get(w) is -1:
                    queue.append(w)
                    level.update(dict([(w, level.get(v) + 1)]))
    print("No")


for i in range(int(n)):
    line = input()
    if line.find(":") != -1:
        cur_class, parent = line.split(" : ")
        l = list(parent.split())

        newlist = []
        for i in range(len(l)):
            newlist.append(l[i])

        if cur_class in adj:
            previous = adj.get(cur_class)
            newlist.append(previous)

        new = dict([(cur_class, newlist)])
        adj.update(new)
        level.update(dict([(cur_class, -1)]))

for i in range(int(input())):
    parent, cur_class = input().split()
    if parent == cur_class:
        print("Yes")
    else:
        for key in level:
            level.update(dict([(key, -1)]))
        bfs(cur_class, parent)