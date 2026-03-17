from pygame import *

window = display.set_mode((700, 500))
background = transform.scale(image.load('background.png'), (700, 500)) #mengambil gambar background dan mengatur ukurannya
#mengambil dan merubah ukuran dari karakter 1 dan 2
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

run = True #kita gunakan untuk pengecekan looping game
FPS = time.Clock() #membuat kode untuk mengatur FPS

#menyimpan data position dari sprite
x1 = 0
y1 = 250

x2 = 600
y2 = 250

# Membuat daftar rintangan (walls)
walls = [
    Rect(300, 150, 50, 200), # Tembok tengah
    Rect(100, 100, 100, 20), # Tembok atas
    Rect(500, 380, 100, 20)  # Tembok bawah
]

while run: #membuat looping game
    window.blit(background, (0,0)) #memunculkan background
    
    # Memunculkan rintangan ke layar
    for wall in walls:
        draw.rect(window, (100, 100, 100), wall)

    window.blit(sprite1, (x1, y1)) #memunculkan sprite pertama
    window.blit(sprite2, (x2, y2)) #memunculkan sprite kedua

    for e in event.get(): #mengambil seluruh event untuk bisa berinteraksi dengan program
        if e.type == QUIT: #jika eventnya adalah keluar dari aplikasi
            run = False #looping game akan diselesaikan

    keys = key.get_pressed() #menyimpan konsep klik keyboard ke variabel

    #pergerakkan sprite 1
    new_x1, new_y1 = x1, y1
    if keys[K_a] and x1 > 0: new_x1 -= 5
    if keys[K_d] and x1 < 600: new_x1 += 5
    if keys[K_s] and y1 < 400: new_y1 += 5
    if keys[K_w] and y1 > 0: new_y1 -= 5
    
    # Cek tabrakan tembok untuk sprite 1
    rect1 = Rect(new_x1, new_y1, 100, 100)
    collide1 = False
    for wall in walls:
        if rect1.colliderect(wall):
            collide1 = True
    if not collide1:
        x1, y1 = new_x1, new_y1

    #pergerakkan sprite 2
    new_x2, new_y2 = x2, y2
    if keys[K_LEFT] and x2 > 0: new_x2 -= 5
    if keys[K_RIGHT] and x2 < 600: new_x2 += 5
    if keys[K_DOWN] and y2 < 400: new_y2 += 5
    if keys[K_UP] and y2 > 0: new_y2 -= 5

    # Cek tabrakan tembok untuk sprite 2
    rect2 = Rect(new_x2, new_y2, 100, 100)
    collide2 = False
    for wall in walls:
        if rect2.colliderect(wall):
            collide2 = True
    if not collide2:
        x2, y2 = new_x2, new_y2

    display.update() #mengupdate konten" yang ada di aplikasi
    FPS.tick(60) #mengatur FPS