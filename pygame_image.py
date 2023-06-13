import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kt_img = pg.image.load("ex01/fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    kt_imgs = []
    
    for i in range(1, 11):
        kt_imgs.append(pg.transform.rotozoom(kt_img, i, 1.0))
        
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if (tmr%20)//10 == 0:
            ktmr = tmr%10
        else:
            ktmr = -tmr%10-1

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        screen.blit(kt_imgs[ktmr], [300, 200])
        pg.display.update()
        tmr += 1  
        if tmr%3200 == 0:
            tmr = 0      
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()