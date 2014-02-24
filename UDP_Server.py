import CN_Sockets
import time
import datetime
import Users
class UDP_Server(object):
    

    
    def __init__(self,IP="127.0.0.1",port=5280):

        socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
        
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP,port))
            sock.settimeout(2.0) # 2 second timeout
            
            print ("UDP Server started on IP Address {}, port {}".format(IP,port))

            while True:
                try:
                    bytearray_msg, address = sock.recvfrom(1024)
                    source_IP, source_port = address
                    
                    ts=time.time()
                    st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		    
                    if address not in Users:
                        Users[address]=st
                    elif address in Users:
                        LastMsg=Users[address]
                        print ("\nMessage received from ip address {}, port {}:".format(
                            source_IP,source_port))
                    
                        str_message =source_IP+(bytearray_msg.decode("UTF-8"))
                        
                        Times[st]=MsgCount
                        MsgList+=str_message
                    
                        for i in range(Times[LastMsg],Times[st]):
                            bytearray_message = bytearray(MsgList[i],encoding="UTF-8")
                            bytes_sent = sock.sendto(bytearray_message, address)

                        MsgCount+=1

                        Users[address]=st
        

                except timeout:
                    print (".",end="",flush=True)
                    continue
                
                
            



            
        
