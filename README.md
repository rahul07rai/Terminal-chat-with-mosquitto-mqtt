# Terminal-chat-with-mosquitto-mqtt
a simple terminal based python chat with local mosquitto server and postgres db over websockets

Python Packages required:
jwt
pony
psycopg2
paho-mqtt

Changes:
In the db.py file, change arguments for the db.bind() function as per your database.
In the server.py change the broker_address and port as per your mosquitto server.

Usage:
run client.py to register new user.
run server.py to create chat instance, login and chat with connected user.
run user_text_api.py to get chat for specific user in given timestamp.
