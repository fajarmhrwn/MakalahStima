import pygame
import sys
import numpy as np
import os
import time
import copy
from pygame.locals import *
from disk import *

# Inisialisasi Pygame
pygame.init()

# Konstanta
FPS = 30
WINDOW_W = 1280
WINDOW_H = 720
BG_C = (50, 50, 90)

# Icon game
iconPath = os.path.join("img", "icon.png")
icon = pygame.image.load(iconPath)
pygame.display.set_icon(icon)
pygame.display.set_caption("Tower of Hanoi Game")

# Dimensi pool
pool_L = 300
pool_W = int((WINDOW_W - 40) / 6)

# Dimensi disk
disk_d = 20
disk_b = 5

# Kecepatan BFS
preBFS_speed = 10

# Inisialisasi Pygame
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOW_W, WINDOW_H))

# Jumlah disk
N = 5

def gameInit():
    # Variabel global
    global pools, preBFS_N, start, finish, status, auto, optN

    # Daftar pool
    pools = []
    pools.append([])
    pools.append([])
    pools.append([])

    # Menambahkan disk ke pool pertama
    for i in range(N, 0, -1):
        pools[0].append(disk(i, (170 + round(85 * (1 - i / N)), 220, 170 + round(85 * i / N)), DISPLAYSURF, disk_d, disk_b))

    # Variabel pool awal dan akhir
    start = -1
    finish = -1

    # Jumlah langkah BFS
    preBFS_N = 0

    # Status permainan
    status = 0

    # Mode otomatis
    auto = False

    # Jumlah langkah optimal
    optN = 1
    for i in range(N - 1):
        optN = 2 * optN + 1
    
# Fungsi untuk menambahkan kontrol ke dalam pool
def addControl(pool_ind):
    global start, finish, selected_disk, disk_x, disk_y, new_disk_x, new_disk_y, status
    
    if start == -1 and status == 0:
        # Menambahkan kontrol jika pool tidak kosong
        if len(pools[pool_ind]) > 0:
            start = pool_ind
            disk_x = (2*pool_ind + 1) * pool_W + 21
            disk_y = WINDOW_H - 40 - len(pools[pool_ind])*(disk_b + disk_d)
            selected_disk = pools[pool_ind][-1]
            pools[start] = pools[pool_ind][:-1]
            status = 1
            
    elif start >= 0 and (status == 1 or status == 2) :
        # Memindahkan kontrol ke pool lain
        if len(pools[pool_ind]) == 0:
            finish = pool_ind
            new_disk_x = (2*pool_ind + 1) * pool_W + 21
            new_disk_y = WINDOW_H - 40 - (len(pools[pool_ind]) + 1)*(disk_b + disk_d)
            if status == 2:
                status = 3  
        else:
            if pools[pool_ind][-1].disk_ind > selected_disk.disk_ind:
                finish = pool_ind
                new_disk_x = (2*pool_ind + 1) * pool_W + 21
                new_disk_y = WINDOW_H - 40 - (len(pools[pool_ind]) + 1)*(disk_b + disk_d)
                if status == 2:
                    status = 3

# Inisialisasi permainan
gameInit()
    
# Menghasilkan daftar pool
def listPoll():
    pool_list = []
    for pool in pools:
        temp = []
        for disk in pool:
            temp.append(disk.disk_ind)
        pool_list.append(temp)
        
    return pool_list

# Mengeksekusi pemindahan kontrol sebelum menjalankan algoritma BFS
def preBFS(p_s, p_f, pools):
    new_pools = copy.deepcopy(pools)
    valid = False
    if len(new_pools[p_s]) > 0:
        if len(new_pools[p_f]) == 0:
            new_pools[p_f].append(new_pools[p_s][-1])
            new_pools[p_s] = new_pools[p_s][:-1]
            valid = True
        else:
            if new_pools[p_s][-1] < new_pools[p_f][-1]:
                new_pools[p_f].append(new_pools[p_s][-1])
                new_pools[p_s] = new_pools[p_s][:-1]
                valid = True
    return new_pools, valid

# Algoritma BFS untuk mencari solusi optimal
def BFS(pool_stat):
    searching = [(pool_stat, [])]
    searched = [pool_stat]
    
    searchedN = 0
    
    while True:
        searchedN += 1
        if searchedN % 1000 == 0:
            print('%s : Searching...'%(searchedN))
        pool_stat, hist = searching[0]
        if len(pool_stat[2]) == N or len(pool_stat[1]) == N:
            break
        searching = searching[1:]
        for p_s in range(3):
            for p_f in range(3):
                if p_s != p_f:
                    new_pools, valid = preBFS(p_s, p_f, pool_stat)
                    if valid:
                        if new_pools not in searched:
                            searching.append((new_pools, hist+[(p_s, p_f)]))
                            searched.append(new_pools)
    return hist
    
