# import module
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import *
# import file python instr
from instr import *

# buat kelas untuk screen kedua     
class TestWin(QWidget): # kelas turunan QWidget
    # buat konstruktor
    def __init__(self, ___): # tambahkan parameter exp (untuk menyimpan hasil inputan user)
        ''' the window which the greeting is located in '''
        super().__init__() # use super.__init__() to inherit all the properties from superclass

        # panggil method untuk membuat tampilan UI di layar terakhir 
        self.initUI()

        # panggil method untuk menyetel tampilan layar ketiga/hasil (ukuran , judul layar, dan lokasi)
        self.set_appear()

        # mulai program (tampilkan layar)
        self.show() # panggil metode ke self untuk munculkan layar


    # metode untuk setelan tampilan UI screen ketiga (final result screen)
    def initUI(self):
        ''' buat widget label '''
        self.roufier = QLabel(txt_index) # setel text txt_index dan hasil dari perhitungan roufier index (panggil property index)
        self.kategori = QLabel(txt_workheart) # setel text txt_workheart dan hasil panggil metode results

        self.layout = QVBoxLayout() # buat vertikal layout
        self.layout.addWidget(self.roufier, alignment = Qt.AlignCenter) # tambahkan widger roufier index ke layout vertikal
        self.layout.addWidget(self.kategori, alignment = Qt.AlignCenter) # tambahkan widget kategori hasil ke layout vertikal
        self.setLayout(self.layout)# setel layout (tambahkan layout vertikal ke self)


    ''' metode untuk penyetelan main window (judul , lokasi , ukuran) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin) # setel judul ke txt_finalwin
        self.resize(win_width, win_height) # resize main window dengan ukuran win_width dan win_height
        self.move(win_x, win_y) # setel lokasi main window ke x=  win_x dan y = win_y
        
   
