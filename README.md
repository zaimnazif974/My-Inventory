Nama    : Zaim Aydin Nazif
NPM     : 2206082524
Kelas   : F
link    : https://zaiminventory.adaptable.app


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Membuat proyek Django baru:
        1. Membuat dan mengaktifkan virtual environtment python pada direktori yang telah ditentukan dengan menjalankan perintah "python -m venv env" kemudian mengaktifkannya dengan perintah "env\Scripts\activate.bat" pada command prompt

        2. Kemudian menyiapkan dependencies dengan membuat file "requirements.txt" yang berisikan:
        - django
        - gunicorn
        - whitenoise
        - psycopg2-binary
        - requests
        - urllib3

        3. Memasang dependencies dengan perintah "pip install -r requirements.txt"

        4. Membuat proyek Django baru bernama "My_Inventory" dengan perintah "django-admin startproject My_Inventory ."

        5. Kemudian merubah value variable ALLOWED_HOSTS menjadi " ["*"] " agar semua host dapat mengakses aplikasi web

    2. Membuat aplikasi main:

        1. Aktifkan virtual environtment

        2. Buat aplikasi bernama main dengan menjalankan perintah "python manage.py startapp <nama aplikasi>" (dalam kasus ini "main")
        
    3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main:

        1. Mendaftarkan aplikasi main ke dalam proyek dengan cara menambahkan "main" pada variable INSTALLED_APPS di dalam settings.py pada direktori proyek django (dalam kasus ini My_Inventory).

        2.  Selanjutnya, saya membuat sebuah template bernama "main.html" di dalam direktori baru bernama "templates" dalam aplikasi "main". File HTML ini akan berperan sebagai tampilan dasar HTML dari halaman yang akan menampilkan Inventory yang saya miliki nantinya

    4. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib:

        1. Membuat class Item pada models.py yang akan merepresantiskan entitas barang yang saya miliki dalam inventory saya.

        2. Membuat atribut-atribut berupa:
            - name = models.CharField(max_length=255): Ini adalah sebuah CharField yang digunakan untuk menyimpan nama item. Maksimal panjang karakter yang diizinkan adalah 255 karakter.
            - date_added = models.DateField(auto_now_add=True): Ini adalah sebuah DateField yang digunakan untuk menyimpan tanggal saat item ditambahkan ke basis data. Parameter auto_now_add=True mengindikasikan bahwa kolom ini akan diatur secara otomatis dengan tanggal saat item dibuat.
            - ammount = models.IntegerField(): Ini adalah sebuah IntegerField yang digunakan untuk menyimpan jumlah barang. Ini mengizinkan Anda untuk menyimpan bilangan bulat.
            - description = models.TextField(): Ini adalah sebuah TextField yang digunakan untuk menyimpan deskripsi barang. TextField cocok untuk menyimpan teks panjang tanpa batasan maksimum panjang karakter.
            - effect = models.CharField(max_length=100, default='None'): Ini adalah CharField yang digunakan untuk menyimpan efek barang. Maksimal panjang karakter yang diizinkan adalah 100 karakter. Default value ('None') adalah nilai yang akan digunakan jika tidak ada nilai yang diset saat membuat instansi Item.
            - category = models.CharField(max_length=100, default='Unknown'): Ini adalah CharField yang digunakan untuk menyimpan kategori barang. Seperti effect, maksimal panjang karakter adalah 100 karakter, dan default value ('Unknown') digunakan jika tidak ada nilai yang diset saat membuat instansi Item.
        
        3. Melakukan migrasi model dengan menjalankan perintah "python manage.py makemigrations" kemudian "python manage.py migrate" pada command prompt. langkah ini bertujuan untuk mengubah struktur tabel basis data sesuai dengan perubahan pada model yang saya buat.

    5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML:

        1. menambahkan perintah "from django.shortcuts import render" untuk mengimport fungsi render dari modul django.shortcuts yang akan digunakan untuk merender tampilan HTML dari file "main.html" yang telah saya buat sebelumnya.
        2. membuat fungsi "show_main" dengan parameter "request" yang berisikan dictionary context dengan key [name, class] dan value [Zaim Aydin Nazif, PBP F] (untuk sementara ini). Fungsi ini mereturn fungsi render dengan parameter request, "main.html, context untuk merender tampilan "main.html".
        3. Ubah nama dan kelas yang sebelumnya dibuat secara statis menjadi key dari value yang telah dibuat dalam dictionary context pada file "views.py"

    6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

        1. melakukan konfigurasi routing URL untuk aplikasi "main" dengan membuat sebuah berkas bernama "urls.py" di dalam direktori "main". Berkas "urls.py" ini memiliki tanggung jawab untuk mengatur rute URL yang terkait langsung dengan aplikasi "main".
        2.  mengonfigurasi routing URL pada tingkat proyek. Hal ini dilakukan dengan menambahkan rute URL yang akan mengarahkan pengguna ke tampilan "main". Rute URL ini ditambahkan ke dalam variabel "urlpatterns" yang terdapat dalam berkas "urls.py" di dalam direktori proyek "My_Inventory". Dengan adanya konfigurasi ini, proyek sekarang memiliki mekanisme yang jelas untuk mengarahkan permintaan URL pengguna ke tampilan yang sesuai di aplikasi "main".

    7. Membuat unit test:
        membuat 4 test yakni:
        1.  test_main_url_is_exist adalah tes untuk mengecek apakah path URL /main/ dapat diakses.
        2.  test_main_using_main_template adalah tes untuk mengecek apakah halaman /main/ di-render menggunakan template main.html.
        3.  test_product_creation memeriksa apakah Item yang telah dibuat pada fungsi setUp sesuai dengan value yang diharapkan.
        4.  test_default_values mengecek apakah default values untuk category dan effect sesuai yang diharapkan

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ![Local Image]("C:\UI\SEM 3\PBP\Tugas\Tugas02\My-Inventory\bagan.png")

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Alasan:
    1. Memungkinkan membuat lingkungan terisolasi sehingga dapat menghindari konflik antara versi paket yang berbeda dalam proyek lainnya
    2. Memudahkan dalam mengelola dependensi proyek.
    3. Virtual environment membantu melindungi sistem dari masalah yang mungkin terjadi akibat perubahan atau pembaruan paket Python.
    
    Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environtment. Akan tetapi hal tersebut tidak disarankan karena dengan tidak menggunakan virtual environtment, kita lebih rentan untuk mendapatkan konflik antar paket dalam proyek-proyek yang kita buat. selain itu aplikasi django kita juga akan rentan akan masalah ketika ada pembaruan paket Python dan juga masalah terkait dependencies.

4. MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah arsitektur desain perangkat lunak yang digunakan untuk mengorganisir dan memisahkan berbagai komponen dalam aplikasi. 

- MVC menggunakan konsep controller untuk mengontrol update pada view ketika ada perubahan model

- MVT View bertanggung jawab merender template yang akan menampilkan data yang dikelola oleh model untuk user sehingga tidak perlu adanya controller seperti yang ada dalam MVC

- MVVM biasanya digunakan  dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama dalam pengembangan perangkat lunak berbasis platform seperti aplikasi mobile dan desktop. Berfungsi untuk merespon secara otomatis perubahan data yang ada dalam model.


