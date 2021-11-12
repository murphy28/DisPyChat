class DisPyChat:
    import requests
    import json
    session = requests.Session()
    jar = requests.cookies.RequestsCookieJar()

    botname = ""
    prefix = ""
    userAgent = ""
    room = {}
    index = 0

    def __init__(self,r,bn="DispoBot",p="!",ua="Disposable Chat Bot"):
        self.botname = bn
        self.prefix = p
        self.room = r
        self.userAgent = ua
        self.connect()

    def connect(self):
        self.session.headers.update({'User-Agent': self.userAgent})
        response = self.session.post('http://www.disposablechat.com/chat', data={
            "room-name": self.room["name"],
            "user-name": self.botname,
            "pass": self.room["password"]
        }, timeout=10)
        self.jar = response.cookies
        self.updateIndex()

    def message(self,msg):
        self.session.post("http://www.disposablechat.com/chat/" + self.room["name"], data={"message_input_window":msg,"noRender":"true"}, cookies=self.jar)

    def newName(self,name):
        self.botname = name
        self.session.post("http://www.disposablechat.com/chat/" + self.room["name"] + "/change-user", data={"new_name":name,"noRender":"true"}, cookies=self.jar)

    def readChat(self,index=index):
        return self.json.loads(self.session.get('http://www.disposablechat.com/chat/' + self.room["name"] + '/ajax?lastId=' + str(index), cookies=self.jar).text)

    def getUsers(self,index=index):
        return self.json.loads(self.session.get('http://www.disposablechat.com/chat/' + self.room["name"] + '/ajax?lastId=' + str(index), cookies=self.jar).text)["users"]

    def updateIndex(self,index=index):
        self.index = self.readChat(index)["lastId"]

    def onMessage(self, func):
        while True:
            if self.readChat(self.index)["chats"] != None:
                latestChats = self.readChat(self.index)["chats"]
                for i in latestChats:
                    func(i["message"],i["user"],i["id"])
                self.updateIndex(self.index)
