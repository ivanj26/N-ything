# N-ything

N-ything problem merupakan modifikasi N-queen problem. Perbedaannya, buah catur yang
menjadi pertimbangan bukan hanya ratu (queen), namun juga meliputi kuda (knight), gajah
(bishop), dan benteng (rook). Seperti N-queen problem, permasalahan dari N-ything problem
adalah mencari susunan buah-buah catur pada papan catur berukuran 8x8 dengan jumlah buah
catur yang menyerang buah catur lain minimum.

Secara lebih formal, cari susunan buah-buah catur sehingga jumlah pasangan terurut (p, q) di
mana p menyerang q minimum. Perhatikan bahwa bila p menyerang q, belum tentu q juga
menyerang p. Perhatikan juga bahwa (p, q) dan (q, p) dianggap sebagai dua pasangan yang
berbeda.

Adapun sifat penyerangan ini mengikuti sifat penyerangan pada permainan catur pada
umumnya. Misalnya, sebuah benteng dapat menyerang buah catur lain yang berada pada jalur
vertikal/horizontal apabila buah catur tersebut tidak terhalang oleh buah catur lainnya, dan
seterusnya.

Untuk menyelesaikan N-ything problem ini, Anda diminta menggunakan ketiga algoritma local
search berikut:
1. Hill climbing
2. Simulated annealing
3. Genetic algorithm

## Aturan Tambahan
1. Bahasa yang boleh dipergunakan adalah Python.
2. 1 kelompok terdiri dari 4-5 orang anggota.
3. Anggota kelompok boleh lintas kelas namun anggota kelompok tidak boleh sama
dengan tugas kecil yang lalu.
4. Isi nama kelompok dan setiap anggotanya di sheet berikut:
https://docs.google.com/spreadsheets/d/1lLYFk60fmx7xAWBvn35HO7oTpkqjEdwnevXU
xvt_1Pc/
5. Pengisian nama kelompok sampai Senin, 17 September 2018​.
