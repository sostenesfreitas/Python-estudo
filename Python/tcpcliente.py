import socket

target_host="216.59.21.13"
target_port=31373
data = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
#create a socket object

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
client.send(bytes(data,'UTF-8'))

#receive some data
response=client.recv(4096)

print (response)
















