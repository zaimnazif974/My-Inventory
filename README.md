**Nama    : Zaim Aydin Nazif**
**NPM     : 2206082524**
**Kelas   : F**



TUGAS 04:

**Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**

UserCreationForm adalah class bawaan dari Django yang digunakan untuk memudahkan untuk proses pembuatan form registrasi pengguna dan menyimpannya ke dalam database. Class ini memungkinkan developer untuk membuat form registrasi tanpa menulis kode dari awal.

    - Kelebihan:
        1. Mudah diimplementasikan: UserCreationForm menyederhanakan proses pembuatan form registrasi tanpa tanpa menulis custom form registrasi dari nol.
        2. Integrasi: UserCreationForm terintegrasi dengan autentikasi bawaan yang disediakan oleh django, sehingga developer mudah dalam mengimplementasikan keduanya.
        3. Validasi: UserCrationForm menyediakan fitur konfirmasi password, kompleksitas password, dan keunikan username yang dapat membantu untuk menyimpan dan mengamankan data bagi sisi developer dan memudahkan user untuk membuat akun yang aman dan unik.

    - Kekurangan:
        1. Fields yang dibatasi: UserCreationFrom hanya memiliki fields untuk username, password1, dan password2. Jika developer ingin menambahkan fields data tambahan seperti email, nomor HP, alamat, dan lain-lain , maka developer harus membuat custom form sendiri.
        2. Tampilan default yang tidak sesuai: tampilan default UserCreationForm mungkin tidak sesuai dengan desain aplikasi web yang diinginkan oleh developer sehingga Ia perlu menghabiskan waktu untuk menyesuaikannya
        3. Tidak fleksibel: UserCreationForm tidak cocok diimplementasikan untuk aplikasi web yang memiliki sistem registrasi yang kompleks karena terbatasnya fields yang dimiliki.

**Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

Autentikasi:
    - Autentikasi adalah proses untuk mengidentifikasi user atau identitas. Proses ini menjawab pertanyaan "Kamu siapa?"
    - Dalam Django proses autentikasi dapat diimplementasikan menggunakan sistem autentikasi bawaan yakni autentikasi berdasarkan username & password, berdasarkan token, dan lain-lain. 
    - Autentikasi mengatur sesi user dengan proses login-logout

Otorisasi:
    - Otorisasi adalah proses untuk mengidentifikasi aksi atau data apa yang dapat diakses oleh seorang user dalam sebuah aplikasi. Proses ini menjawab pertanyaan "Kamu diizinkan untuk melakukan apa?"
    - Dalam Django proses otorisasi dapat diimplementasikan menggunakan sistem otorisasi dan perizinan yang telah disediakan oleh django. Sistem perizinan Django memungkinkan developer untuk menentukan siapa yang dapat melakukan aktivitas dan meangkses data dari aplikasi dan siapa yang tidak. 

autentikasi dan otorisasi adalah komponen fundamental dari pengembangan web di Django. Keduanya membantu membangun kepercayaan, melindungi data, dan memberikan pengalaman yang dipersonalisasi dan aman bagi user. Ketika diimplementasikan dengan benar, keduanya berkontribusi pada kesuksesan dan fungsionalitas aplikasi web yang akan kita kembangkan.

**Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

Cookies adalah data kecil yang disimpan oleh browser web pada perangkat user. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi di sisi klien, seperti preferensi user, ID sesi, token otentikasi, dan banyak lagi. Cookies berguna untuk melacak informasi antar permintaan HTTP dan memungkinkan aplikasi untuk mengenali user saat mereka kembali.

