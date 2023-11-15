**Nama    : Zaim Aydin Nazif**

**NPM     : 2206082524**

**Kelas   : F**

TUGAS 06:

**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**

_Synchronus programming_ membuat proses pemrograman berjalan baris perbaris atau _sequential_. Hal ini membuat terjadinya penghentian sebuah program sebelum suatu proses diselesaikan terlebih dahulu. _Asynchronus programming_ di lain sisi, memungkinkan untuk proses-proses pemrograman berjalan secara bersamaan tanpa adanya interupsi dari proses lainnya.

**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

_Event-driven programming_ adalah sebuah konsep pemrograman dimana program dapat merespon setiap _events_ yang terjadi seperti interaksi pengguna, perubahan status, atau tindakan eksternal. Dalam konsep ini, program tidak berjalan secara linear baris per baris (atas ke bawah), akan tetapi menunggu adanya kejadian atau _events_ kemudian meresponnya.
Contohnya, pada tugas ini saya menggunakan _Event-driven programming_ pada bagian modal yang akan tampil ketika tombol `add item by AJAX` ditekan.


**Jelaskan penerapan asynchronous programming pada AJAX**

1. Menggunakan XMLHttpRequest atau Fetch API: Untuk melakukan permintaan ke server secara asinkron, kita dapat menggunakan objek XMLHttpRequest atau Fetch API. Biasanya, Fetch API lebih disukai karena lebih modern dan mudah digunakan.

2. Penanganan Callback: AJAX menggunakan callback functions untuk menangani respons dari server. kita mendefinisikan callback function yang akan dijalankan ketika respons dari server sudah siap. Ini memungkinkan kita untuk menjalankan kode lain selama menunggu respons dari server.

3. Promise dan async/await: kita juga dapat menggunakan Promise dan async/await untuk mengelola permintaan AJAX. Ini memungkinkan kita untuk menulis kode yang lebih bersih dan mudah dipahami.

4. Event Handling: kita juga dapat menggunakan event handling untuk menangani perubahan status permintaan AJAX, seperti ketika permintaan sedang dikirim, diterima, atau gagal.

**Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**

- Fetch API: 
    - Merupakan bagian dari JavaScript sehingga kita tidak perlu untuk mengunduh library tambahan. Termasuk spesifikasi standar ECMAScript yang men-_support_ hampir semua borwser

    - Dapat mengelola operasi asinkronusi yang lebih mudah dibaca daripada _callback_.

    - Lebih dringan daripada JQuery karena hanya berfokus pada AJAX

- JQuery:
    - Dirancang untuk menyelesaikan masalah kompatibilitas _device_ yang umum.

    - Dapat digunakan untuk pengembangan _front end_ yang lebih kompleksa karena JQuery menyediakan banyak utilitas untuk memanipulasi DOM

Penggunaan Fetch API lebih cocok untuk proyek yang ada pada pembelajaran PBP kali ini karena kita diharuskan untuk menggunakan AJAX yang sederhana dan dengan fokus untuk menjaga proyek agar tetap ringan dan bersih. Akan tetapi, apabila kita memerlukan untuk memanipulasi DOM secara mendalam, maka JQuery lebih baik untuk digunakan.


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**


Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX:

- AJAX GET:
1. Membuat fungsi `get_items_json` untuk mengembalikan data dalam bentuk JSON pada `views.py`. Perlu diingat bahwa item yang diambil sudah difilter berdasarkan items yang dimiliki user.

```python
def get_items_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))
```

2. Mendaftarkan fungsi `get_items_json` pada `urls.py`.

```python
...
path('get-item/', get_items_json, name='get_items_json'),
...
```

3. Menghapus tabel yang telah saya buat pada `main.html` sebelumnya, kemudian menggantinya dengan implementasi card.

4. Membuat blok script di bagian bawah file untuk implementasi Fetch API (mengambil data item dalam format JSON) kemudian menampilkannya dalam bentuk cards. 

- AJAX POST

1. Membuat fungsi `add_item_AJAX`pada `views.py` untuk menambahkan items secara asinkronus menggunakan AJAX. Kemudian menambahkan dekorator `@csrf_exempt` untuk kepentingan keamanan.

```python
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        ammount = request.POST.get("ammount")
        description = request.POST.get("description")
        effect = request.POST.get("effect")
        category = request.POST.get("category")
        user = request.user

        new_item = Item(name=name, ammount=ammount, description=description, effect=effect, category=category, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
    fields data diambil dari modal menggunakan `request.POST.get(<nama fields>)`. Kemudian membuat object item baru, lalu melakukan save item baru dengan menggunakan method `.save()`

2. Menambahkan fungsi yang telah dibuat pada `urls.py` dengan path `/create-ajax`.

```python
...
path('create-ajax/', add_item_ajax, name='add_ajax'),
...
```

3. Membuat implementasi modal untuk memasukkan data yang akan diinput oleh user pada `main.html`

4. Menambahkan button `Add Item by AJAX` kemudian menghubungkannya dengan modal yang telah dibuat.
```HTML
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX</button>
```

5. Menghubungkan button `Add item` pada modal ke fungsi `add_item_ajax` yang berada pada fungsi `views.py`.

```HTML
<button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
```

```JavaScript
function additem() {
        fetch("{% url 'main:add_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItems)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = additem
```
    method `onclick` memastikan bahwa ketika tombol dengan id "button_add" ditekan maka akan diarahkan pada funciton `additem()` diatasnya.

6. Membuat fungsi `refresh item` kemmudian memanggil fungsi tersebut untuk menampilkan daftar item terbaru menggunakan ajax.

```JavaScript
async function refreshItems() {
        const itemCards = document.getElementById("item_collection");
        itemCards.innerHTML = "";
        
        const items = await getItems()
        let htmlString =  items.forEach((item) => {
            const card = document.createElement("div")
            card.classList.add("col-md-4")
            card.innerHTML = `
            <div class="card text-bg-light border-info mb-3">
                <div class="card-body">
                    <h5 class="card-title">${item.fields.name}</h5>
                    <div class="card-text">
                        <p><b> Date Added : </b>${item.fields.date_added}</p>
                        <p><b> Ammount : </b>${item.fields.ammount}</p>
                        <p><b> Effect : </b>${item.fields.effect}</p>
                        <p><b> Category : </b>${item.fields.category}</p>
                        <b>Description:</b>
                        <p>${item.fields.description}</p>
                    </div>
                </div>
            
                <div class="card-footer d-flex align-items-center justify-content-center">
                    <a href="edit-item/${item.pk}">
                        <button class="btn btn-warning">
                            Edit
                        </button>
                        <a href="delete/${item.pk}">
                        <button class="btn btn-danger">
                            delete
                        </button>
                </div>
            </div>
            `;

            itemCards.appendChild(card);
           
        })
    }
```

- CollectStatic

1. menjalankan environment python

2. melakukan perintah `python manage.py collectstatic` sehingga file static yang ada akan dimasukkan pada direktori yang telah ditentukan pada `STATIC_ROOT`
