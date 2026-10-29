import sys
from PyQt5.QtWidgets import QApplication,QLabel , QWidget ,QPushButton, QLineEdit , QGraphicsColorizeEffect
import copy

class form(QWidget):
    def __init__(self):
        super().__init__()
        self.number = '0'
        self.tedad_clickmos = 0
        self.tedad_click2 = 0
        self.setupUI()
        self.signals()
        self.my_label = []
        self.last_operator = ''
        self.last_operand = ''
        self.after_equal = False
        self.amal = 0
        
    

    def setupUI(self):
        font = QApplication.font()
        font.bold()
        font.setPixelSize(30)
        self.setGeometry(400,400,570,520)
        # self.setWindowTitle("CALCULATOR")
        self.setWindowTitle("Calculator")
        self.lbl1 =QLabel(self, text=str(self.number))
        self.lbl1.setGeometry(120,30,350,50)
        
        self.btnbk = QPushButton(self,text="dele")
        self.btnbk.setGeometry(480,10,55,55)
        self.btn_clear = QPushButton(self,text="clear")
        self.btn_clear.setGeometry(480,100,55,55)
        self.bt1 = QPushButton(self, text="1" )
        self.bt1.setGeometry(100,120,80,80)
        self.bt2 = QPushButton(self, text="2")
        self.bt2.setGeometry(200,120,80,80)
        self.bt3 = QPushButton(self, text="3")
        self.bt3.setGeometry(300,120,80,80)
        self.bt4 = QPushButton(self, text="4")
        self.bt4.setGeometry(100,220,80,80)
        self.bt5 = QPushButton(self, text="5")
        self.bt5.setGeometry(200,220,80,80)
        self.bt6 = QPushButton(self, text="6")
        self.bt6.setGeometry(300,220,80,80)
        self.bt7 = QPushButton(self, text="7")
        self.bt7.setGeometry(100,320,80,80)
        self.bt8 = QPushButton(self, text="8")
        self.bt8.setGeometry(200,320,80,80)
        self.bt9 = QPushButton(self, text="9")
        self.bt9.setGeometry(300,320,80,80)
        self.bt0 = QPushButton(self, text="0")
        self.bt0.setGeometry(200,420,80,80)
        self.btndat = QPushButton(self, text=".")
        self.btndat.setGeometry(100,420,80,80)
                            # (300,120,80,80)
        self.btnPlus = QPushButton(self,text="+")
        self.btnPlus.setGeometry(400,120,80,80)
        self.btnminus =QPushButton(self,text="-")
        self.btnminus.setGeometry(400,220,80,80)
        self.btnmos =QPushButton(self,text="=")
        self.btnmos.setGeometry(400,420,80,80)
        self.btnmultip = QPushButton(self, text="*")
        self.btnmultip.setGeometry( 400,320,80,80)
        self.btndivis = QPushButton(self, text="/")
        self.btndivis.setGeometry(300,420,80,80)
        self.bt0.setFont(font)
        self.bt1.setFont(font)
        self.bt2.setFont(font)
        self.bt3.setFont(font)
        self.bt4.setFont(font)
        self.bt5.setFont(font)
        self.bt6.setFont(font)
        self.bt7.setFont(font)
        self.bt8.setFont(font)
        self.bt9.setFont(font)
        self.btnminus.setFont(font)
        self.btnmos.setFont(font)
        self.btnPlus.setFont(font)
        self.btnPlus.setFont(font)
        self.btnmultip.setFont(font)
        self.btndivis.setFont(font)
        self.lbl1.setFont(font)
        # self.btn_clear.setFont(font)
    def signals(self):
        self.bt1.clicked.connect(lambda : self.btn_click('1'))
        self.bt2.clicked.connect(lambda : self.btn_click('2'))
        self.bt3.clicked.connect(lambda : self.btn_click('3'))
        self.bt4.clicked.connect(lambda : self.btn_click('4'))
        self.bt5.clicked.connect(lambda : self.btn_click('5'))
        self.bt6.clicked.connect(lambda : self.btn_click('6'))
        self.bt7.clicked.connect(lambda : self.btn_click('7'))
        self.bt8.clicked.connect(lambda : self.btn_click('8'))
        self.bt9.clicked.connect(lambda : self.btn_click('9'))
        self.bt0.clicked.connect(lambda : self.btn_click('0'))
        self.btndat.clicked.connect(lambda : self.btn_click('.'))
        self.btnPlus.clicked.connect(lambda : self.btn_click('+'))
        self.btnminus.clicked.connect(lambda : self.btn_click('-'))
        self.btnmos.clicked.connect(lambda : self.btn_click('='))
        self.btnmultip.clicked.connect(lambda : self.btn_click('*'))
        self.btndivis.clicked.connect(lambda : self.btn_click('/'))
        self.btnbk.clicked.connect(self.my_back)
        self.btn_clear.clicked.connect(self.my_clear)
   
    def my_clear(self):
        self.my_num = None
        self.number = "0"
        self.tedad_clickmos = 0
        self.tedad_click2 = 0

        self.last_operator = None
        self.last_operand = None
        self.after_equal = False
        self.lbl1.setText(self.number)
        

    def btn_click(self,n):
        try:
            if n in ('+', '-', '*', '/'):
                self.amal+=1
                if self.tedad_clickmos == 1:
                    self.my_num = self.number
                    self.tedad_clickmos = 0

                if self.number[-1] in ('+', '-', '*', '/'  , '.'):
                    if self.number == '.':
                        print("aaaa")
                    self.number = self.number[:-1] + n
                else:
                    self.number += n

                self.after_equal = False
            elif n == '.':
                last_op = -1
                for i, ch in enumerate(self.number):
                    if ch in ('+', '-', '*', '/'):
                        last_op = i
                
                current_number = self.number[last_op + 1:]
                
                if '.' not in current_number:
                    self.number += n
            elif n == '=':
                self.amal = 0
                if self.tedad_clickmos == 0:

                    self.my_num = copy.deepcopy(self.number)

                    answer = eval(self.number)

                    self.number = str(answer)

                    self.tedad_clickmos = 1
                    self.after_equal = True

                else:
                    self.mosavi_bedo()

            
            else:

                if self.after_equal:

                    self.my_clear()

                    self.number = n

                    self.after_equal = False

                elif self.number == '0':

                    self.number = n
                
                else:

                    self.number += n

            self.lbl1.setText(str(self.number))

        except SyntaxError:
            pass

        except Exception as e:

            print(e)

            self.lbl1.setText("Error")
    def my_back(self):
        if len(self.number) > 1:
            self.number = self.number[:-1]

        else:
            self.number = '0'

        self.lbl1.setText(self.number)
        # le = len(self.number)-1
        # self.number = ''
        # for i in range (le-1):
        #     self.number+=self.number[i]
        #     print(self.number)
        # print("byby")
        # self.close()
    def mosavi_bedo(self):
            
        self.tedad_click2 +=1
        p = int