Bagaiamana django menggunakan cookies untuk mengelola data sesi user:
    1. Ketika user masuk ke aplikasi web Django, kredensial user (misalnya, username dan password) diverifikasi oleh sistem autentikasi aplikasi.
    2. Setelah autentikasi berhasil, Django membuat sesi untuk usesr. Sesi pada dasarnya adalah sekumpulan data yang disimpan di server dan diasosiasikan dengan user.
    3. ID sesi yang unik dibuat untuk sesi user. ID sesi ini adalah identifier acak dan unik.
    4. Data sesi disimpan di server, dan cookie ID sesi dikirim ke browser user. Cookie ini biasanya diberi nama seperti sessionid dan berisi ID sesi yang unik.
    5. Pada permintaan HTTP berikutnya, browser user secara otomatis mengirimkan cookie ID sesi ke server. Hal ini memungkinkan server mengenali user dan mengaitkan request dengan sesi mereka.
    6. Data sesi digunakan untuk menentukan apakah user memiliki izin untuk mengakses sumber daya atau tampilan tertentu. Sistem izin Django, yang sering kali terkait dengan data sesi, dapat mengontrol akses ke berbagai bagian aplikasi.
    7.Ketika user keluar, sesi biasanya dihancurkan, dan cookie ID sesi dihapus dari device user.
    8. Sesi memiliki periode waktu habis (dikontrol oleh pengaturan SESSION_COOKIE_AGE di Django). Setelah periode tidak aktif ini, sesi 
    akan kedaluwarsa, dan user harus login kembali.

**Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

    Penggunaan cookies dalam pengembangan web dapat menjadi alat yang kuat untuk mengelola sesi pengguna, otentikasi, dan menyimpan preferensi pengguna. Namun, ada sejumlah risiko potensial yang perlu diwaspadai:

    1. Keamanan Data: Cookies dapat menyimpan informasi pribadi, seperti token otentikasi, yang dapat menjadi sasaran peretasan jika tidak disimpan dengan benar.

    2. Privasi Pengguna: Cookies dapat digunakan untuk melacak perilaku pengguna di seluruh situs web. Hal ini menimbulkan masalah privasi, terutama jika pengguna merasa terlalu banyak data mereka disimpan dan digunakan tanpa izin.

    3. CSRF (Cross-Site Request Forgery): Cookies yang disimpan dalam browser dapat digunakan untuk mengotorisasi permintaan HTTP ke aplikasi. Ini dapat dimanfaatkan oleh serangan CSRF jika tindakan mitigasi tidak diambil.

    4. XSS (Cross-Site Scripting): Serangan XSS dapat mencuri data sesi dari cookie pengguna. Ini terjadi jika aplikasi tidak mengamankan data yang masuk ke dalam cookie.

    5. Peretasan: Penjahat siber dapat mencoba mencuri cookie pengguna dengan berbagai cara, termasuk serangan perangkat lunak berbahaya dan peretasan jaringan.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    Registrasi:
        1. Mengimport 'redirect', 'UserCreationForm', dan 'messages' pada views.py. Fungsi 'redirect' digunakan untuk mengembalikan tampilan dari bagian register akun. 'UserCreation' merupakan formulir bawaan yang disediakan oleh django sehingga saya tidak perlu membuat kode untuk form dari awal. 'messages' digunakan untuk menampilkan pesan bila user berhasil membuat akun.
        2. Membuat fungsi baru bernama 'register' yang menerima parameter 'request'. Fungsi ini berisi 'form = UserCreationForm(request.POST)' yang berfungsi untuk menampilkan form yang telah diimport dan memasukkan data ke server atau database sesuai dengan data yang diinput oleh user. Kemudian apabila data pada form yang diinput user valid, maka form tersebut akan disimpan dan mengeluarkan pesan menggunakan 'message.success'. Setelah user berhasil membuat akun baru, maka tampilan web akan kembali ke halaman login.
        3. Membuat berkas HTML bernama 'register.html' pada 'main/templates' untuk membuat template halaman register akun.
        4. Mengimport fungsi 'register' pada 'main/urls.py.' kemudian mendaftarkan fungsi tersebut pada 'urlpatterns' agar ketika tombol register ditekan oleh user, maka halaman web akan berpindah ke halaman register dan menjalankan fungsi register.

    Login:
        1. Mengimport 'authenticate' dan 'login' pada 'views.py' untuk melakukan autentikasi user dan login apabila autentikasi berhasil.
        2. Membuat fungsi 'login_user' pada views.py dan melakukan autentikasi username dan password yang diinput oleh user dengan membuat variable 'user = authenticate (request, username=username, password=password)'. Fungsi authenticate akan mengautentikasi user berdasarkan username dan password yang dimasukkan. 
        3. Membuat berkas HTML bernama 'login.html' pada 'main/templates' untuk membuat template halaman login akun.
        4. Mengimport fungsi 'login_user' yang telah dibuat ke dalam 'main/urls.py'. Kemudian mendaftarkan fungsi pada 'urlpatterns'

    Logout:
        1. Mengimport 'logout' 'pada views.py' berfungsi untuk melogout user yang telah login pada session.
        2. Membuat fungsi 'logout_user' views.py dan melogout pengguna pada session menggunakan perintah 'logout(request)' dan mengembalikan halaman website ke halaman login menggunakan 'return redirect('main:login')'
        3. Menambahkan button 'Logout' pada 'main/templates/main.html/'
        4. Mengimport fungsi 'logout_user' yang telah dibuat ke dalam 'main/urls.py'. Kemudian mendaftarkan fungsi tersebut pada 'urlpatterns'

    Mengharuskan user untuk login:
        Untuk mewajibkan user login terlebih dahulu, maka saya merestriksi halaman main dengan cara berikut:
        1. Mengimport 'login_required' pada 'main/views.py' 
        2. Menambahkan perintah '@login_required(login_url='/login')' tepat diatas fungsi 'show_main' untuk merestriksi user mengakses halaman main ketika belum login.

2. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    1. Mengimport 'datetime' , 'HttpResponseRedirect', 'reverse' pada 'main/views.py'
    2. Menambahkan perintah 'response = HttpResponseRedirect(reverse("main:show_main")) ' dan 'response.set_cookie('last_login', str(datetime.datetime.now()))' di bawah 'login(request, user)' yang berada pada fungsi 'login_user'. Perintah 'response.set_cookie('last_login', str(datetime.datetime.now()))' digunakan untuk membuat cookie last login dan menambahkannya ke dalam variable 'response' yang telah dibuat.
    3. Menambahkan kode " 'last_login': request.COOKIES['last_login']," pada 'context' untuk menambahkan informasi cookie last_login.
    4. Menambahkan perintah 'response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')' di bawah 'logout(request)' yang berada pada fungsi 'logout_user' untuk menghapus cookie last_login ketika user logout.
    5. Menambahkan informasi cookies last login pada main.html

3.  Menghubungkan model Item dengan User.

    1. Mengimport 'user' pada 'main/models.py'
    2. Menambahkan variable user pada class 'Item' dengan value 'models.ForeignKey(User, on_delete=models.CASCADE)' pada 'main/models.py'. Hal tersebut dilakukan untuk menghubungkan satu item dengan satu user menggunakan relationship sehingga setiap item pasti akan berkaitan dengan seorang user.
    3. Menambahkan 'item = form.save(commit=False)', 'item.user = request.user', dan 'item.save()' pada fungsi 'create_item' yang berada pada 'main/views.py'. Saya menggunakan parameter 'commit=False' untuk mencegah Django agar tidak langsung menyimpan object form yang telah saya buat ke database sehingga saya dapat mengaitkannya dengan user terlebih dahulu menggunakan 'item.user = request.user'. Perintah itu menandakan bahwa item yang baru saja dibuat dimiliki oleh user yang sedang login pada session ini. Kemudian saya baru menyimpan item pada database menggunakan 'item.save()'
    4. Mengganti '.all()' pada variable items menjadi 'filter(user=request.user)'. Hal ini saya lakukan agar item yang tampil di halaman utama hanyalah item yang terasosiasikan oleh pengguna (dimiliki pengguna). Mengganti value dari key 'name' pada context dengan 'request.user.username' untuk menampilkan username dari user yang login pada session ini.
    5. Membuat migration baru dan menetapkan default value untuk field user. Kemudian melakukan migrasi.

4. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    
    1. Menjalankan server menggunakan perintah 'python manage.py runserver'
    2. Membuat 2 akun berbeda dengan menekan tombol register.
    3. Login pada salah satu akun kemudian membuat item sebanyak 3.
    4. Login pada akun lainnya dan membuat item sebanyak 3 (yang berbeda dengan item pada akun pertama).
    5. Dapat dilihat bahwa tampilan pada halaman tiap akun akan berbeda. Nama yang ditampilkan merupakan username dari tiap akun dan item yang ditampilkan hanyalah item yang dibuat pada tiap akun (tidak tercampur semuanya).
