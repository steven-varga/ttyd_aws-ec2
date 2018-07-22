
TTYD utilities for distributed service
======================================

ttyd_node
------------
creates random user `h5cpp_####`, runs ttyd at port `-p ####` and removes user account when finished
```bash
usage: ttyd_node [-h] [-p PORT] [-s SERVER] [-t TIMEOUT] [--port-min PORT_MIN]
                 [--port-max PORT_MAX]

this client connects to server, the client must have h5cpp group defined

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  udp port to connect
  -s SERVER, --server SERVER
                        server to connect
  -t TIMEOUT, --timeout TIMEOUT
                        socket timeout
  --port-min PORT_MIN   min random port ttyd listens at
  --port-max PORT_MAX   max random port ttyd listens at
```

ttyd_master
------------
```bash
usage: ttyd_master [-h] [-t TIMEOUT] [-p PORT] [-l LINK]

    TTYD  CONTROLLER
    layered on UDP with REQ-REP-ACK protocol tracks running number of instances, and be polled by python call
    ttyd_link. Consumed link must be connected to with html redirect so the resource is closed when connection 
    breaks

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        socket timeout
  -p PORT, --port PORT  udp port listen at
  -l LINK, --link LINK  link to redirect if all ttyd services are busy
```


ttyd_link | redirect.py
------------------------

pulls html link from master queue, and redirects html request. If the aws-ec2 nodes are saturated the returned link is the webpage
specified with `ttyd_master --link parking_page.html`

```bash
usage: ttyd_link [-h] [-t TIMEOUT] [-r RETRY] [-p PORT] [-s SERVER]

retrieves an href link from ttyd_queue

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        packet timeout
  -r RETRY, --retry RETRY
                        max retry after transmission failure
  -p PORT, --port PORT  udp port listen at
  -s SERVER, --server SERVER
                        ttyd_master ip address

```
