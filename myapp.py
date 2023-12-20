# import module
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import *
# import file python instr dan second_win 
from instr import *
from second_win import *

# buat kelas untuk screen pertama     
class MainWin(QWidget): # kelas turunan QWidget
    # buat konstruktor
    def __init__(self):
        ''' the window which the greeting is located in '''
        super().__init__() # use super.__init__() to inherit all the properties from superclass

        # panggil method untuk membuat tampilan UI di layar pertama 
        self.initUI()

        # panggil method untuk ganti/connect ke screen selanjutnya
        self.connects()

        # panggil method untuk menyetel tampilan layar utama (ukuran , judul layar, dan lokasi)
        self.set_appear()

        # mulai program (tampilkan layar)
        self.show() # panggil metode ke self untuk munculkan layar
    # metode untuk setelan tampilan UI screen pertama
    def initUI(self):
        ''' creates graphic elements '''
        self.button = QPushButton(txt_next, self) #buat objek button/tombol dengan text = txt_next dan parameter ke 2 self 
        self.label1 = QLabel(txt_hello) # buat tulisan/label opening dengan teks txt_hello
        self.label2 = QLabel(txt_instruction) # buat label instruksi dengan teks = txt_instruction


        self.vlayout = QVBoxLayout() # buat layout vertikal
        self.vlayout.addWidget(self.label1, alignment = Qt.AlignLeft) # tambahkan widget label opening ke layout vertikal dengan left alignment
        self.vlayout.addWidget(self.label2, alignment = Qt.AlignLeft) # tambahkan widget label instruksi ke layout vertikal dengan left alignment
        self.vlayout.addWidget(self.button, alignment = Qt.AlignCenter) # tambahkan widget tombol ke layout vertikal dengan center alignment   
        self.setLayout(self.vlayout) # setel layout (tambahkan layout vertikal ke self)
    # metode untuk reaksi dari klik tombol (memunculkan layar kedua)
    def next_click(self):
        self.tw = TestWin() # Panggil kelas screen kedua
        self.hide() # sembunyikan screen pertama (diri sendiri)


    def connects(self):
        # sambungkan tombol dengan fungsi next_click untuk memicu transisi screen saat klik tombol
        self.button.clicked.connect(self.next_click) 

    ''' metode untuk penyetelan main window (judul , lokasi , ukuran) '''
    def set_appear(self):
        self.setWindowTitle(txt_title) # setel judul ke txt_title
        self.resize(win_width, win_height) # resize main window dengan ukuran win_width dan win_height
        self.move(win_x, win_y) # setel lokasi main window ke x=  win_x dan y = win_y

def main():
    app = QApplication([]) # buat aplikasi
    mw = MainWin() # panggil kelas untuk mainwindow (menampilkan main window)
    app.exec_() # setelan agar app berjalan terus

main()
