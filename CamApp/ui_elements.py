import event_handlers
import wx


class Elements:


    def __init__(self,sizer_object,mediactrl_object,tree): #slider
        self.sizer=sizer_object
        self.mc=mediactrl_object
        #<class 'wx._media.MediaCtrl'> <class 'wx._core.Slider'> <class 'wx._core.TreeCtrl'>
        self.behavior=event_handlers.EventBehaviors(self.mc,tree) #slider

    def buttonData(self):
        return {
               #    "label": "P","event": self.behavior.onPlay,
               #    "sizer": "22","size": (16,16)
               #},{
               #    "label": "S","event": self.behavior.onStop,
               #    "sizer": "24","size": (16,16)
               #},{
                   "label": "Download","event": self.behavior.onDownload,
                   "sizer": "20","size": wx.DefaultSize
               },{
                   "label": "Delete","event": self.behavior.onDelete,
                   "sizer": "21","size": wx.DefaultSize

               },{
                   "label": "<","event": self.behavior.onBack,
                  "sizer": "12","size": (20,480)
               },{
                  "label": ">","event": self.behavior.onForward,
                  "sizer":"14","size": (20,480)}
		
    def createButtons(self,panel):
        for eachButton in self.buttonData():
                button = self.buildOneButton(panel,
                             eachButton["label"],
                             eachButton["event"],
                             eachButton["sizer"],
                             eachButton["size"])
    def buildOneButton(self,parent,label,handler,sizer,size):
        button = wx.Button(parent,-1,label,size=size)
        parent.Bind(wx.EVT_BUTTON, handler, button)
        parent.sizer.Add(button,(int(sizer[0]),int(sizer[1])))
        return button



    def staticTextData(self):
        return (("Naviagtion Tree","00"),
                ("Motion Video","03"))
    def createStaticText(self,panel):
        for eachLabel, eachSizer in self.staticTextData():
            text = self.buildOneStaticText(panel,eachLabel,eachSizer)
    def buildOneStaticText(self,parent,label,sizer):
        text = wx.StaticText(parent, -1, size=(100,-1))
        text.SetLabel(label)
        parent.sizer.Add(text,(int(sizer[0]),int(sizer[1])))
        return text


    #an idea on how to implement this? data structure outside the program with uqiue ids to idenify Elements

























    #put the tree control into ui_elements create a treectrl object within a panel of a sizer inside the frame class
    #have events inside the frame class that create another panel with the media inside it
"""
class ElementsInPanels:

    def __init__(self,parent):
        self.parent_frame=parent

    def createNavigationTreePanel(self):
        panel = wx.Panel(self,frame,-1)
        tree = wx.TreeCtrl(self.parent,size=(400,480),style=wx.TR_LINES_AT_ROOT | wx.TR_HAS_BUTTONS)
        root = self.parent.tree.AddRoot(self.bucket)
        panel.tree.SetItemHasChildren(self.root)
        return panel, tree

    def createMediaInPanel(self,frame):
        panel = wx.Panel(self,frame,-1)
        try:
            panel.mc = wx.media.MediaCtrl(self, style=wx.SIMPLE_BORDER)
        except NotImplementedError:
            panel.Destroy()
            raise
        slider = wx.Slider(self, -1, 0, 0, 0, size=wx.Size(640, -1))
        #panel.Bind(wx.EVT_SLIDER, Behaviors.onSeek, slider)
        return panel, slider

    def overlayMediaInPanelWithControlsInPanel(self):
        panel = wx.Panel(self,frame,-1)
        return panel
"""
