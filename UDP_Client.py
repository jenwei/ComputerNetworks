
import CN_Sockets # CN_Sockets adds ability to interrupt "while True" loop with ctl-C
    

            
class UDP_Client(object):
    """ Computer Networks Chapter 4: Sockets.  UDP Client example. """ 
    
    
    def __init__(self,IP='127.0.0.1', port=7400,Server_Address=("127.0.0.1",5280)):

        socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout

        with socket(AF_INET,SOCK_DGRAM) as sock:
            sock.bind((IP,port))
            sock.settimeout(2.0) # 2 second timeout
            
            print ("UDP_Client started for UDP_Server at IP address {} on port {}".format(
                Server_Address[0],Server_Address[1]))

    
            while True:
                
                str_message = input("Enter message to send to server:\n")

                if not str_message:
                    break
                
                bytearray_message = bytearray(str_message,encoding="UTF-8")

                bytes_sent = sock.sendto(bytearray_message, Server_Address)
                
                print ("{} bytes sent".format(bytes_sent))

                t=0

                while True:
                    try:
                        bytearray_msg, address = sock.recvfrom(1024)
                        source_IP, source_port = address
                        str_message =(bytearray_msg.decode("UTF-8"))
                        print(str_message)
                        t+=1

                    except timeout:
                        break

        print("UDP_Client ended")

    



               
    
                
                
                
            



            
        
