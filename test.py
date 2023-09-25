import time

def __SetProxy(self, proxy, username, password = (None, None)):
    if proxy == '':
        return None
    ld = None.ld
    (ip, port) = proxy.split(':')
    self.ref.show.emit(self.row, 7, 'Đang set proxy...')
    ld.OpenApp('com.cell47.College_Proxy')
    file = self.ld.DumXml()
    (posok, ok) = self.ld.FindXml('//node[@resource-id="android:id/button1"]', file)
    (posedit, address) = self.ld.FindXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_address"]', file)
    if posok != []:
        pos = posok
    
    if posedit != []:
        pos = posedit
    else:
        time.sleep(1)
    (x, y) = pos[0]
    ld.Click(x, y)
    (pos, addressedit) = self.ld.FindXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_address"]', file)
    if addressedit.attrib['text'] != '' and addressedit.attrib['text'] != 'Now Accepts IP/Domain':
        ld.KeyEvent('KEYCODE_DPAD_DOWN')
        self.__DeleteText(30)
        ld.SendText(ip)
        (pos, portedit) = self.ld.FindXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_port"]', file)
        (x, y) = pos[0]
        ld.Click(x, y)
        if portedit.attrib['text'] != '':
            ld.KeyEvent('KEYCODE_DPAD_DOWN')
            self.__DeleteText(30)
            ld.SendText(port)
            if username != None and password != None:
                (pos, checkuser) = self.ld.FindXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_username"]', file)
                (x, y) = pos[0]
                ld.Click(x, y)
                if checkuser.attrib['text'] != 'Optional' and checkuser.attrib['text'] != '':
                    ld.KeyEvent('KEYCODE_DPAD_DOWN')
                    self.__DeleteText(30)
                    ld.SendText(username)
                    (pos, checkpassword) = self.ld.FindXml('//node[@resource-id="com.cell47.College_Proxy:id/editText_password"]', file)
                    (x, y) = pos[0]
                    ld.Click(x, y)
                    if checkpassword.attrib['text'] != 'Optional' and checkpassword.attrib['text'] != '':
                        ld.KeyEvent('KEYCODE_DPAD_DOWN')
                        self.__DeleteText(30)
                        ld.SendText(password)
                        (pos, _) = ld.FindXml('//node[@text="START PROXY SERVICE"]', file)
                        (x, y) = pos[0]
                        ld.Click(x, y)
                        self.ld.Connect()
                        time.sleep(5)
                        pos = ld.GetPosXml('//node[@text="OK"]')
                        if pos != []:
                            (x, y) = pos[0]
                            ld.Click(x, y)
                            self.ld.Connect()
                            return None
