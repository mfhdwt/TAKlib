import uuid
import datetime as dt
class Event:
    # Event.py
    # Python implementation of the Class Event
    # represents a TAK event: this class is instantiated with a standard set of
    #    values.
    # Generated by Enterprise Architect
    # Created on: 11-Feb-2020 11:08:07 AM
    # Original author: Corvo
    #

    # event as an XML
    #<?xml version="1.0" encoding="UTF-8" standalone="yes"?><event version="2.0" uid="Linux-ABC.server-ping" type="b-t-f" time="2020-02-14T20:32:31.444Z" start="2020-02-14T20:32:31.444Z" stale="2020-02-15T20:32:31.444Z" how="h-g-i-g-o"> 
        
        #default constructor
    def __init__(self,isPing = 0 ,type = "a-f-G-I" , how = 'm-g' ,isGeochat = 0 ,DATETIME_FMT = "%Y-%m-%dT%H:%M:%SZ", uid = "UIDString" ,version = '2.0', connType=None, lat="00.00000000", lon='00.00000000', le = "9999999.0", ce = "9999999.0", hae = "00.00000000", detailType = 'ping', chatType = None, senderCallsign = None, chatroom = None, groupOwner = None, id = None, parent = None, chatgrpuid0 = None, chatgrpuid1 = None, chatgrpid = None):
        print('initing')
        self.version = version

        self.uid = uid

        self.DATETIME_FMT = DATETIME_FMT

        self.GEOCHATPREFIX = "GeoChat."

        self.type = type
        # flag to determin e if this event is a geo chcat if so, will be added as a
        # prefix to the uid
        self.isGeochat = isGeochat
        
        # starting time when an event should be considered valid
        self.start = "%Y-%m-%dT%H:%M:%SZ"
        # xml header
        self.xmlheader = "<?xml version='1.0' encoding='UTF-8' standalone='yes'?>"
        # basic event
        # Gives a hint about how the coordinates were generated
        self.how = how

        # Schema version of this event instance (e.g.  2.0)
            
        # time stamp: when the event was generated
        self.time = "%Y-%m-%dT%H:%M:%SZ" 
        
        # Hierarchically organized hint about event type (defaultis is 'a-f-G-I'
        # for infrastructure)
        
            # ending time when an event should no longer be considered valid
        self.stale = "%Y-%m-%dT%H:%M:%SZ" 
        
            # Globally unique name for this information on this event can have
            # additional information attached.
        # e.g.  -ping means that this request is a ping
        
        # flag to determin e if this event is a Ping, in this case append to the UID
        self.PINGSUFFIX = "-ping"

        self.isPing = ping
        
        self.setuid()
        self.timer = dt.datetime
        self.now = self.timer.utcnow()
        self.zulu = self.now.strftime(self.DATETIME_FMT)
        self.stale_part = self.now.minute + 1
        if self.stale_part > 59:
            self.stale_part = self.stale_part - 60
            self.stale_now = self.now.replace(minute=self.stale_part)
            self.stale = self.stale_now.strftime(self.DATETIME_FMT)
        self.settime(self.zulu)
        self.setstart(self.zulu)
        self.setstale(self.stale)

        if connType == 'ping':
            from Model.detail import Detail
            from Model.point import Point
            self.detail = Detail(connType)
            self.point = Point(lat=lat, lon=lon, le=le, ce=ce, hae=hae)


        elif connType == 'chat':
            from Model.detail import Detail
            from Model.point import Point
            self.detail = Detail(connType = connType, chatType = chatType, senderCallsign = senderCallsign, chatroom = chatroom, groupOwner = groupOwner, id = id, parent = parent, chatgrpuid0 = chatgrpuid0, chatgrpuid1 = chatgrpuid1, chatgrpid = chatgrpid)
            self.point = Point(lat=lat, lon=lon, le=le, ce=ce, hae=hae)


        #Start getter
    def getstart(self): 
        return self.Start 
    
        # Start setter
    def setstart(self, Start=0):  
        self.Start = Start 
    
        # m_point setter
    def setpoint(self, m_point=0):  
        self.point = m_point
    
        # how getter
    def gethow(self): 
        return self.how 
    
        
    # how setter
    def sethow(self, how=0):  
        self.how = how 

        # uid getter
    def getuid(self): 
        return self.uid 
    
        # uid setter
    def setuid(self, uid=0):  
        a = uuid.uuid1()
        self.uid = str(a)
        if self.isGeochat == 1:
                uid = self.GEOCHATPREFIX + uid
                self.settype('h-g-i-g-o')
        elif self.isPing == 1:
                uid = uid + self.PINGSUFFIX
                self.settype('t-x-c-t')

            # version getter
    def getversion(self): 
        return self.version 
    
        # version setter
    def setversion(self, version):  
        self.version = version 

            # time getter
    def gettime(self): 
        return self.time 
    
        # time setter
    def settime(self, time=0):  
        self.time = time
        
        # stale getter
    def getstale(self): 
        return self.stale 
    
        # stale setter
    def setstale(self, stale=0):
        self.stale = stale 
    
            # type getter
    def gettype(self): 
        return self.type 
    
        # type setter
    def settype(self, type=0):  
        self.type = type