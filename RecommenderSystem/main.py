# main.py
# simulate different requests coming into the system

from Webserver import WebServer, Request, Action

configMap = {"numberToServe": 10, "data_dir": "DATA"}
server = WebServer(configMap)
server.start() # load all the data in the database, start the first model training

reqX1 = Request(userId='X1') # X1 represents an anonymous user
req1 = Request(userId=1) # using integer to represent a registered user
print(reqX1)
print(req1)

recX1 = server.renderRecommendation(reqX1)
print(recX1) # give the recommendation to the anonymous user

# rec1 = server.renderRecommendation(req1)
# print(rec1)

# user 1 gives rating of 5 for item 255
action1 = Action(1, 255, 5)
print(server.getFromInventory(255))
server.getAction(action1)
rec1_afteraction = server.renderRecommendation(req1)
print(rec1_afteraction)

# anonymous user X1 gives rating of 5 for item 123
actionX1 = Action('X1', 123, 5)
print(server.getFromInventory(123))
server.getAction(actionX1)
recX1_afteraction = server.renderRecommendation(reqX1)
print(recX1_afteraction)

server.increment()
recX1_aftercleaning = server.renderRecommendation(reqX1)
print(recX1_aftercleaning) # will give the same result as before the actionX1

req19 = Request(userId=19) # the one with very few history, new user
rec19 = server.renderRecommendation(req19)
print(rec19)