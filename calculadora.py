import wx
import math

class CalculatorFrame(wx.Frame):
    def __init__(self, parent, title):
        super(CalculatorFrame, self).__init__(parent, title=title, size=(300, 400))
        self.InitUI()
        
    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_RIGHT)
        vbox.Add(self.text_ctrl, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=10)
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['√', 'C']
        ]
        
        grid = wx.GridSizer(5, 4, 5, 5)
        
        for label_row in buttons:
            for label in label_row:
                button = wx.Button(panel, label=label)
                button.Bind(wx.EVT_BUTTON, self.OnButtonPress)
                grid.Add(button, 0, wx.EXPAND)
                
        vbox.Add(grid, proportion=1, flag=wx.EXPAND)
        
        panel.SetSizer(vbox)
        
    def OnButtonPress(self, event):
        button = event.GetEventObject()
        label = button.GetLabel()
        
        if label == '=':
            try:
                result = str(eval(self.text_ctrl.GetValue()))
                self.text_ctrl.SetValue(result)
            except:
                self.text_ctrl.SetValue("Error")
        elif label == '√':
            try:
                value = float(self.text_ctrl.GetValue())
                result = math.sqrt(value)
                self.text_ctrl.SetValue(str(result))
            except:
                self.text_ctrl.SetValue("Error")
        elif label == 'C':
            self.text_ctrl.SetValue("")
        else:
            self.text_ctrl.SetValue(self.text_ctrl.GetValue() + label)
            
if __name__ == '__main__':
    app = wx.App()
    frame = CalculatorFrame(None, title='Creative Calculator')
    frame.Show()
    app.MainLoop()
