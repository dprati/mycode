#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') # this will add 'dns' to the end of our proto list
protoa.append('dns') # this will add 'dns' to the end of our protoa list
print(proto)
proto2 = [22, 80, 443, 53] # this is a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print(protoa)
protob = ['email', 'ftp'] # now create another new list
proto.extend(protob) # now add on protob list items to the end of our proto list
print(proto) # note that this does not nest the protob list
protoa.append(protob) # now add the protob list to the end of the protoa list
print(protoa) # note that this nests the protob list at the end of the protoa list
