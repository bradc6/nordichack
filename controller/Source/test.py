import zmq
c = zmq.Context()
s = c.socket(zmq.REQ)
s.connect("tcp://localhost:5555")
#s.send(b"SETDUTYCYCLE adsf")
s.send(b"SETDUTYCYCLE 0")
#s.send(b"GETSPEEDFREQUENCY")
msg = s.recv()
print("reply: '%s'" % (msg, ))
