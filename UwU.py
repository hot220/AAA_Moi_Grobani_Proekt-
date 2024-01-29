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
w_lvl = -1
zuk = 0
mobes = 0
wiwi = 0
m_hp = []
iksiki = []
seki = []
seki_2 = []
ataki = []
bilo = []
stadia = []
mob1 = pygame.sprite.Group()
hero = pygame.sprite.Group()
seki_neo = 0
fon_nast = 1
fon = 0
fon_ded = 0

hp_ = pygame.image.load("data/hp.png")
dmj_ = pygame.image.load("data/dmj.png")
ded_ = pygame.image.load("data/ded.jpg")

mob_ded_ = pygame.mixer.Sound("data/fon/mob_ded.ogg")
person_ded_ = pygame.mixer.Sound("data/fon/person_ded.ogg")
mob_ = [pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob_neatak.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob.png"), (150, 150)),
        pygame.transform.scale(pygame.image.load("data/mob_atak.png"), (150, 150))]
fon_ = ["data/fon/fon1.mp3",
        "data/fon/fon2.mp3",
        "data/fon/fon3.mp3",
        "data/fon/fon4.mp3",
        "data/fon/fon5.mp3"]


def stop():
    pygame.quit()
    exit()


def font(razmer_bookve):
    font = pygame.font.Font("data/briannetod.ttf", razmer_bookve)
    return font


def naris(png, xy):
    rect = png.get_rect(bottomright=xy)
    screen.blit(png, rect)


class Person(pygame.sprite.Sprite):
    if pers == 1:
        image = pygame.image.load("data/lover.png")
    if pers == 2:
        image = pygame.image.load("data/normis.png")
    if pers == 3:
        image = pygame.image.load("data/ostrov.png")

    def __init__(self, pers, *group):
        global hp, hpall, seki_neo
        super().__init__(*group)

        self.pers = pers
        self.hp = hp
        self.hpall = hpall

        self.skin(self.pers)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.zdor(self.hp, self.hpall)

    def update(self, *pos):
        global seki_neo, nomer_ekrana, fon_ded

        self.hp = hp
        self.hpall = hpall
        self.pers = pers
        self.seki_neo = seki_neo

        self.zdor(self.hp, self.hpall)
        self.skin(self.pers)

        self.rect.x = pos[0][0]
        self.rect.y = pos[0][1]

        if self.seki_neo > 0:
            seki_neo -= 1

        if nomer_ekrana == 2 and self.hp == 0:
            pygame.mixer.music.stop()
            fon_ded = 1
            nomer_ekrana = 3

    def skin(self, pers):
        if pers == 1:
            self.image = pygame.transform.scale(pygame.image.load("data/lover.png"), (150, 150))
        if pers == 2:
            self.image = pygame.transform.scale(pygame.image.load("data/normis.png"), (100, 100))
        if pers == 3:
            self.image = pygame.transform.scale(pygame.image.load("data/ostrov.png"), (100, 100))

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

    def __init__(self, nom, *group):
        global mobes, zzz, fps, dmg, zuk, m_hp, iksiki, ataki, seki, bilo, stadia, nomer_ekrana, seki_2
        super().__init__(*group)
        if zuk > 0:
            m_hp.append(fps * 7)
            zuk -= 1
        self.nom = nom
        self.ataki = ataki[nom]
        self.seki = seki[nom]
        self.seki_2 = seki_2[nom]
        self.stadia = stadia[nom]
        self.dmg = dmg
        self.image = Mob.image[self.stadia]
        self.rect = self.image.get_rect()
        self.rect.x = iksiki[self.nom][0]
        self.rect.y = iksiki[self.nom][1]

    def update(self):
        global mobes, mob_ded_
        if nomer_ekrana != 2:
            self.kill()
        self.ataki = ataki[self.nom]
        self.seki = seki[self.nom]
        self.stadia = stadia[self.nom]
        self.seki_2 = seki_2[self.nom]
        self.image = Mob.image[self.stadia]
        if bilo[self.nom] == 1:
            self.rect = self.image.get_rect()
            self.rect.x = iksiki[self.nom][0]
            self.rect.y = iksiki[self.nom][1]
            bilo[self.nom] -= 1
        if self.seki < 1:
            seki[self.nom] = 0
            stadia[self.nom] = 1
            ataki[self.nom] = random.randint(1, 7)
            if ataki[self.nom] == 1:
                seki[self.nom] = fps * 3
            seki[self.nom] += round(fps / 2)
        if self.ataki != 1 and self.ataki != 0:
            seki[self.nom] -= 1
        if self.ataki == 1:
            seki_2[self.nom] = round(fps / 2)
            ataki[self.nom] = 0
        if self.ataki == 0:
            if self.seki_2 == round(fps / 2):
                stadia[self.nom] = 5
            if self.seki_2 == round(fps * 0.33):
                stadia[self.nom] = 1
            if self.seki_2 == round(fps * 0.165):
                stadia[self.nom] = 5
            if self.seki_2 == 0:
                stadia[self.nom] = 10
                ataki[self.nom] = 10
            if self.seki_2 != 0:
                seki_2[self.nom] -= 1
        self.image = Mob.image[self.stadia]
        colision = pygame.sprite.collide_mask(self, person)

        if colision:
            self.auh()

        if m_hp[self.nom] < 1:
            self.kill()
            mobes -= 1
            mob_ded_.play()

    def auh(self):
        global seki_neo, fps, hp, person_ded_
        if self.stadia != 10:
            m_hp[self.nom] -= self.dmg
        if self.stadia == 10 and seki_neo == 0:
            seki_neo += round(fps * 0.8)
            hp -= 1
            person_ded_.play()


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
        dmg = 15

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
        dmg = 10

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
        hpall = 5
        dmg = 5


