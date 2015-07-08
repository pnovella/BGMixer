
from Centella.AAlgo import AAlgo
from Centella.physical_constants import *

from Centella.gateWriter import gateWriter
from Centella.gateReader import gateReader

from random import uniform

class BGMixer(AAlgo):

    def __init__(self,param=False,level = 1,label="",**kargs):

        """
        """
        
        self.name='BGMixer'
        
        AAlgo.__init__(self,param,level,self.name,0,label,kargs)
        
        try: self.odstname = self.strings["OUTPUT_DST_NAME"]
        
        except KeyError: self.odstname = "MixedBG.root" 

        try: self.idstname1 = self.strings["INTPUT_DST_NAME_1"]
        
        except KeyError: self.m.fatalError("No input file defined!") 
        
        try: self.idstname2 = self.strings["INTPUT_DST_NAME_2"]
        
        except KeyError: self.m.fatalError("No input file defined!") 


    def initialize(self):

        """
        """
        
        self.m.log(1,'+++Init method of BGMixer algorithm+++')
        
        self.writer = gateWriter()
        
        self.writer.open(self.odstname)
        
        self.reader1 = gateReader()
        
        self.reader1.open(self.idstname1)

        self.reader2 = gateReader()

        self.reader2.open(self.idstname2)
        
        return

   
    def finalize(self):

        self.m.log(1,'+++End method of BGMixer algorithm+++')
        
        ok = True

        while ok:

            bgtype = uniform(0,1)

            if bgtype<0.5:
                
                event = self.reader1.read()
                
                if self.reader1.eof(): ok = False
                
            else:     
                
                event = self.reader2.read()
                
                if self.reader2.eof(): ok = False
                
            self.writer.write(event)

        self.m.log(1,"EOF reached in one of the input files")

        self.m.log(1,"Closing output file:",self.odstname)

        self.writer.close()

        return

    
