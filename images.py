import pygame
import pygame.image

LARGEUR_DU_MONSTRE = 200
HAUTEUR_DU_MONSTRE = 170
ESPACE = 30


def create_layers(size):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyGame Images Example")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    return screen, background


def display(screen, background, *, image, invaders):
    screen.blit(background, (0, 0))
    # on copie toute l'image sur la zone de dessin
    screen.blit(image, (0, 0))

    for i in range(3):
        screen.blit(
            # on veut copier un boût d'invaders ...
            invaders,
            # à ces coordonnées sur la zone de dessin (screen) ...
            (20 + i * LARGEUR_DU_MONSTRE, 20 + ((i + 1) % 2) * 50),
            # et seulement cette zone.
            (
                i * (LARGEUR_DU_MONSTRE + ESPACE),
                0,
                LARGEUR_DU_MONSTRE,
                HAUTEUR_DU_MONSTRE,
            ),
        )

    # on échange la zone d'affichage et la zone de dessin pour que notre écran affiche ce qu'on a prévu.
    pygame.display.flip()


def main():
    # on charge nos images
    image = pygame.image.load("image.jpg")
    invaders = pygame.image.load("invaders.png")

    # on crée les couches
    screen, background = create_layers(image.get_size())

    # on crée le canal de transparence de l'image png
    invaders.convert_alpha()

    running = True
    display(screen, background, image=image, invaders=invaders)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        display(screen, background, image=image, invaders=invaders)


if __name__ == "__main__":
    # initialiser pygame
    pygame.init()

    try:
        # exécuter le jeu
        main()
    finally:
        # finaliser pygame, quoiqu'il arrive
        pygame.quit()