def wolna():
    global iksiki, w_lvl, mobes, person, zuk, m_hp, seki, ataki, seki_neo, fps, bilo, mob1, seki_2, stadia
    m_hp = []
    iksiki = []
    seki = []
    seki_2 = []
    ataki = []
    bilo = []
    stadia = []
    seki_neo = round(fps * 2.5)
    for i in range(random.randint(math.ceil(w_lvl / 3), math.ceil(w_lvl * 2))):
        iksiki.append((random.randint(100, 850), random.randint(130, 450)))
        mobes += 1
        zuk += 1
        seki.append(round(fps / 2))
        seki_2.append(round(fps))
        stadia.append(1)
        ataki.append(2)
        bilo.append(1)

    for i in range(len(iksiki)):
        Mob(i).add(mob1)


def ekran(nomer_ekrana):
    global iksiki, mobes, w_lvl, mob1, fon_, fon_nast, fon, fon_ded
    if nomer_ekrana == 1:
        screen.fill((88, 255, 228))
        pygame.draw.rect(screen, (232, 140, 49), (300, 400, 400, 170), 0)
        pygame.draw.rect(screen, (255, 225, 68), (320, 420, 360, 130), 0)

        text = font(130).render("play", True, [255, 255, 255])
        screen.blit(text, (407, 390))

        naris(dmj_, (150, 120))

        if fon_nast == 1:
            pygame.mixer.music.load("data/fon/fon_nasr.mp3")
            pygame.mixer.music.play(-1)
            fon_nast -= 1

        persik()

    if nomer_ekrana == 2:
        screen.fill((88, 255, 228))
        if mobes == 0:
            w_lvl += 1
            wolna()
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

        if fon == 1:
            pygame.mixer.music.load(fon_[random.randint(1, 4)])
            pygame.mixer.music.play(-1)
            fon -= 1

    if nomer_ekrana == 3:
        f = open("data/sekreti.txt", "r")
        top_lvl = int(f.read())

        if fon_ded == 1:
            pygame.mixer.music.load("data/fon/fon_ded.mp3")
            pygame.mixer.music.play(-1)
            fon_ded -= 1

        if w_lvl > top_lvl:
            f = open("data/sekreti.txt", "w")
            f.write(str(w_lvl))
            f.close()
            f = open("data/sekreti.txt", "r")
            top_lvl = int(f.read())

        naris(ded_, (1000, 600))

        text1 = font(70).render("похоже, что вы умерли", True, [255, 255, 255])
        text2 = font(60).render(f'вы прошли {w_lvl - 1} волну', True, [255, 255, 255])
        text3 = font(60).render(f'ваш лучший результат {top_lvl - 1} волна', True, [255, 255, 255])

        screen.blit(text1, (50, 170))
        screen.blit(text2, (55, 270))
        screen.blit(text3, (55, 315))


clock = pygame.time.Clock()
fps = 60
zzz = False
person = Person(pers)
person.add(hero)
while True:
    ekran(nomer_ekrana)

    hero.update(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                nomer_ekrana = 1
                pygame.mixer.music.stop()
                fon_nast = 1
            if event.key == pygame.K_F5:
                for i in range(len(m_hp)):
                    m_hp[i] = -1
            if event.key == pygame.K_z:
                zzz = True
            if event.key == pygame.K_x:
                zzz = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if nomer_ekrana == 1:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and pers != 1:
                    pers -= 1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and pers != 3:
                    pers += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if int(event.pos[0]) > 300 and int(event.pos[1]) > 400 \
                            and int(event.pos[0]) < 700 and int(event.pos[1]) < 570:
                        nomer_ekrana = 2
                        pygame.mixer.music.stop()
                        fon = 1
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
            if nomer_ekrana == 3:
                nomer_ekrana = 1
                pygame.mixer.music.stop()
                fon_nast = 1

    mob1.draw(screen)
    mob1.update()
    if pygame.mouse.get_focused():
        hero.draw(screen)
    screen.blit(font(30).render(f"fps: {str(int(clock.get_fps()))}", True, [255, 255, 255]), (10, 555))
    pygame.display.flip()
    clock.tick(fps)

stop()
