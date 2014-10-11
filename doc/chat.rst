Chat
#####

Chat Types
==========

#. Room
#. Guild
#. P2P
#. Channel
#. Offline



Protocol
========

The Protocol between the server and client

 +--------+---------------+------------------+
 |         Head           | Body             |
 +--------+---------------+------------------+
 | Opcode | Packet Length |  Raw Data        |
 +--------+---------------+------------------+
 |   8    |    24         | Packet Len -  4  |
 +--------+---------------+------------------+