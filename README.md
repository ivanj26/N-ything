# N-ything

`English version`

The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the more general n queens problem of placing n non-attacking queens on an n×n chessboard, for which solutions exist for all natural numbers n with the exception of n = 2 and n = 3

`Indonesia version`

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

## Requirements
- Python2

## How to run app?
1. Run the program with the following command.
   ```shell
    python main.py
   ```
2. Input the filename, you can choose one of test file from this repository.
2. Choose the algorithm strategy to find the solution.
3. Choose max attempt.
4. The Board will printing immediately after found the solution.

# Screenshots
![App .gif #1](./screenshots/1080p%20Screen%20Recording%202021-09-10%20at%2019.30.15.gif)
**Figure 1** - App preview


![App Screenshot #2](./screenshots/Screen%20Shot%202021-09-10%20at%2019.38.58.png)
**Figure 2** - App screenshot
