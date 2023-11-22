# import module
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import *
# import file python instr dan final_win 
from instr import *
from final_win import *
# tambah disini


# buat kelas untuk screen kedua     
class TestWin(QWidget): # kelas turunan QWidget
    # buat konstruktor
    def __init__(self):
        ''' the window which the greeting is located in '''
        # use super.__init__() to inherit all the properties from superclass
        super().__init__()
        # panggil method untuk membuat tampilan UI di layar pertama 
        self.initUI()
        # panggil method untuk ganti/connect ke screen selanjutnya
        self.connects()
        # panggil method untuk menyetel tampilan layar kedua/testing (ukuran , judul layar, dan lokasi)
        self.set_appear()
        # mulai program (tampilkan layar)
        self.show()
        # panggil metode ke self untuk munculkan layar

    # metode untuk setelan tampilan UI screen kedua (testing screen)
    def initUI(self):
        self.button_1 =  QPushButton(txt_sendresults)
        # buat button untuk transisi ke halaman ke 3 dgn text= txt_sendresults
        self.button_2 =  QPushButton(txt_starttest1)
        # buat button untuk mulai tes/timer pertama dgn text= txt_starttest1
        self.button_3 =  QPushButton(txt_starttest2)
        # buat button untuk mulai tes/timer kedua dgn text= txt_starttest2
        self.button_4 =  QPushButton(txt_starttest3)
        # buat button untuk mulai tes/timer ketiga dgn text= txt_starttest3

        '''' buat widget-widget label '''
        self.label_1 =  QLabel(txt_name)
        # buat label untuk tulisan Nama: (txt_name)
        self.label_2 =  QLabel(txt_age)
        # buat label untuk tulisan Umur: (txt_age)
        self.label_3 =  QLabel(txt_test1)
        # buat label dengan tulisan info test pertama (txt_test1)
        self.label_4 =  QLabel(txt_test2)
        # buat label dengan tulisan info test kedua (txt_test2)
        self.label_5 =  QLabel(txt_test3)
        # buat label dengan tulisan info test ketiga (txt_test3)
        self.label_6 =  QLabel(txt_timer)
        # buat label untuk timer (txt_timer)
        

        ''' buat widget-widget text input'''
        self.text_1 =  QLineEdit(txt_hintname)
        # buat text input field untuk masukan nama dengan default text = txt_hintname
        self.text_2 =  QLineEdit(txt_hintage)
        # buat text input field untuk masukan umur dengan default text = txt_hintage
        self.text_3 =  QLineEdit(txt_hinttest1)
        # buat text input field untuk masukan hasil tes 1 dengan default text = txt_hinttest1
        self.text_4 =  QLineEdit(txt_hinttest2)
        # buat text input field untuk masukan hasil tes 2 dengan default text = txt_hinttest2
        self.text_5 =  QLineEdit(txt_hinttest3)
        # buat text input field untuk masukan hasil tes 3 dengan default text = txt_hinttest3

# BATAS
        ''' buat layout '''
        self.vlayout1 = QVBoxLayout()
        # buat vertikal layout 1 (kolom 1)
        self.vlayout2 =  QVBoxLayout()
        # buat vertikal layout 2 (kolom 2)
        self.hlayout =  QHBoxLayout()
        # buat horizontal layout
        ''' add/tambah widget ke layout '''
        # tambahkan widget label timer ke kolom 2 dengan center alignment
        self.vlayout2.addWidget(self.label_6, alignment=Qt.AlignCenter)
        # tambahkan widget label nama ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.label_1, alignment=Qt.AlignLeft)
         # tambahkan widget text input nama ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.text_1, alignment=Qt.AlignLeft)
         # tambahkan widget label umur ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.label_2, alignment=Qt.AlignLeft)
         # tambahkan widget text input umur ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.text_2, alignment=Qt.AlignLeft)
         # tambahkan widget label tes 1 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.label_3, alignment=Qt.AlignLeft)
         # tambahkan widget tombol untuk tes 1 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.button_2, alignment=Qt.AlignLeft)
         # tambahkan widget text inputan hasil tes 1 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.text_3, alignment=Qt.AlignLeft)
         # tambahkan widget label tes 2 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.label_4, alignment=Qt.ALignLeft)
         # tambahkan widget tombol untuk tes 2 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.button_3, alignment=Qt.AlignLeft)
         # tambahkan widget label tes 3 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.label_5, alignment=Qt.AlignLeft)
         # tambahkan widget tombol untuk tes 3 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.button_4, alignment=Qt.AlignLeft)
         # tambahkan widget text inputan hasil tes 2 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.text_4, alignment=Qt.AlignLeft)
         # tambahkan widget text inputan hasil tes 3 ke kolom 1 dengan left alignment
        self.vlayout1.addWidget(self.text_5, alignment=Qt.AlignLeft)
         # tambahkan widget tombol untuk transisi ke layar selanjutnya dengan center alignment
        self.vlayout1.addWidget(self.button_1, alignment=Qt.AlignCenter)
        ''' setelan layout'''
          # tambahkan layout vertikal 1 (kolom 1) ke layout horizontal
        self.hlayout.addLayout(self.vlayout1)
          # tambahkan layout vertikal 2 (kolom 2) ke layout horizontal
        self.hlayout.addLayout(self.vlayout2)
         # setel layout (tambahkan layout horizontal ke self)
        self.setLayout(self.hlayout)
    # metode untuk reaksi dari klik tombol (transisi ke layar ketiga)
    def next_click(self):
        self.win3 = TestWin() # Panggil kelas screen ketiga (final screen)
        self.hide() # sembunyikan screen kedua (diri sendiri)

    def connects(self):
        self.button_1.clicked.connect(self.next_click)
        # sambungkan tombol next dengan fungsi next_click untuk transisi ke layar ketiga


    #''' metode untuk penyetelan main window (judul , lokasi , ukuran) '''

    def set_appear(self):
         # setel judul ke txt_title
        self.setWindowTitle(txt_title)
         # resize main window dengan ukuran win_width dan win_height
        self.resize(win_width, win_height)
         # setel lokasi main window ke x=  win_x dan y = win_y
        self.move(win_x, win_y)
