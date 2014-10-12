import httplib, urllib
        
class UGRacingSQLServerConnector():

    def __init__(self, dsn, user, password, database):
        self.dict={}
        self.url=dsn

    def write_tag(self, tag_name, value):
        self.dict[tag_name.upper()]=str(value)
        
    def commit(self):
        params = urllib.urlencode(self.dict)
        urllib.urlopen(self.url, params)

        self.dict={}
