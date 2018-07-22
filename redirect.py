#!/usr/bin/env python2
import cgi, socket, json

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
url =  'http://' + ttyd.link( ('54.209.33.120',5000), 10 )

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

