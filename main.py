import pygame
from pygame import mixer
from random import randint, choice
from resource_manager import load_image, load_sound
from ui_module import start_button, button, show_score, show_bullet_use, show_alien_die, show_text
from game_logic import player, alien, bullet, bomb, is_collision

pygame.init()
screen = pygame.display.set_mode((800, 600))
bg = load_image('images/bg.jpg')  
icon = load_image('images/icon.png')
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon)
mixer.music.load('musics/menu.wav')
mixer.music.set_volume(0.4)
mixer.music.play(-1)
GAME = False
LEARN = False
MENU = True

while MENU:
	screen.blit(bg, (0, 0))
	easy = start_button(screen, (260, 50), 'EASY', (0, 0, 0), 100)
	normal = start_button(screen, (245, 200), 'MEAN', (0, 0, 0), 100)
	hard = start_button(screen, (260, 350), 'HARD', (0, 0, 0), 100)
	learn = start_button(screen, (150, 500), ' How To Play ', (0, 0, 0), 80)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			MENU = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if easy.collidepoint(pygame.mouse.get_pos()):
				COUNT_BULLET = 2
				STANDARD = 0.5
				WINS = 0.5
				GOOD_MOBS = 0.5
				BAD_MOBS = 2
				BULLET_SPEED = 2
				UFO_SPEED = 2
				BAD_SCORE = 0.5
				GOOD_SCORE = 2
				MENU = False
				GAME = True
			if normal.collidepoint(pygame.mouse.get_pos()):
				COUNT_BULLET = 1
				STANDARD = 1
				WINS = 1
				GOOD_MOBS = 1
				BAD_MOBS = 1
				BULLET_SPEED = 1
				UFO_SPEED = 1
				BAD_SCORE = 1
				GOOD_SCORE = 1
				MENU = False
				GAME = True
			if hard.collidepoint(pygame.mouse.get_pos()):
				COUNT_BULLET = 0.5
				STANDARD = 1.5
				WINS = 2
				GOOD_MOBS = 2
				BAD_MOBS = 0.5
				BULLET_SPEED = 0.5
				UFO_SPEED = 0.5
				BAD_SCORE = 2
				GOOD_SCORE = 0.5
				MENU = False
				GAME = True
			if learn.collidepoint(pygame.mouse.get_pos()):
				LEARN = True
				COUNT = 0
				if LEARN:
					screen2 = pygame.display.set_mode((800, 600))
					bg2 = pygame.image.load('images/learn.png')
					pygame.display.set_caption('How to Play')
					icon = pygame.image.load('images/icon.png')
					pygame.display.set_icon(icon)


				while LEARN:
					for e in pygame.event.get():
						if e.type == pygame.QUIT:
							LEARN = False
							MENU = False
						if COUNT > 1000:
							if e.type == pygame.MOUSEBUTTONDOWN:
								if back.collidepoint(pygame.mouse.get_pos()):
									LEARN = False
					screen2.blit(bg2, (0, 0))
					COUNT += 1
					if COUNT > 1000:
						back = start_button(screen2, (30, 270), 'BACK', (0, 0, 0), 65)
					pygame.display.update()
	pygame.display.update()

