# import module
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # checking the types of input values
from PyQt5.QtWidgets import *
# import file python instr dan final_win 
from instr import *
from final_win import *
# tambah disini

class Experiment(): # buat kelas experiment untuk menyimpan data inputan (jawaban user)
    ___ ___(___, ___, ___, ___, ___): # konstruktor kelas dengan parameter : self, age , test1, test2,test3
        # setel tiap properti seperti self.properti = properti
        ___.___ = ___ # setel age 
        ___.___ = ___ # setel test1 
        ___.___ = ___ # setel test2 
        ___.___ = ___ # setel test3

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
        # panggil metode ke self untuk munculkan layar
        self.next_click() # panggil metode ke self untuk munculkan layar

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
        # sambungkan tombol test1 dengan fungsi timer_test untuk memicu timer test 1
        ___.___.___.___(___.___)
        # sambungkan tombol test2 dengan fungsi timer_sits untuk memicu timer test 2
        ___.___.___.___(___.___)
        # sambungkan tombol test3 dengan fungsi timer_final untuk memicu timer test 3
        ___.___.___.___(___.___)

    def timer_test(self): # metode timer untuk test pertama 
        global time # setel variabel time sebagai global variabel
        time = ___(_, _, __) # buat objek time dengan kelas QTime(jam,menit,detik) dimana waktu hanya 15 detik
        ___.timer = ___() # buat objek timer dengan kelas QTimer()
        ___.___.___.___(___.___) # sambungkan timer dengan fungsi timer1Event (agar timer berjalan dan terupdate)
        ___.___.___(1000) # mulai timer dengan metode start


    def timer_sits(self): # metode timer untuk test kedua
        global time
        time = ___(_, _, __) # buat objek time dengan kelas QTime(jam,menit,detik) dimana waktu hanya 30 detik
        ___.timer = ___() # buat objek timer dengan kelas QTimer()
        ___.___.___.___(___.___) # sambungkan timer dengan fungsi timer2Event (agar timer berjalan dan terupdate)
        #one squat in 1.5 seconds
        ___.___.___(1500) # mulai timer dengan metode start


    def timer_final(self): # metode timer untuk test akhir
        global time
        time = ___(_, _, __) # buat objek time dengan kelas QTime(jam,menit,detik) dimana waktu hanya 1 menit
        ___.timer = ___() # buat objek timer dengan kelas QTimer()
        ___.___.___.___(___.___) # sambungkan timer dengan fungsi timer3Event (agar timer berjalan dan terupdate)
        ___.___.___(1000) # mulai timer dengan metode start


    def timer1Event(self):
        global time
        time = ___.___(-1) # gunakan metode addSecs untuk countdown waktu dimana timer berkurang 1 setiap detiknya 
        ___.___.___(___.___("___:___:___")) # setel text timer (label_6) dengan teks waktu yg diubah menjadi string dalam format "hh:mm:ss"
        ___.___.___(___("___", __, ___.___)) # setel font dari text timer (label_6) dengan style "Timer" , ukuran 36  dan format bold
        ___.___.___("color: rgb(0,0,0)") # setel warna tulisan dari label_6 / text timer dengan color: rgb(0,0,0)
        __ ___.___("___:___:___") == "___:___:___": # jika waktu habis (jika time yang diconvert ke string sama dengan "00:00:00")
            ___.___.___() # maka stop timer


    def timer2Event(self):
        global time
        time = ___.___(-1) # gunakan metode addSecs untuk countdown waktu dimana timer berkurang 1 setiap detiknya 
        ___.___.___(___.___("___:___:___")[6:8]) # setel text timer (label_6) dengan teks waktu yg diubah menjadi string dalam format "hh:mm:ss"
        ___.___.___(___("___", __, ___.___)) # setel font dari text timer (label_6) dengan style "Timer" , ukuran 36  dan format bold
        ___.___.___("color: rgb(0,0,0)") # setel warna tulisan dari label_6 / text timer dengan color: rgb(0,0,0)
        __ ___.___("___:___:___") == "___:___:___": # jika waktu habis (jika time yang diconvert ke string sama dengan "00:00:00")
            ___.___.___() # maka stop timer


    def timer3Event(self):
        global time
        time = ___.___(-1) # gunakan metode addSecs untuk countdown waktu dimana timer berkurang 1 setiap detiknya 
        ___.___.___(___.___("___:___:___")) # setel text timer (label_6) dengan teks waktu yg diubah menjadi string dalam format "hh:mm:ss"
        if ___(___.___("hh:mm:ss")[6:8]) __ __: # jika time / waktu diatas 45 detik (waktu : format integer dari time yang diconvert ke string dlm forma "hh:mm:ss")
            ___.___.___("color: rgb(___,___,___)") # maka setel warna tulisan dari text timer / label_6 dengan rgb(0,255,0)
        elif ___(___.___("hh:mm:ss")[6:8]) __ __: # jika time / waktu dibawah 15 detik (waktu : format integer dari time yang diconvert ke string dlm forma "hh:mm:ss")
            ___.___.___("color: rgb(___,___,___)") # maka setel warna tulisan dari text timer / label_6 dengan rgb(0,255,0)
        ___: # selain itu 
            ___.___.___("color: rgb(___,___,___)") # maka setel warna tulisan dari text timer / label_6 dengan rgb(0,20,0)
        ___.___.___(___("___", __, ___.___)) # setel font dari text timer (label_6) dengan style "Timer" , ukuran 36  dan format bold
        __ ___.___("___:___:___") == "___:___:___": # jika waktu habis (jika time yang diconvert ke string sama dengan "00:00:00")
            ___.___.___() # maka stop timer

    #''' metode untuk penyetelan main window (judul , lokasi , ukuran) '''

    def set_appear(self):
         # setel judul ke txt_title
        self.setWindowTitle(txt_title)
         # resize main window dengan ukuran win_width dan win_height
        self.resize(win_width, win_height)
         # setel lokasi main window ke x=  win_x dan y = win_y
        self.move(win_x, win_y)
