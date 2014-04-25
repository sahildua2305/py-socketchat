py-socketchat
=============

A simple chat application using sockets programming written in Python

<b>DOCUMENTATION:</b>

1) First of all, run <b>chat_server.py</b>. It will start the socket server to which the various clients can then connect.

2) Now, in a different terminal window, run <b>chat_client.py</b> with proper syntax.

<code>$ python chat_client.py hostname port</code>

which in this case will be: 

<code>$ python chat_client.py localhost 5000</code>

3) Repeat step 2 in different terminal. Now you have 2 clients connected to the server.

Send messages from either of the two and see how they send/receive messages!!

<i><b>Don't forget to have an eye on terminal window running chat_server.py! There must be something interested going on! ;)</b></i>
