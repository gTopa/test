import hashlib, sqlite3


def addUser(user, password):
    db=sqlite3.connect('data/tables.db')
    c=db.cursor()
    d=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT * FROM users'
    c.execute(q)
    userInfo=c.fetchall()
    for data in userInfo:
        if (user in data):
            return False
    q='INSERT INTO users(userID, username, password) VALUES("'+str(userInfo[len(userInfo)-1][0]+1)+'", "'+user+'", "'+myHashObj.hexdigest()+'");'
    print q
    d.execute(q)
    return True

def userLogin(user, password):
    db=sqlite3.connect('data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM users'
    print "hi"
    for data in c.execute(q):
        if(user in data):
            print "bye"
            q='SELECT password FROM users WHERE username = "'+user+'";'
            c.execute(q)
            password=c.fetchall()
            if(myHashObj.hexdigest()==password[0][0]):
                return True
    return False
