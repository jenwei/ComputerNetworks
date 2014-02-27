import CN_Sockets
import time
import datetime
import Users

class UDP_Server(object):
    
    def __init__(self,IP="192.168.49.127",port=5280):
        socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
        while True:
            run_the_chat()
    def run_the_chat():
        
        with socket(AF_INET, SOCK_DGRAM) as sock:
            sock.bind((IP,port))
            sock.settimeout(2.0) # 2 second timeout
            Users={}
            MsgList=[]
            AdminList={} #List of Admins (added 2/25/2014} Stores Address and T/F
            BannedList={} #Store Address and T/F
            Times={}
            password='admin'
            MsgCount=0
            print ("UDP Server started on IP Address {}, port {}".format(IP,port))

            while True:
                try:
                    bytearray_msg, address = sock.recvfrom(1024)
                    source_IP, source_port = address
                    
                    ts=time.time()
                    st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    
                    test=address in Users
                    if test==False:
                        Users[address]=st
                        MsgList+=['']
                        Times[st]=MsgCount
                        MsgCount+=1
                        bytearray_message = bytearray('Your IP and port have been added to the system!  Congratulations!' ,encoding="UTF-8")
                        bytes_sent = sock.sendto(bytearray_message, address)
                    elif test==True:
                        if bannedList[address}==False:
                            print ("\nMessage received from IP address {}, port {}:".format(
                                source_IP,source_port))

                            if (bytearray_msg.decode("UTF-8"))[0] == '/':
                                command = bytearray_msg.decode("UTF-8")
                                print (source_IP+': '+command)
                                if command == "/help":
                                    bytearray_message = bytearray("List of avaliable commands are: /admin {}, /adminInfo, /help",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                                if command == "/admin":
                                    bytearray_message = bytearray("Admin permissions require a password to logon!",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                                if command == "/admin "+password:
                                    bytearray_message = bytearray("You are now Admin!(Too bad it doesn't do anything...)",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                                    AdminList[address] = True
                                    
                                    #New command checks added (2/25/2014)
                                    #Note - commands need to be checked (sorry!)
                                if command == "/adminInfo":
                                    bytearray_message = bytearray("If you are an admin, type /admin [password] to logon",encoding="UTF-8")
                                if command == "/logoff":
                                    bytearray_message = bytearray("BYE - you will now be logged off",encoding="UTF-8")
                                    break
                                if "/ban " in command:
                                    if AdminList[address]:
                                        who = command[5:]
                                        BannedList[who] = True
                                        bytearray_message = bytearray("Your ban is now active",encoding-"UTF-8")
                                    else:
                                        bytearray_message = bytearray("You do not have the authority to ban a user",encoding="UTF-8")
                                        
                                else:
                                    bytearray_message = bytearray("The command you entered is not recognized.",encoding="UTF-8")
                                    bytes_sent = sock.sendto(bytearray_message, address)
                        else:
                            bytearray_message=bytearray("You are on the 'banned' list - Contact an Admin to have the ban lifted",encoding="UTF-8")
                            break
                        ##Code below this point has not been modified at all
                        
                        else:
                            LastMsg=Users[address]
                            str_message =[source_IP+': '+(bytearray_msg.decode("UTF-8"))]
                            print(str_message)
                        
                            Times[st]=MsgCount
                            MsgList+=str_message
                        
                            for i in range(Times[LastMsg]+1,Times[st]+1):
                                bytearray_message = bytearray(MsgList[i],encoding="UTF-8")
                                bytes_sent = sock.sendto(bytearray_message, address)

                            MsgCount+=1

                            Users[address]=st
        
                except timeout:
                    print (".",end="",flush=True)
                    continue
                
                
            



            
        
