# -*- coding: utf-8 -*-
# Python 2.7
import wx

def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read().decode('utf-8'))
    file.close()

def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(contents.GetValue().encode('utf-8'))
    file.close()
  
app = wx.App()
win = wx.Frame(None, title=u"十八哥的编辑器", size=(410, 335))
bkg = wx.Panel(win)


loadButton = wx.Button(bkg, label=u'打开')
loadButton.Bind(wx.EVT_BUTTON, load)

saveButton = wx.Button(bkg, label=u'保存')
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, pos=(5, 35), style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()

