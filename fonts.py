import pygame
import pygame.font


def create_layers():
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("PyGame Fonts Example")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    return screen, background


def display(screen, background, *, font):
    screen.blit(background, (0, 0))
    text = font.render("Bonjour, le monde.", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # on échange la zone d'affichage et la zone de dessin pour que notre écran affiche ce qu'on a prévu.
    pygame.display.flip()


def main():
    # on crée un objet "police de caractères" pour la fonte Arial, en taille 16
    font = pygame.font.SysFont("arial", 16)

    screen, background = create_layers()

    running = True
    display(screen, background, font=font)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
        display(screen, background, font=font)


if __name__ == "__main__":
    # ignorer cette partie, elle sert à afficher la liste des fontes disponibles si on passe un certain argument au programme.
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("--list", action="store_true", default=False)
    options = parser.parse_args()
    if options.list:
        print("Liste des fontes disponibles:")
        for fontname in sorted(pygame.font.get_fonts()):
            print("-", fontname)

    # initialiser pygame
    pygame.init()

    try:
        # exécuter le jeu
        main()
    finally:
        # finaliser pygame, quoiqu'il arrive
        pygame.quit()
