# -*- coding: UTF-8 -*-

'''

Start GUI mode to create the tools, different from the terminal scripts, It is design as production and the platform.
It will become very usefull.
Created on 2018年3月21日

Simply,I use the cross-platform GUI toolkit by wxPython. It provide the 100% native look and feel GUI for application while depend on host os  Mac os, Linux,Windwos.

Reference: https://www.wxpython.org/pages/overview/#hello-world
@author: lizhen
'''


import wx

class HelloFrame(wx.Frame):
    """
    A Frame that says Hello World
    """
    def __init__(self,*args,**kw):
        #Ensure the parent`s __init__ is called
        super(HelloFrame,self).__init__(*args,**kw)
        #Create panel
        pnl = wx.Panel(self)
        #Put text with large bold font on it
        st = wx.StaticText(pnl,label="Hello World",pos=(25,25))
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)
        
        #Create a menu bar
        self.makeMenuBar()
        
        #And a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcom to GUI wxPython!")
    
    def makeMenuBar(self):
        """
        A menu bar is compose of menus
        """
        
        fileMenu = wx.Menu()
        #The "\t...  " syntax defines an accelerator key that also triggers
        helloItem = fileMenu.Append(-1,"&Hello... \tCtrl-H",
                                    "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)
        
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)
        
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu,"&Help")
        
        self.SetMenuBar(menuBar)
        #Finally ,associate a handler function with the eVT_MENU event for 
        #each of teh menu items.
        self.Bind(wx.EVT_MENU,self.OnHello,helloItem)
        self.Bind(wx.EVT_MENU,self.OnExit,exitItem)
        self.Bind(wx.EVT_MENU,self.OnAbout,aboutItem)
        
    def OnExit(self,event):
        """
        Close the frame,terminating the application
        """
        self.Close(True)
    
    def OnHello(self,event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")
        
    def OnAbout(self,event):
        """Display an about dialog"""
        wx.MessageBox("This is a wxPython Hello Wprld sample",
                      "About Hello World,Banrieen",
                      wx.OK|wx.ICON_INFORMATION)
        

if __name__ == "__main__":
    #Start module ,create the app,frame,show it,with event loop
    app = wx.App()
    frm = HelloFrame(None,title='Hello World! Banrieen')
    frm.Show()
    app.MainLoop()
    


