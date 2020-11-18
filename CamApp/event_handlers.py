import s3logic
import time
import os
import wx

class EventBehaviors:

    def __init__(self,mediactrl,tree): #slider
        self.tree=tree
        self.mc=mediactrl
        #self.slider=slider
        self.bucket="front.cam.storage"
        self.s3client=s3logic.s3logic(self.bucket)
        self.__collapsing = False

    def onPlay(self, evt):
        self.mc.Play()
        #print(self.mc.GetState())
        #if self.mc.GetState()==2:
        #    self.mc.Pause()
        #else:
        #    time.sleep(1)
        #    self.mc.Play()
        #    self.slider.SetRange(0,self.mc.Length())

    def onStop(self, evt):
        print("well howdy")
        self.mc.Stop()

    def onBack(self,evt):
        self.mc.Seek(self.mc.Tell()-1000)
    def onForward(self,evt):
        self.mc.Seek(self.mc.Tell()+1000)

    def doLoad(self,evt):
        self.mc.Stop()
        objectkey=self.tree.GetItemText(self.tree.GetFocusedItem())
        if objectkey==self.bucket:
            return
        print("attempting to download selection")
        filename=self.s3client.downloadFileGiven(objectkey)
        if self.mc.Load(filename) is True:
           print('self.mc.Load was successfull')
           #time.sleep(1)
           return
           #self.mc.Play()
           #print("played?")
           #self.slider.SetRange(0,self.mc.Length())
           #pass
        #else:
        #    print("could not load media")
        #    self.slider.SetRange(0,self.mc.Length())
        #    self.quit(None)


    def OnItemExpanded(self,event):
        prefix=''
        if self.tree.GetItemText(event.GetItem())==self.bucket:
            prefix=''
        else:
            prefix=self.tree.GetItemText(event.GetItem())
        directoryprefixes=self.s3client.getDirectoryPrefixesGiven(prefix,'/')
        self.AddTreeNodes(self.tree.GetFocusedItem(),directoryprefixes)

    def AddTreeNodes(self, parentItem, items):
        for item in items:
            if type(item) == str:
                self.tree.AppendItem(parentItem, item)
            else:
                newItem = self.tree.AppendItem(parentItem, item[0])
                self.tree.SetItemHasChildren(newItem,True)

    def OnItemCollapsed(self,event):
           print("collapsed",event,self)
           if self.__collapsing:
               print("dont put code places when you dont fucking know what it does idoit")
               #event.Veto()
           else:
               self.__collapsing = True
               item = event.GetItem()
               self.tree.CollapseAndReset(item)
               self.tree.SetItemHasChildren(item)
               self.__collapsing = False

    #def onSeek(self, evt):
    #    offset = self.slider.GetValue()
    #   self.mc.Seek(offset)

    def onDownload(self,evt): pass
    def onDelete(self,evt): pass
