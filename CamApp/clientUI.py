#virtualenv -p /usr/bin/python3.6 /home/friedsteak/CamApp
#source /home/friedsteak/CamApp/bin/activate
"""
stuff to add
rep['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']

include temporary file names within an array so that back/foward can me implemented
"""
import event_handlers
import ui_elements
import wx.media
import time
import os
import wx

class MainWindow(wx.Panel):

    def __init__(self, parent,id,bucketname):
        wx.Panel.__init__(self, parent, -1, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
        try:
            self.mc = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER,size=(640,480))
        except NotImplementedError:
            self.Destroy()
            raise
        self.mc.Load('/home/friedsteak/test.jpg')
        self.mc.ShowPlayerControls(flags=wx.media.MEDIACTRLPLAYERCONTROLS_DEFAULT)
        self.bucket=bucketname
        self.tree = wx.TreeCtrl(self,size=(400,480),style=wx.TR_LINES_AT_ROOT | wx.TR_HAS_BUTTONS)
        root = self.tree.AddRoot(self.bucket)
        self.tree.SetItemHasChildren(root)
        #self.slider = wx.Slider(self, -1, 0, 0, 1, size=wx.Size(640, -1))
        self.sizer = wx.GridBagSizer(0,0)
        ui_objects=ui_elements.Elements(self.sizer,self.mc,self.tree)
        ui_objects.createButtons(self)
        ui_objects.createStaticText(self)
        behaviors=event_handlers.EventBehaviors(self.mc,self.tree) #self.slider
        #self.Bind(wx.EVT_SLIDER,
        #             behaviors.onSeek,
        #             self.slider)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDING,
                     behaviors.OnItemExpanded)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSING,
                     behaviors.OnItemCollapsed)
        self.Bind(wx.EVT_TREE_ITEM_ACTIVATED,
                     behaviors.doLoad)
        self.mc.Bind(wx.media.EVT_MEDIA_LOADED,
                        behaviors.onPlay)
        self.mc.Bind(wx.media.EVT_MEDIA_FINISHED,
                        behaviors.onStop)
        self.sizer.Add(self.tree,(1,0), span=(0,2))
        self.sizer.Add(self.mc, (1,3))
        #self.sizer.Add(self.slider,(2,3))
        #self.size = wx.StaticText(parent, -1, size=(100,-1))
        #self.len = wx.StaticText(parent, -1, size=(100,-1))
        #self.pos = wx.StaticText(parent, -1, size=(100,-1))
        #self.sizer.Add(self.size,(4,3))
        #self.sizer.Add(self.len,(5,3))
        #self.sizer.Add(self.pos,(6,3))
        self.SetSizer(self.sizer)
        
        #self.timer = wx.Timer(self)
        #self.Bind(wx.EVT_TIMER, self.onTimer)
        #self.timer.Start(100)

    #def onTimer(self,evt):
        #offset = self.mc.Tell()
        #self.slider.SetValue(offset)
        #self.size.SetLabel('size: %s ms' % self.mc.Length())
        #self.len.SetLabel('( %d seconds )' % (self.mc.Length()/1000))
        #self.pos.SetLabel('position: %d ms' % offset)


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title="FrontCam Viewer")
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        panel=MainWindow(self,None,"front.cam.storage")
        self.sizer.Add(panel,1,wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Fit()
        #self.Maximize(True)
        self.Show()
        print("I have created a frame and will now append a panel within it!")

if __name__ == "__main__":
    os.system('mkdir tmp')
    print("making an application object")
    app = wx.App()
    top=MainFrame()
    top.Show()
    app.MainLoop()
    print('now removing and cleaning /tmp')
    os.system('rd /s /q tmp')
