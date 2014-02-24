
import CN_Sockets # CN_Sockets adds ability to interrupt "while True" loop with ctl-C
    

            
class UDP_Client(object):
    """ Computer Networks Chapter 4: Sockets.  UDP Client example. """ 
    
    
<<<<<<< HEAD
    def __init__(self,Server_Address=("192.168.49.127",5280)):
=======
    def __init__(self, myPort = 7890, Server_Address=("127.0.0.1",5280)):
>>>>>>> ca16b5430dde2fb2113c65dfbeb906f8a71b0860

        socket, AF_INET, SOCK_DGRAM, self.timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout

<<<<<<< HEAD
        with socket(AF_INET,SOCK_DGRAM) as sock:
            sock.settimeout(2.0) # 2 second timeout
=======
        self.myPort = myPort
        self.Server_Address = Server_Address
        with socket(AF_INET,SOCK_DGRAM) as self.sock:
            self.sock.bind(('127.0.0.1', myPort)) # invisible to the outside world
            self.sock.settimeout(2.0) # 2 second timeout
>>>>>>> ca16b5430dde2fb2113c65dfbeb906f8a71b0860
            
            print ("UDP_Client started for UDP_Server at IP address {} on port {}".format(
                self.Server_Address[0],self.Server_Address[1]))

            # auto sending first message
            self.sendStrMessage("Hello Server!")
            msg = self.receiveMessage()
            print(msg)

    
            while True:
                
                str_message = input("Enter message to send to server: ")

                if not str_message:
                    break

                self.sendStrMessage(str_message)
                msg = self.receiveMessage()
                print(msg)

        print("UDP_Client ended")
        
    def sendStrMessage(self, message):
        bytearray_message = bytearray(message,encoding="UTF-8")
        bytes_sent = self.sock.sendto(bytearray_message, self.Server_Address)
        # print ("{} bytes sent".format(bytes_sent))
    
    
    def receiveMessage(self):
        t = 0
        while True:
            try:
                
                bytearray_msg, address = self.sock.recvfrom(1024)
                source_IP, source_port = address
                return self.decodeMessage(bytearray_msg.decode("UTF-8"))
            
            except self.timeout:
                t += 1
                print (".",end="",flush=True)
                return
    
    def decodeMessage(self, string):
        return self.Message(string)
    
    class Message:
        def __init__(self, message = ""):
            self.message = message
        
        def __str__(self):
            return self.message


<<<<<<< HEAD
                while True:
                    try:
                        bytearray_msg, address = sock.recvfrom(1024)
                        source_IP, source_port = address
                        str_message =(bytearray_msg.decode("UTF-8"))
                        print(str_message)
=======

>>>>>>> ca16b5430dde2fb2113c65dfbeb906f8a71b0860



    



               
    
                
                
                
            



            
        
