
import CN_Sockets # CN_Sockets adds ability to interrupt "while True" loop with ctl-C
    

            
class UDP_Client(object):
    """ Computer Networks Chapter 4: Sockets.  UDP Client example. """ 
    
    
    def __init__(self,Server_Address=("192.168.49.127",5280)):#Server IP and Port to talk to


        socket, AF_INET, SOCK_DGRAM, self.timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout

        self.Server_Address = Server_Address
        with socket(AF_INET,SOCK_DGRAM) as self.sock:
            self.sock.settimeout(0.2) # .2 second timeout
            
            print ("UDP_Client started for UDP_Server at IP address {} on port {}".format(
                self.Server_Address[0],self.Server_Address[1]))

            # Auto sending first message
            self.sendStrMessage("Hello Server!")
            # Recieve response
            self.receiveMessage()

    
            while True:
                
                str_message = input("Enter message to send to server: ")#User input message

                if not str_message:
                    break

                self.sendStrMessage(str_message)
                self.receiveMessage()

        print("UDP_Client ended")
        
    def sendStrMessage(self, message):#Translates message from string to UTF-8 and transmitts
        bytearray_message = bytearray(message,encoding="UTF-8")#Translate
        bytes_sent = self.sock.sendto(bytearray_message, self.Server_Address)#Transmit
        # print ("{} bytes sent".format(bytes_sent))
    
    
    def receiveMessage(self):
        while True:
            try:
                #Attempts to recieve the return message from the server
                bytearray_msg, address = self.sock.recvfrom(1024)
                source_IP, source_port = address
                print(self.decodeMessage(bytearray_msg.decode("UTF-8")))
            
            except self.timeout:
                break #After timeout, returns client to user for next input
    
    def decodeMessage(self, string):
        return self.Message(string)
    
    class Message:
        def __init__(self, message = ""):
            self.message = message
        
        def __str__(self):
            return self.message



    



               
    
                
                
                
            



            
        
