
users =[

    { "id":0, "name": "Hero" },

    { "id":1, "name": "Dunn" },

    { "id":2, "name": "Sue" },

    { "id":3, "name": "Chi" },

    { "id":4, "name": "Thor" },

    { "id":5, "name": "Clive" },

    { "id":6, "name": "Hicks" },

    { "id":7, "name": "Devin" },

    { "id":8, "name": "Kate" },

    { "id":9, "name": "Klein" }    

]

friendship = [

    (0, 1),

    (0, 2),

    (1, 2),

    (1, 3),

    (2, 3),

    (3, 4),

    (4, 5),

    (5, 6),

    (6, 7),

    (6, 8),

    (7, 8),

    (8, 9)

]

t = []

def num_friends(users, friendship):

    friends = []
    count = []
    names = []
    friends = [x for row in friendship for x in row]
    friends = list(set(friends))
    for i in friends:
        flag = [x for row in friendship for x in row].count(i)
        count.append(flag)
        
    for x in users: 
        wind = x['name']  
        names.append(wind)
        
    q = []
    global t
    for i in range(0, len(count)):
        q.append([])
        q[i].append(names[i])
        q[i].append(count[i])

    t = sorted(q,key=lambda x: -x[1])
    for i in range(0, len(t)):
        print("{} has {} friends".format(t[i][0],t[i][1]))

def sort_by_num_friends(t):
    num_friends(users, friendship)
    for i in range(0, len(t)):
        print("{} has {} friends".format(t[i][0],t[i][1]))
