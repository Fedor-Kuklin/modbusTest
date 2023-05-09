# def calculate(val1, val2, oper):
#     match oper.replace(' ',''):
#         case '+':
#             return val1 + val2
#         case '-':
#             return val1 - val2
#         case '*':
#             return val1 * val2
#         case '/':
#             try:
#                 return val1 / val2
#             except:
#                 return "Делить на ноль нельзя"
#         case _:
#             return 'Неизвестная операция'
#
#
# print(calculate(10, 2, '/ +  '))

import wx
from constants import *


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        '''Создаю строку меню'''
        menubar = wx.MenuBar()
        '''создаю выпадающее меню File'''
        fileMenu = wx.Menu()

        '''создаю дополнительное выпадающее меню в меню File'''
        expMenu = wx.Menu()
        '''добавляю пункты в вып.меню'''
        expMenu.Append(wx.ID_ANY, 'Изображения')
        expMenu.Append(wx.ID_ANY, 'Видео')
        expMenu.Append(wx.ID_ANY, 'Данные')

        '''добавляю пункты в меню File'''
        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        '''добавляю вып.меню в меню File после пункта Сохранить'''
        fileMenu.AppendSubMenu(expMenu, "&Экспорт")
        '''добавляю разделительную черту'''
        fileMenu.AppendSeparator()
        '''создаю пункт меню Выход'''
        item = wx.MenuItem(fileMenu, APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        # item = fileMenu.Append(APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        '''добавляю иконку для пункта Выход'''
        item.SetBitmap(wx.Bitmap('exit16.png'))
        '''добавляю пункт Выход в меню File'''
        fileMenu.Append(item)

        viewMenu = wx.Menu()
        self.vSatus = viewMenu.Append(VIEW_STATUS, 'Статусная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)
        '''добавляю меню File в строку меню'''
        menubar.Append(fileMenu, "&File")
        menubar.Append(viewMenu, "&Вид")
        '''добавляю меню в окно'''
        self.SetMenuBar(menubar)

        '''связываю событие пункт меню Выход с методом onQuit'''
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)
        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)

    def onStatus(self, event):
        if self.vSatus.IsChecked():
            print('Показать статусную строку')
        else:
            print('Скрыть статусную строку')

    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print('Режим RGB')
        elif self.vSrgb.IsChecked():
            print('Режим sRGB')

    def onQuit(self, event):
        self.Close()

app = wx.App()
frame = MyFrame(None, title='ModbusMaster')
frame.Show()
app.MainLoop()