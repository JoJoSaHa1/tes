# import module
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import *
# import file python instr
from PyQt5.QtWidget import *
from instr import *

# buat kelas untuk screen kedua     
class TestWin(QWidget): # kelas turunan QWidget
    # buat konstruktor
    def __init__(self, ___): # tambahkan parameter exp (untuk menyimpan hasil inputan user)
        ''' the window which the greeting is located in '''
        super().__init__() # use super.__init__() to inherit all the properties from superclass

        #setel properti exp
        ___.___ = ___
        # panggil method untuk membuat tampilan UI di layar terakhir 
        self.initUI()

        # panggil method untuk menyetel tampilan layar ketiga/hasil (ukuran , judul layar, dan lokasi)
        self.set_appear()

        # mulai program (tampilkan layar)
        self.show() # panggil metode ke self untuk munculkan layar


    # metode untuk setelan tampilan UI screen ketiga (final result screen)
    def initUI(self):
        ''' buat widget label '''
        self.roufier = QLabel(txt_index + str(___.___)) # setel text txt_index dan hasil dari perhitungan roufier index (panggil property index)
        self.kategori = QLabel(txt_workheart + ___.___()) # setel text txt_workheart dan hasil panggil metode results

        self.Qlayout = QVBoxLayout() # buat vertikal layout
        self.layout.addWidget(self.roufier, alignment = Qt.AlignCenter) # tambahkan widger roufier index ke layout vertikal
        self.layout.addWidget(self.kategori, alignment = Qt.AlignCenter) # tambahkan widget kategori hasil ke layout vertikal
        self.setLayout(self.Qlayout)# setel layout (tambahkan layout vertikal ke self)


    ''' metode untuk penyetelan main window (judul , lokasi , ukuran) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin) # setel judul ke txt_finalwin
        self.resize(win_width, win_height) # resize main window dengan ukuran win_width dan win_height
        self.move(win_x, win_y) # setel lokasi main window ke x=  win_x dan y = win_y
        
    ''' metode untuk menghitung indeks roufier dari inputan user dan juga kategori kesehatan berdasarkan indeks yang dihitung '''
    def results(self):
        __ ___.___.___ _ _: #  jika umur pengguna (property age dari exp diri sendiri) dibawah 7 
            ___.index = _ # setel property index menjadi 0
            return "____" # kembalikan nilai "there is no data for this age"
        # hitung nilai indeks sesuai rumus roufier yaitu index = 4  * ((t1+t2+t3) -200) / 10
        ___.___ = (_ * (___(___.___.___) + ___(___.___.___) + ___(___.___.___)) - ___) / ___
        __ ___.___.___ == _ __ ___.___.___ == _: # jika umur pengguna 7 ATAU 8 
            __ ___.___ __ ___: # jika hasil indeks lebih besar atau sama dengan  21
                return ___ # kembalikan hasil txt_res1
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 21 DAN diatas atau sama dengan 17
                ___ ___ # kembalikan hasil txt_res2
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 17 DAN >= 12
                ___ ___ # kembalikan txt_res3
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 12 DAN >= 6.5
                ___ ___ # kembalikan txt_res4
            ____:  
                ___ ___ # selain itu kembalikan txt_res5
        
        __ ___.___.___ == _ __ ___.___.___ == _: # jika umur pengguna 9 ATAU 10 
            __ ___.___ __ ___: # jika hasil indeks lebih besar atau sama dengan  19.5
                return ___ # kembalikan hasil txt_res1
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 19.5 DAN diatas atau sama dengan 15.5
                ___ ___ # kembalikan hasil txt_res2
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 15.5 DAN >= 10.5
                ___ ___ # kembalikan txt_res3
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 10.5 DAN >= 5
                ___ ___ # kembalikan txt_res4
            ____:  
                ___ ___ # selain itu kembalikan txt_res5

        __ ___.___.___ == _ __ ___.___.___ == _: # jika umur pengguna 11 ATAU 12 
            __ ___.___ __ ___: # jika hasil indeks lebih besar atau sama dengan  18
                return ___ # kembalikan hasil txt_res1
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 18 DAN diatas atau sama dengan 14
                ___ ___ # kembalikan hasil txt_res2
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 14 DAN >= 9
                ___ ___ # kembalikan txt_res3
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 9 DAN >= 3.5
                ___ ___ # kembalikan txt_res4
            ____:  
                ___ ___ # selain itu kembalikan txt_res5

        __ ___.___.___ == _ __ ___.___.___ == _: # jika umur pengguna 13 ATAU 14 
            __ ___.___ __ ___: # jika hasil indeks lebih besar atau sama dengan  16.5
                return ___ # kembalikan hasil txt_res1
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 16.5 DAN diatas atau sama dengan 12.5
                ___ ___ # kembalikan hasil txt_res2
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 12.5 DAN >= 7.5
                ___ ___ # kembalikan txt_res3
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 7.5 DAN >= 2
                ___ ___ # kembalikan txt_res4
            ____:  
                ___ ___ # selain itu kembalikan txt_res5

        if ___.___.___ >= 15: # jika umur >= 15
            __ ___.___ __ ___: # jika hasil indeks lebih besar atau sama dengan  15
                return ___ # kembalikan hasil txt_res1
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 15 DAN diatas atau sama dengan 11
                ___ ___ # kembalikan hasil txt_res2
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 11 DAN >= 6
                ___ ___ # kembalikan txt_res3
            elif ___.___ _ ___ and ___.___ __ __: # jika hasil indeks dibawah 6 DAN >= 0.5
                ___ ___ # kembalikan txt_res4
            ____:  
                ___ ___ # selain itu kembalikan txt_res5