# پیدا کردن محل عملگر بر اساس عدد
        # if self.my_num.find("+") != -1:
        #     p = self.my_num.find("+")
        # elif self.my_num.find("-") != -1:
        #     p = self.my_num.find("-")
        # elif self.my_num.find("*") != -1:
        #     p = self.my_num.find("*")
        # elif self.my_num.find("/") != -1:
        #     p = self.my_num.find("/")
        
        for i, ch in enumerate(self.my_num):
            if ch in ('+', '-', '*', '/'):
                p = i

        self.arm = self.my_num[p]

        self.start = ''
        for i in range(0,p):
            self.start += self.my_num[i]

        self.end = ''
        for i in range(p+1,len(self.my_num)):
            self.end += self.my_num[i]

        self.last_operator = self.arm
        self.last_operand = self.end

        self.final_mosavi()

    def final_mosavi(self):
        r = eval(
    f"{self.number}{self.last_operator}{self.last_operand}"
)
        self.number = str(r)

        self.lbl1.setText(self.number)
        # final 
        # for i in range(1,self.tedad_click2):            
        #     r = eval(f"{self.start}{self.arm}{self.end}")
        #     print(f"dor : {i}")
        #     print("-----------------------")
        #     print(f"tab  : {r}")
        #     print("-----------------------")
        #     self.start = r
        self.lbl1.setText(f"{r}")
        self.number = str(r)
        

if __name__=='__main__':
    app = QApplication(sys.argv)
    window= form()
    window.show()
    sys.exit(app.exec())
