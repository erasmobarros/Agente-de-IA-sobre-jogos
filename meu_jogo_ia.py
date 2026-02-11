import pygame
import math

def main_game():
    pygame.init()

    largura_tela = 800
    altura_tela = 600
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Agente G: O Jogo!")
    
    
    pos_jogador = (largura_tela // 2, altura_tela // 2)
    guarda =("Agente G", (50, 50))
    
    rodando = True
    clock = pygame.time.Clock()

   
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: pos_jogador.x -= 5
        if keys[pygame.K_RIGHT]: pos_jogador.x += 5
        if keys[pygame.K_UP]: pos_jogador.y -= 5
        if keys[pygame.K_DOWN]: pos_jogador.y += 5
        
       
        guarda.atualizar(pos_jogador)
        
       
        tela.fill((255, 255, 255)) 
        
       
        pygame.draw.circle(tela, (0, 0, 255), (int(pos_jogador.x), int(pos_jogador.y)), 15)
        
        
        pygame.draw.rect(tela, (255, 0, 0), (int(guarda.posicao.x)-15, int(guarda.posicao.y)-15, 30, 30))
        
       
        
        pygame.display.flip() 
        clock.tick(60) 

    pygame.quit()

if __name__ == "__main__":
    main_game()