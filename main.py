import connection
import asyncio




token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoicGFibG9nZzAxMUBnbWFpbC5jb20ifQ.xJ3bn0q62KZh8n1IPVS7SscLgx2dejAajl2QwJHsxLs'
newConn = connection.Connection(token)

try:
    asyncio.run(newConn.start())
except KeyboardInterrupt:
    print("Exiting...")