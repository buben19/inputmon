#!/usr/bin/env python
from twistedinput.device import EventDevice
from twistedinput.protocol import EventProtocol
from twistedinput.factory import InputEventFactory
from twisted.internet import reactor
import sys
 
class MonitorProtocol(EventProtocol):
 
    def eventReceived(self, event):
        print unicode(event)

def usage():
    pass

def main():
    gamepad = EventDevice(
        MonitorProtocol(InputEventFactory()),
        sys.argv[1])
    gamepad.startReading()
    reactor.run()

if __name__ == '__main__':
    main()