while GAME:
	pygame.init()
	bg = pygame.image.load('images/bg.jpg')
	icon = pygame.image.load('images/icon.png')
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Space Invaders')
	pygame.display.set_icon(icon)
	mixer.music.load('musics/background.wav')
	mixer.music.set_volume(0.4)
	mixer.music.play(-1)
	exp1_sound = mixer.Sound('musics/exp.wav')
	exp2_sound = mixer.Sound('musics/exp3.wav')
	exp3_sound = mixer.Sound('musics/exp2.wav')
	fire1_sound = mixer.Sound('musics/laser1.wav')
	fire2_sound = mixer.Sound('musics/laser2.wav')
	fire_sound = fire1_sound
	wrong_sound = mixer.Sound('musics/wrong.wav')
	WITCH = 1
	count_back = 0
	alien_y_back = False
	SCORE_VALUE = 0
	BULLET_USE = 0
	BULLET_Y_CHANGE = 2*BULLET_SPEED
	PLAYER_X_SPEED = 0.5*UFO_SPEED
	ALIEN_DIE = 0
	BULLET_UFO = False
	BULLET_IMG_1 = pygame.image.load('images/bullet1.png')
	BULLET_IMG_2 = pygame.image.load('images/bullet2.png')
	BULLET_IMG = BULLET_IMG_1
	UFO1 = pygame.image.load('images/ufo1.png')
	UFO2 = pygame.image.load('images/ufo2.png')
	SHOW_FONT = pygame.font.Font('freesansbold.ttf', 40)
	GAME_OVER_FONT = pygame.font.Font('freesansbold.ttf', 80)
	BUTTON_FONT = pygame.font.Font('freesansbold.ttf', 50)
	ALIEN_COUNT = int(7*BAD_MOBS)
	G_ALIEN_COUNT = int(9*GOOD_MOBS)
	PLAYER_IMG_CHANGE = True
	RUNNING = True
	GAME_OVER_RUNNING = False
	WON_GAME = False
	all_aliens = []
	for a in range(0, 20):
		all_aliens.append((a, pygame.image.load(f'images/alien{a}.png')))
	all_g_aliens = []
	for a in range(1, 9):
		all_g_aliens.append((a, pygame.image.load(f'images/g_alien{a}.png')))
	ALIEN_UFO = {
		10: 15,
		11: 16,
		12: 17,
		13: 18,
		14: 19,
	}
	ALIEN_UFO2 = [15, 16, 17, 18, 19]
	BOMB_ANIMATION = []
	for picture in range(1, 13):
		BOMB_ANIMATION.append(pygame.image.load(f'images/bomb/{picture}.png'))

	player_img = UFO1
	player_x, player_y, player_x_change = 368, 500, 0

	alien_name = []
	alien_img = []
	alien_y = []
	alien_x = []
	alien_x_change = []


	for a in range(ALIEN_COUNT):
		img = choice(all_aliens[:15])
		alien_name.append(img[0])
		alien_img.append(img[1])
		true_false = [True]
		x_size, y_size = 500, 150
		while any(true_false):
			true_false = []
			x_size = randint(6, 730)
			y_size = randint(30, 250)
			for x_point, y_point in zip(alien_x, alien_y):
				true_false.append(is_collision(x_size, y_size, x_point, y_point, 64))
		alien_x.append(x_size)
		alien_y.append(y_size)
		alien_x_change.append(randint(4, 12)/10)


	g_alien_name = []
	g_alien_img = []
	g_alien_y = []
	g_alien_x = []
	g_alien_x_change = []
	g_alien_y_change = []

	for a in range(G_ALIEN_COUNT):
		img = choice(all_g_aliens)
		g_alien_name.append(img[0])
		g_alien_img.append(img[1])
		true_false = [True]
		x_size, y_size = 500, 150
		while any(true_false):
			true_false = []
			x_size = randint(6, 730)
			y_size = randint(30, 250)
			for x_point, y_point in zip(alien_x, alien_y):
				true_false.append(is_collision(x_size, y_size, x_point, y_point, 64))
		g_alien_x.append(x_size)
		g_alien_y.append(y_size)
		g_alien_x_change.append(randint(4, 12)/10)
		g_alien_y_change.append(1)


	bullet_x, bullet_y, bullet_state = 0, 490, 'ready'
	# bullet_state='ready' bullet not shoot
	# bullet_state='fire' bullet was shoot

	animation, index, round_count, bomb_x, bomb_y = False, 0, 0, 0, 490

	while RUNNING:
		screen.blit(bg, (0, 0))
		player(screen, player_img, player_x, player_y)
		show_score(screen, SHOW_FONT, SCORE_VALUE)
		show_bullet_use(screen, SHOW_FONT, BULLET_USE)
		show_alien_die(screen, SHOW_FONT, ALIEN_DIE)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				RUNNING = False
				GAME = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player_x_change = -PLAYER_X_SPEED
				elif event.key == pygame.K_RIGHT:
					player_x_change = PLAYER_X_SPEED
				elif event.key == pygame.K_SPACE:
					if bullet_state == 'ready':
						fire_sound.play()
						bullet_x = player_x
						bullet(BULLET_IMG, bullet_x, bullet_y)
						bullet_state = 'fire'
						BULLET_USE += 1
				elif event.key == pygame.K_RETURN:
					if PLAYER_IMG_CHANGE:
						player_img = UFO2
						fire_sound = fire2_sound
						PLAYER_IMG_CHANGE = False
						PLAYER_X_SPEED = 3
						BULLET_Y_CHANGE = 6
						if bullet_state == 'ready':
							BULLET_IMG = BULLET_IMG_2
						else:
							BULLET_UFO = True
					else:
						player_img = UFO1
						fire_sound = fire1_sound
						PLAYER_IMG_CHANGE = True
						BULLET_Y_CHANGE = 2*BULLET_SPEED
						PLAYER_X_SPEED = 0.5*UFO_SPEED
						if bullet_state == 'ready':
							BULLET_IMG = BULLET_IMG_1
						else:
							BULLET_UFO = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					player_x_change = 0

		player_x += player_x_change
		if player_x > 730:
			player_x = 730
		elif player_x < 6:
			player_x = 6

		if bullet_y < -25:
			bullet_y = 480
			bullet_state = 'ready'
			if BULLET_UFO:
				BULLET_UFO = False
				if PLAYER_IMG_CHANGE:
					BULLET_IMG = BULLET_IMG_1
				else:
					BULLET_IMG = BULLET_IMG_2

		if bullet_state == 'fire':
			bullet(BULLET_IMG, bullet_x, bullet_y)
			bullet_y -= BULLET_Y_CHANGE
		if BULLET_USE > (100*COUNT_BULLET):
			try:
				if BULLET_USE/SCORE_VALUE > (2.5*STANDARD) or BULLET_USE/SCORE_VALUE < 0:
					RUNNING = False
					GAME_OVER_RUNNING = True
			except ZeroDivisionError:
				RUNNING = False
				GAME_OVER_RUNNING = True
		if SCORE_VALUE > (200*WINS):
			if 0 < BULLET_USE/SCORE_VALUE < (2.5*STANDARD):
				RUNNING = False
				WON_GAME = True

		for a in range(ALIEN_COUNT):
			alien_x[a] += alien_x_change[a]

			if alien_x[a] > 730:
				alien_x_change[a] = -randint(4, 12)/10
				alien_y[a] += randint(6, 20)
			if alien_x[a] < 6:
				alien_x_change[a] = randint(4, 12)/10
				alien_y[a] += randint(6, 20)
			alien(screen, alien_img[a], alien_x[a], alien_y[a])

			if is_collision(player_x, player_y, alien_x[a], alien_y[a], 70):
				RUNNING = False
				GAME_OVER_RUNNING = True
				break

			elif is_collision(alien_x[a], alien_y[a], bullet_x, bullet_y, 40):
				bomb_x, bomb_y, round_count, index, animation = bullet_x, bullet_y, 0, 0, True
				if BULLET_UFO:
					BULLET_UFO = False
					if PLAYER_IMG_CHANGE:
						BULLET_IMG = BULLET_IMG_1
					else:
						BULLET_IMG = BULLET_IMG_2

				if alien_name[a] in ALIEN_UFO:
					exp1_sound.play()
					alien_img[a] = all_aliens[ALIEN_UFO[alien_name[a]]][1]
					alien_name[a] = ALIEN_UFO[alien_name[a]]
					bullet_y = 480
					bullet_state = 'ready'
					alien_y_back = a

				else:
					if alien_name[a] in ALIEN_UFO2:
						exp2_sound.play()
					else:
						exp3_sound.play()
					bullet_y = 480
					bullet_state = 'ready'
					if PLAYER_IMG_CHANGE:
						SCORE_VALUE += (1*GOOD_SCORE)
					else:
						SCORE_VALUE += 1
					ALIEN_DIE += 1
					img = choice(all_aliens[:15])
					alien_img[a] = img[1]
					alien_name[a] = img[0]
					true_false = [True]
					x_size, y_size = 150, 250
					while any(true_false):
						true_false = []
						x_size = randint(6, 730)
						y_size = randint(30, 250)
						for x_point, y_point in zip(alien_x, alien_y):
							true_false.append(is_collision(
								x_size, y_size, x_point, y_point, 64))
					alien_x[a] = x_size
					alien_y[a] = y_size

		for a in range(G_ALIEN_COUNT):
			g_alien_x[a] += g_alien_x_change[a]

			if g_alien_y[a] > 420:
				g_alien_y_change[a] = -1
			elif g_alien_y[a] < 180:
				g_alien_y_change[a] = 1
			if g_alien_x[a] > 730:
				g_alien_x_change[a] = -randint(4, 12)/10
				g_alien_y[a] += randint(6, 20) * g_alien_y_change[a]
			elif g_alien_x[a] < 6:
				g_alien_x_change[a] = randint(4, 12)/10
				g_alien_y[a] += randint(6, 20) * g_alien_y_change[a]
			alien(g_alien_img[a], g_alien_x[a], g_alien_y[a])

			if is_collision(g_alien_x[a], g_alien_y[a], bullet_x, bullet_y, 40):
				bomb_x, bomb_y, round_count, index, animation = bullet_x, bullet_y, 0, 0, True
				if BULLET_UFO:
					BULLET_UFO = False
					if PLAYER_IMG_CHANGE:
						BULLET_IMG = BULLET_IMG_1
					else:
						BULLET_IMG = BULLET_IMG_2


				exp2_sound.play()
				wrong_sound.play()
				bullet_y = 480
				bullet_state = 'ready'
				if PLAYER_IMG_CHANGE:
					SCORE_VALUE -= (1*BAD_SCORE)
				else:
					SCORE_VALUE -= 1
				ALIEN_DIE += 1
				img = choice(all_g_aliens)
				g_alien_img[a] = img[1]
				g_alien_name[a] = img[0]
				true_false = [True]
				x_size, y_size = 150, 250
				while any(true_false):
					true_false = []
					x_size = randint(6, 730)
					y_size = randint(30, 250)
					for x_point, y_point in zip(alien_x, alien_y):
						true_false.append(is_collision(
							x_size, y_size, x_point, y_point, 64))
				g_alien_x[a] = x_size
				g_alien_y[a] = y_size



		if animation:
			if index == 12:
				index, round_count, animation = 0, 0, False
			bomb(BOMB_ANIMATION[index], bomb_x, bomb_y-30)
			if round_count == 15:
				round_count = 0
				index += 1
			round_count += 1

		if alien_y_back:
			alien_y[alien_y_back] = alien_y[alien_y_back] - 2
			count_back += 1
			if count_back == 7:
				count_back = 0
				alien_y_back = False
		pygame.display.update()