# Loop dalam permainan
while True:
    DISPLAYSURF.fill(BG_C)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            if y > WINDOW_H - pool_L - 40 and y < WINDOW_H - 30:
                for p_i in range(3):
                    if abs(x - ((2*p_i + 1) * pool_W + 20)) < 50:
                        addControl(p_i)
            
        if event.type == pygame.MOUSEBUTTONUP:
            pass
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                addControl(0)
            if event.key == pygame.K_2:
                addControl(1)
            if event.key == pygame.K_3:
                addControl(2)
                
            if event.key == pygame.K_4:
                num = np.random.randint(0, N)
                if status == 0:
                    if len(pools[0]) > num:
                        addControl(0)
                    elif len(pools[1]) + len(pools[0]) > num:
                        addControl(1)
                    elif len(pools[2]) + len(pools[1]) + len(pools[2]) > num:
                        addControl(2)
                else:
                    num = np.random.randint(0, 3)
                    addControl(num)
            
            # Menakan `r` pada keyboard untuk reset permainan
            if event.key == pygame.K_r:
                gameInit()
            
            # Menakan `s` pada keyboard untuk memulai solusi otomatis permainan
            if event.key == pygame.K_s:
                if not auto and status == 0:
                    move = BFS(listPoll())
                    auto = True
                else:
                    auto = False
            
            # Menakan `up arrow` pada keyboard untuk meningkatkan game speed
            if event.key == pygame.K_UP:
                preBFS_speed += 5
            
            # Menakan `down arrow` pada keyboard untuk menurunkan game speed
            if event.key == pygame.K_DOWN:
                preBFS_speed = max(5, preBFS_speed - 5)
            
            # Menakan `right arrow` pada keyboard untuk menambah piringan pada game
            if event.key == pygame.K_RIGHT:
                N = min(10, N + 1)
                gameInit()
            
            # Menakan `left arrow` pada keyboard untuk mengurangi piringan pada game
            if event.key == pygame.K_LEFT:
                N = max(3, N - 1)
                gameInit()
                
    for p_i in range(3): 
        pygame.draw.line(DISPLAYSURF, (200, 200, 200), ((2*p_i + 1) * pool_W + 20, WINDOW_H - pool_L - 40), ((2*p_i + 1) * pool_W + 20, WINDOW_H - 30), 6)
    
    pygame.draw.line(DISPLAYSURF, (240, 240, 240), (20, WINDOW_H - 30), (WINDOW_W - 20, WINDOW_H - 30), 10)
    
    for p_i, pool in enumerate(pools):
        for d_i, d_l in enumerate(pool, 1):
            d_l.draw((2*p_i + 1) * pool_W + 21, WINDOW_H - 40 - d_i*(disk_b + disk_d))
            
    if auto:
        AUTOFONT = pygame.font.Font('freesansbold.ttf', 20)
        autoSurf = AUTOFONT.render('Mode Otomatis', 1, (240, 240, 255)) 
        autoRect = autoSurf.get_rect()
        autoRect.topleft = (30, 20)
        
        DISPLAYSURF.blit(autoSurf, autoRect)
        
        if status == 0 and len(move) > 0:
            p_s, p_f = move[0]
            move = move[1:]
            addControl(p_s)
            addControl(p_f)
        
        
    if status == 1:
        if disk_y > 100:
            disk_y -= preBFS_speed
        else:
            status = 2
        selected_disk.draw(disk_x, disk_y)
        
    if status == 2:
        selected_disk.draw(disk_x, disk_y)
        if finish >= 0:
            status = 3
        
    if status == 3:
        if abs(disk_x - new_disk_x) > preBFS_speed:
            if disk_x - new_disk_x > 0:
                disk_x -= preBFS_speed
            elif disk_x - new_disk_x < 0:
                disk_x += preBFS_speed
        else:
            disk_x = new_disk_x
            status = 4
            preBFS_N += 1
        selected_disk.draw(disk_x, disk_y)
        
    if status == 4:
        if disk_y < new_disk_y:
            disk_y += preBFS_speed
        else:
            status = 0
            pools[finish].append(selected_disk)
            start = -1
            finish = -1
        selected_disk.draw(disk_x, disk_y)  
        
    if len(pools[1]) == N or len(pools[2]) == N:
        VICFONT = pygame.font.Font('freesansbold.ttf', 100)
        vicSurf = VICFONT.render('STAGE CLEAR', 1, (round(255 * (1 - optN / preBFS_N)), round(255 * (optN / preBFS_N)), 10))
        vicRect = vicSurf.get_rect()
        vicRect.center = (WINDOW_W/2, WINDOW_H/2)
    
        RESFONT = pygame.font.Font('freesansbold.ttf', 30)
        resSurf = RESFONT.render('BFS Movement / Optimal = %s / %s'%(preBFS_N, optN), 1, (255, 255, 255)) 
        resRect = resSurf.get_rect()
        resRect.center = (WINDOW_W/2, WINDOW_H/2 + 70)
        
        DISPLAYSURF.blit(vicSurf, vicRect)
        DISPLAYSURF.blit(resSurf, resRect)        
        
    STATUSFONT = pygame.font.Font('freesansbold.ttf', 30)
    statSurf = STATUSFONT.render('BFS Movement : %s'%(preBFS_N), 1, (255, 255, 255))  
    statRect = statSurf.get_rect()
    statRect.topright = (WINDOW_W - 30, 30)
    DISPLAYSURF.blit(statSurf, statRect)
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)