import hashlib, sqlite3


def addUser(user, password):
    db=sqlite3.connect('data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT * FROM users'
    for users in c.execute(q):
        if (users[1]==user):
            return False
        
    q='INSERT INTO users ('+str(c.execute(q)[len(c.execute(q))-1]+1)+', '+user+', '+myHashObj.hexdigest()+');'
    c.execute(q)
    return True

def userLogin(user, password):
    db=sqlite3.connect('data/tables.db')
    c=db.cursor()
    myHashObj=hashlib.sha1()
    myHashObj.update(password)
    q='SELECT username FROM users'
    if(user in c.execute(q)):
        q='SELECT pass FROM users WITH username='+user+';'
        if(myHashObj.hexdigest()==c.execute(q)[0]):
            return True
    return False
