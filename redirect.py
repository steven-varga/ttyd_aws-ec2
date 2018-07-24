#!/usr/bin/env python2
import cgi, socket, json, os
import logging

UDP_SERVER_IP = '52.2.17.127'
UDP_SERVER_PORT = 5000

class ttyd_redirector :
    keep_going = True
    server = socket = None

    def __init__( self, timeout ) :
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_.settimeout( timeout )
        self.socket = socket_

    def link( self, server, retry ) :
        msg = None
        for seq in range(1,retry):
            self.socket.sendto(json.dumps( { 'cmd':'gethref','seq':seq }  ), server )
            try :
                frame, address = self.socket.recvfrom(1024)
                msg = json.loads( frame )
                if msg['seq'] == seq :
                    break
            except:
                seq += 1

        # we have our reply
        return msg['href']

ttyd = ttyd_redirector( 2.0 )
url =  'http://' + ttyd.link( (UDP_SERVER_IP,UDP_SERVER_PORT), 10 )

logging.basicConfig( 
    format='%(asctime)s %(message)s', filename='/tmp/h5cpp.log',level=logging.INFO)
env = os.environ
logging.info('%s\t%s\t%s',url,env['REMOTE_ADDR'], env['HTTP_USER_AGENT'] )

print "Status: 302 Moved"
print "Location: %s" % url
print
print '<html>'
print '  <head>'
print '    <meta http-equiv="refresh" content="0;url=%s" />' % url
print '    <title>You are going to be redirected to web based terminal</title>'
print '  </head>' 
print '  <body>'
print '    Redirecting... <a href="%s">free h5cpp trial manual link</a>' % url
print '  </body>'
print '</html>'

