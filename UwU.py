import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

nomer_ekrana = 1
pers = 2
hp = 1
hpall = 1
w_lvl = 0
zuk = 0
mobes = 0
m_hp = []
iksiki = []
seki = []
ataki = []
seki_neo = 0

hp_ = pygame.image.load("data/hp.png")
dmj_ = pygame.image.load("data/dmj.png")
mob_ = [pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob_atak.png"), (150, 150))]


def stop():
    pygame.quit()
    exit()


def font(razmer_bookve):
    font = pygame.font.Font("data/briannetod.ttf", razmer_bookve)
    return font


def naris(png, xy):
    rect = png.get_rect(bottomright=xy)
    screen.blit(png, rect)


def nar_skin(png):
    global surf
    surf = pygame.image.load(png)
    surf = pygame.transform.scale(surf, (100, 100))
    if pers == 1:
        surf = pygame.transform.scale(surf, (150, 150))
    rect = pygame.mouse.get_pos()
    if rect[0] != 0 and rect[1] != 0:
        screen.blit(surf, rect)


class Person(pygame.sprite.Sprite):
    if pers == 1:
        image = pygame.image.load("data/lover.png")
    if pers == 2:
        image = pygame.image.load("data/normis.png")
    if pers == 3:
        image = pygame.image.load("data/ostrov.png")

    def __init__(self, pers):
        global hp, hpall
        self.pers = pers
        self.hp = hp
        self.hpall = hpall
        self.mask = pygame.mask.from_surface(self.image)

        self.zdor(self.hp, self.hpall)
        self.skin(self.pers)

    def skin(self, pers):
        if pers == 1:
            nar_skin("data/lover.png")
        if pers == 2:
            nar_skin("data/normis.png")
        if pers == 3:
            nar_skin("data/ostrov.png")

    def zdor(self, hp, hpall):
        if hp > hpall:
            hp = hpall
        if int(hp) > 0:
            naris(hp_, (950, 120))
            if int(hp) > 1:
                naris(hp_, (830, 120))
                if int(hp) > 2:
                    naris(hp_, (710, 120))
                    if int(hp) > 3:
                        naris(hp_, (590, 120))
                        if int(hp) > 4:
                            naris(hp_, (470, 120))


class Mob(pygame.sprite.Sprite):
    image = mob_

    def __init__(self, nom):
        global mobes, zzz, fps, dmg, zuk, m_hp, iksiki, ataki, seki
        if zuk > 0:
            m_hp.append(fps * 3)
            zuk -= 1
        self.nom = nom
        self.ataki = ataki[nom]
        self.seki = seki[nom]
        self.dmg = dmg
        self.image = Mob.image

        naris(self.image[self.ataki], iksiki[self.nom])
        colision = zzz  # Когда моб сопрекасаеться с Person    if pygame.sprite.collide_mask(self, self.person):
        if self.seki < 1:
            seki[nom] = 0
            ataki[nom] = random.randint(0, 4)
            if ataki[nom] != 3:
                seki[nom] = fps
            seki[nom] += fps
        seki[nom] -= 1

        if colision:
            self.auh()

    def auh(self):
        global m_hp, mobes
        m_hp[self.nom] -= self.dmg
        if m_hp[self.nom] < 1:
            mobes -= 1
        print(m_hp[self.nom])

    # def odnoraz(self):


def persik():
    global pers, nomer_ekrana, hp, hpall, mobes, w_lvl, dmg

    if pers == 3:
        picture = pygame.image.load("data/ostrov.png")
        rect = picture.get_rect(bottomright=(820, 350))
        screen.blit(picture, rect)

        picture = pygame.image.load("data/normis.png")
        picture = pygame.transform.scale(picture, (160, 160))
        rect = picture.get_rect(bottomright=(580, 330))
        screen.blit(picture, rect)

        picture = pygame.image.load("data/lover.png")
        picture = pygame.transform.scale(picture, (160, 160))
        rect = picture.get_rect(bottomright=(360, 330))
        screen.blit(picture, rect)

        naris(dmj_, (270, 120))
        naris(dmj_, (390, 120))
        hp = 2
        hpall = 2
        dmg = 3

    elif pers == 2:
        picture = pygame.image.load("data/ostrov.png")
        picture = pygame.transform.scale(picture, (160, 160))
        rect = picture.get_rect(bottomright=(800, 330))
        screen.blit(picture, rect)

        picture = pygame.image.load("data/normis.png")
        rect = picture.get_rect(bottomright=(600, 350))
        screen.blit(picture, rect)

        picture = pygame.image.load("data/lover.png")
        picture = pygame.transform.scale(picture, (160, 160))
        rect = picture.get_rect(bottomright=(360, 330))
        screen.blit(picture, rect)

        naris(dmj_, (270, 120))
        hp = 3
        hpall = 3
        dmg = 2

    elif pers == 1:
        picture = pygame.image.load("data/ostrov.png")
        picture = pygame.transform.scale(picture, (160, 160))
        rect = picture.get_rect(bottomright=(800, 330))
        screen.blit(picture, rect)

        picture = pygame.image.load("data/normis.png")
        picture = pygame.transform.scale(picture, (160, 160))
        rect = picture.get_rect(bottomright=(580, 330))
        screen.blit(picture, rect)

        picture = pygame.image.load("data/lover.png")
        rect = picture.get_rect(bottomright=(380, 350))
        screen.blit(picture, rect)
        hp = 3
        hpall = 4
        dmg = 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and pers != 1:
            pers -= 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and pers != 3:
            pers += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if int(event.pos[0]) > 300 and int(event.pos[1]) > 400 \
                    and int(event.pos[0]) < 700 and int(event.pos[1]) < 570:
                nomer_ekrana = 2
                mobes = 0
                w_lvl = 0
            if int(event.pos[0]) > 200 and int(event.pos[1]) > 170 \
                    and int(event.pos[0]) < 360 and int(event.pos[1]) < 330:
                pers = 1
            if int(event.pos[0]) > 420 and int(event.pos[1]) > 170 \
                    and int(event.pos[0]) < 580 and int(event.pos[1]) < 330:
                pers = 2
            if int(event.pos[0]) > 640 and int(event.pos[1]) > 170 \
                    and int(event.pos[0]) < 800 and int(event.pos[1]) < 330:
                pers = 3
        if event.type == pygame.QUIT:
            stop()


def wolna():
    global iksiki, w_lvl, mobes, person, zuk, m_hp, seki, ataki, seki_neo, fps
    m_hp = []
    iksiki = []
    seki = []
    ataki = []
    seki_neo = round(fps * 2.5)
    for i in range(w_lvl + math.ceil(w_lvl / 2) + random.randint(0, math.ceil(w_lvl / 2))):
        iksiki.append((random.randint(250, 850), random.randint(250, 550)))
        mobes += 1
        zuk += 1
        seki.append(round(fps))
        ataki.append(1)


def ekran(nomer_ekrana):
    global iksiki, mobes, w_lvl
    if nomer_ekrana == 1:
        screen.fill((88, 255, 228))
        pygame.draw.rect(screen, (232, 140, 49), (300, 400, 400, 170), 0)
        pygame.draw.rect(screen, (255, 225, 68), (320, 420, 360, 130), 0)

        text = font(130).render("play", True, [255, 255, 255])
        screen.blit(text, (407, 390))

        naris(dmj_, (150, 120))

        persik()

    if nomer_ekrana == 2:
        screen.fill((88, 255, 228))
        if mobes == 0:
            w_lvl += 1
            wolna()
        for i in range(len(iksiki)):
            mob1 = Mob(i)
        c_col = (235, 90, 255)
        pygame.draw.circle(screen, (170, 0, 200), (50, 50), 150)
        pygame.draw.circle(screen, (235, 90, 255), (50, 50), 135)
        text = font(130).render(str(w_lvl), True, [0, 0, 0])
        if w_lvl == 1:
            uu = (60, 10)
        if 20 > w_lvl > 1:
            uu = (40, 10)
        if w_lvl > 19:
            uu = (15, 10)
        screen.blit(text, uu)

    person = Person(pers)


clock = pygame.time.Clock()
fps = 70
zzz = False
while True:
    ekran(nomer_ekrana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                nomer_ekrana = 1
            if event.key == pygame.K_F5:
                w_lvl += 1
                mobes = 0
            if event.key == pygame.K_z:
                zzz = True
            if event.key == pygame.K_x:
                zzz = False

    screen.blit(font(30).render(f"fps: {str(int(clock.get_fps()))}", True, [255, 255, 255]), (10, 555))
    clock.tick(fps)
    pygame.display.update()

stop()
