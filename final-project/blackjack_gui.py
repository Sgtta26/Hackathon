# import pygame

# pygame.init()

# # ouvrir une fenetre 
# screen = pygame.display.set_mode((400, 400))

# running = True

# # importer image
# image = pygame.image.load("ball.png").convert()

# # fenetre qui ne se ferme pas
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # afficher l'image
#     screen.blit(image, (0, 0))

#     # met a jour l'image pour etre afficher
#     pygame.display.flip()

# pygame.quit()

import pygame

# create GUI (Graphical User Interface)
pygame.init()

# initialize GUI window

win_width = 400
win_height = 200
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("BLACKJACK by Sarah Guetta")

run_game = True

# main game loop
while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # GUI window will remain open until [x] button is clicked or GUI is closed
            run_game = False

pygame.quit()


# IMPORTER LES IMAGES DES CARTES !!

# Define Pixel Size of card
card_width = 100
card_height = 150

card_img_dir = []
card_img = []

# Obtain directory and objects for card images

# card-name = face / face2 / face3 a verifier !!!
for i in card_names:
    for j in card_suits:
        card_img_dir.append("images/" + str(i) + "-" + str(j) + ".png")

for i in card_img_dir:
    card_img.append(pygame.transform.scale(pygame.image.load(i), (card_width, card_height)))

bg_card = card(0,0,0, pygame.transform.scale(pygame.image.load("images/blue_back.png"), (card_width, card_height)))




