from connection import Connection
import asyncio


def main():
    file = open("/home/pablo/Repositorios/EDA2022/token.txt","r")
    token = file.read()
    file.close()
    
    newConn = Connection(token)

    try:
        asyncio.get_event_loop().run_until_complete(newConn.start())
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == '__main__':
    main()