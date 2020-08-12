class DecimalHexConverter:

    def toHex(self, value):
        if value < 16777216:
            for a in range(16):    
                for b in range(16):
                    for c in range(16):
                        for d in range(16):
                            for e in range(16):
                                for f in range(16):
                                    if value == 0:
                                        return self.check([a,b,c,d,e,f])
                                    value -= 1
        else:
            return 'Maksimal angka integer 16.777.215 gan!!!'

    def check(self, list):
        hexnya = ''
        for i in range(6):
            if list[i] == 10:
                list[i] = 'A'
            elif list[i] == 11:
                list[i] = 'B'
            elif list[i] == 12:
                list[i] = 'C'
            elif list[i] == 13:
                list[i] = 'D'
            elif list[i] == 14:
                list[i] = 'E'
            elif list[i] == 15:
                list[i] = 'F'
        
        for item in list:
            hexnya += str(item)

        return hexnya

    def toDecimal(self, value):
        value = str(value)
        arr = []
        if len(value) >6:
            return "Maksimal 6 digit gan"
        else:
            for i in value:
                arr.append(i)
                if 'A' in i: