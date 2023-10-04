**Nama    : Zaim Aydin Nazif**

**NPM     : 2206082524**

**Kelas   : F**

TUGAS 05:

**Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.**
1. Selector Universal `(*)` : Digunakan untuk memilih semua elemen pada halaman web. Digunakan untuk memberikan style dasar. Kita perlu hati-hati untuk menggunakan selector ini karena dapat mempengaruhi seluruh elemen yang ada pada halaman web.

2. Selector Tag `(<p>, <h1>, <div>, dll.)`: digunakan untuk memilih semua elemen dengan tag HTML tertentu. Digunakan untuk mengatur style dasar elemen-elemen HTML seperti paragraf, judul, atau div.

3. Selector Class `(.classname)` : Selector ini digunakan untuk memilih elemen-elemen yang memiliki class tertentu. Selector ini digunakan ketika menggabungkan elemen-elemen yang ingin diatur dengan gaya yang sama atau papa penerapan gaya pada suatu kelas.

4. Selector Id `(#idname)` : digunakan untuk memilih elemen dengan ID tertentu. Selector ini biasa digunakan untuk mengatur gaya atau perilaku khusus untuk elemen dengan ID tertentu.

5. Selector Pseudo-class `(:pseudo-class)` : digunakan untuk memilih elemen berdasarkan keadaan atau interaksi pengguna. Digunakan untuk memberikan efek interaktif pada elemen.

6. Selector Pseudo-element `(::pseudo-element)` : Selector ini digunakan untuk memilih bagian khusus dari elemen, seperti bagian sebelum (:before) atau sesudah (:after) elemen, atau bahkan baris pertama (:first-line) dalam elemen teks. Selector ini dapat digunakan untuk mengatur gaya khusus untuk bagian-bagian elemen tertentu.

7. Selector kombinasi: selector ini memungkinkan untuk memilih elemen berdasarkan hubungan atau konteks mereka dalam dokumen, contohnya elemen yang berada dalam elemen lain (element1 element2).

8. Selector Atribut `([attribute], [attribute=value], [attribute~=value])` :
Selector ini memilih elemen berdasarkan atribut HTML mereka. Selector ini digunakan ketika ingin menargetkan elemen yang memiliki atribut tertentu atau nilai atribut tertentu.

**Jelaskan HTML5 Tag yang kamu ketahui.**
1. `<header>`: Digunakan untuk mendefinisikan bagian atas halaman atau elemen pembuka dalam sebuah artikel atau bagian konten.

2. `<nav>`: Menunjukkan bagian dari tautan navigasi seperti menu atau daftar tautan ke halaman lain.

3. `<section>`: Mengelompokkan konten yang terkait secara tematik dalam sebuah dokumen. section membantu mengorganisasi dan menjelaskan konten dalam dokumen.

4. `<article>`: Mengidentifikasi sebuah konten yang bisa berdiri sendiri dan bisa digunakan secara independen dari halaman lainnya, seperti posting blog atau artikel berita.

5. `<aside>`: Mengandung konten yang berhubungan, tetapi bukan bagian utama dari halaman. aside sering digunakan untuk sidebar atau konten terkait lainnya.

6. `<footer>`: Digunakan untuk mendefinisikan bagian bawah halaman atau elemen penutup dalam sebuah artikel atau bagian konten.

7. `<figure>` dan `<figcaption>`: `<figure>` digunakan untuk mengelompokkan elemen yang berhubungan, seperti gambar, grafik, atau ilustrasi, bersama dengan `<figcaption>` yang digunakan untuk memberikan deskripsi atau keterangan.

8. `<main>`: Menandakan elemen utama konten dalam sebuah dokumen. Hanya boleh ada satu elemen `<main>` dalam satu halaman.

9. `<mark>`: Mewarnai teks di dalamnya untuk menyorot atau menandai teks yang relevan.

10. `<time>`: Digunakan untuk menandai tanggal atau waktu dalam berbagai format, seperti tanggal, waktu, atau zona waktu.

**Jelaskan perbedaan antara margin dan padding.**
- margin:
    Margin adalah area kosong yang ada di sekeliling batas sebuah elemen. Margin berfungsi untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya. Dengan menggunakan margin, Anda dapat mengendalikan jarak antara elemen-elemen, menciptakan pemisahan visual antara elemen-elemen, atau mengelola tata letak secara keseluruhan.

- padding:
    adalah ruang di dalam batas elemen. Padding akan mempengaruhi jarak antara isi elemen dan batas elemen itu sendiri. Padding digunakan untuk mengatur jarak antara suatu konten elemen dan batas elemen tersebut.

**Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**
1. Desain:
    - Bootstrap: Bootstrap adalah framework CSS yang bersifat lebih preskriptif. Ini berarti Bootstrap memiliki style bawaan yang lebih banyak dan komponen yang telah dirancang dengan baik, dan kita cukup menggunakannya sesuai dengan panduan yang diberikan.

    -Tailwind CSS: Tailwind CSS adalah framework yang lebih terfokus pada utilitas. Ini berarti kita perlu membuat komponen kita sendiri dengan menggabungkan kelas-kelas utilitas yang disediakan oleh Tailwind. Hal ini menyebabkan desain dari tailwind lebih fleksibel.

2. Kustomisasi:
    - Bootstrap: : Bootstrap memiliki opsi kustomisasi, tetapi untuk melakukan penyesuaian yang signifikan, kita perlu merombak CSSnya.

    - Tailwind CSS: kita dapat mengatur setiap aspek desain dengan mengedit file kongigurasi atau kita dapat membuat kelas kustom tersendiri.

3. Kecepatan pengembangan:
    - Bootstrap : Lebih cepat karena banyak komponen-komponen yang sudah disediakan.

    - Tailwind CSS : Memerlukan waktu yang lebih lama karena kita harus membuat komponen dari awal.

Kapan kita menggunakan Bootstrap:
1. Ketika kita perlu membangun prototipe atau mengembangkan dengan cepat karena Bootstrap menyediakan banyak komponen siap pakai.

2. Tidak ingin menggunakan banyak kustomisasi visual dan lebih memilih kustomisasi yang sudah disediakan oleh Bootstrap


Kapan kita menggunakan Tailwind:
1. Ketika ingin website kita fleksibel dalam hal desain dan tampilan yang sangat mendetail.

2. Ingin membangun komponen dari awal

3. Ingin mengurangi ukuran file CSS yang dihasilkan dan hanya menggunakan apa yang dibutuhkan


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

- menambahkan script Bootstrap CSS dan JavaScript pada `base.html` 

```html
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>

```

- Menambahkan navbar pada `edit_item.html`, `main.html`, `create_item.html` menggunakan navbar yang ada pada bootsrap.
```html
<nav class="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">My Inventory</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
     
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class= "navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link disabled" aria-disabled="true">{{name}}</a>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">{{class}}</a>
            </li>
          </ul>

        <ul class="nav justify-content-end">
            <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
            </form>
        </ul>
      </div>
    </div>
  </nav> 
```
- membuat tabel untuk item pada `main.html` dengan style "table-striped" dan "table-hover". Kemudian membuat garis pemisah antara nama field dan itemnya menggunakan "table-groupdivider"

```html
<table class="table table-striped table-hover">
    <tr>
        <th>Name</th>
        <th>Ammounts</th>
        <th>Description</th>
        <th>Date Added</th>
        <th>Effect</th>
        <th>Category</th>
        <th>Action</th>
    </tr>

    <tbody class="table-group-divider">
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.ammount}}</td>
                <td>{{item.description}}</td>
                <td>{{item.date_added}}</td>
                <td>{{item.effect}}</td>
                <td>{{item.category}}</td>
                <td>
                    <a href="{% url 'main:edit_item' item.pk %}">
                        <button button type="button" class="btn btn-warning">
                            Edit
                        </button>
                    </a>
                    <a href="{% url 'main:delete_item' item.pk %}">
                        <button type="button" class="btn btn-danger">
                            Delete
                        </button>
                    </a>
                </td>
            </tr>
        {% endfor %}
    </tbody>
```
- Mengubah warna button-button yang ada pada `main.html` menggunakan variasi class button yang ada pada Bootstrap. Contohnya:

```html
<button button type="button" class="btn btn-warning">
    Edit
</button>

<button type="button" class="btn btn-danger">
    Delete
</button>
```
- Membuat container mt-4 untuk `login.html`, `edit_item.html`, `register.html`, dan `create_item.html` kemudian membuat class yang akan menampung komponen2 yang ada. Kemudian membuat text dan table komponen berada di tengah menggunakan "text-center" untuk text dan "mx-auto" tabel

```html
<div class="container mt-4">
    <div class="editItem text-center">
        <h1>Edit Item</h1>
        <form method="POST">
            {% csrf_token %}
            <table class="mx-auto">
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Edit Item"/>
                    </td>
                </tr>
            </table>
        </form>
    </div>
</div>
```