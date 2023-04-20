## Messenger with ZeroMQ
I initally tried to create a messenger app using the `REQ/REP` pattern. However, I realized this wasn't ideal for creating something responsive. So, I spent a while trying to make it using the `PUB/SUB` pattern. However, I while I was able to get the program to send a message to the server.py, I couldn't figure out how to get that server to then distribute the message to the other clients. So, I went back to the `REQ/REP` implementation, because I at least made it far enough to send a message. 

### TLDR: I gave it my best shot.
