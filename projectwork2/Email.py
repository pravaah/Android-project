import smtplib,getpass

while(True):
  try:
     c=smtplib.SMTP("smtp.gmail.com",587)
     
     x=input("enter email : ") 
     if(x[-10:]=='@gmail.com'):
     
              y=getpass.getpass("enter password : ")

              
              try:
                 
                  c.ehlo()
                  c.starttls()
                  c.login(x,y)
              except:
                  print("either email address or password are incorrect")
                  continue
              else:
                  print("you are successfully logged in")
                  while(True):
                      z=input("enter recievers email address : ")
                      if(z[-10:]=='@gmail.com'):

                           subject=input("Subject : ")
                           message=input("Message : ")
                           
                           
                           try:
                             
                              c.sendmail(x,z,("Subject :"+str(subject)  +"\n\n" +str(message)))
                              c.quit()             
                              break  
                      
                          
                           except:
                              print("entered email address does not exist")
                              continue
                          

                           else:
                              print("entered reciepent email address is invalid,enter again.")
                              continue   
                      else:
                        print("entered email address does not exist,please enter valid email address")     

                  print(" email sent successfully,thaknyou")
                  break

              
     else:
        print("entered email address is invalid,please enter valid email address")  
  except:
    print("please check your network connection ")
    break  