while GAME_OVER_RUNNING:
		quit_b = button(screen, (70, 170), ' Close Game ', (0, 0, 0))
		play_again_b = button(screen, (450, 170), ' Play Again ', (0, 0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				GAME_OVER_RUNNING = False
				GAME = False
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if quit_b.collidepoint(pygame.mouse.get_pos()):
					pygame.quit()
					GAME = False
				if play_again_b.collidepoint(pygame.mouse.get_pos()):
					GAME_OVER_RUNNING = False
		show_text('YOU LOSE', 195, 340)
		pygame.display.update()

while WON_GAME:
		quit_b = button(screen, (70, 170), ' Close Game ', (0, 0, 0))
		play_again_b = button(screen, (450, 170), ' Play Again ', (0, 0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				WON_GAME = False
				GAME = False
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if quit_b.collidepoint(pygame.mouse.get_pos()):
					pygame.quit()
					GAME = False
				if play_again_b.collidepoint(pygame.mouse.get_pos()):
					WON_GAME = False
		show_text('YOU WON', 200, 340)
		pygame.display.update()	
	
mixer.music.stop()
if GAME_OVER_RUNNING:
		game_over_sound = load_sound('musics/game_over.wav')
		game_over_sound.set_volume(0.9)
		game_over_sound.play()
	
if WON_GAME:
	win_sound = load_sound('musics/won.wav')
	game_over_sound.set_volume(0.8)
	game_over_sound.play()