#print ("Loader server version " + "0.1" + " by Alexandr Krasnow\n")
#print ("Starting server")

import uvicorn
import socket
import settings

from colorama import init
init()
from colorama import Fore, Back, Style



host, port = settings.init ()

if __name__ == '__main__':
    print (Fore.GREEN + "IP" + Style.RESET_ALL + ":       " + str(host))
    print (Fore.GREEN + "PORT" + Style.RESET_ALL + ":     " + str(port))


    uvicorn.run(
        "server:app",
        host=host,
        port=port,
        reload=True
    )