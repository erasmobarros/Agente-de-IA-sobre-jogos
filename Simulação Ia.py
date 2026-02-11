import math

class Posicao:
    """Uma classe simples para representar uma posição 2D."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def calcular_distancia(pos1, pos2):
    """Calcula a distância Euclidiana entre dois pontos."""
    return math.sqrt((pos2.x - pos1.x)**2 + (pos2.y - pos1.y)**2)

class Guarda:
    """Representa o agente de IA (o guarda)."""
    
    def __init__(self, nome, pos_inicial):
        self.nome = nome
        self.posicao = pos_inicial
        self.estado = 'PATRULHANDO'  # Estado inicial
        
        # Pontos de patrulha definidos
        self.ponto_patrulha_A = Posicao(0, 0)
        self.ponto_patrulha_B = Posicao(10, 5)
        self.alvo_atual = self.ponto_patrulha_B
        
        # "Memória" do guarda
        self.ultima_posicao_vista_jogador = None
        self.contador_perda_de_visao = 0
        
        # Atributos/Habilidades do agente
        self.raio_visao = 8.0
        self.raio_captura = 1.5
        self.velocidade = 1.0

    def atualizar(self, pos_jogador):
        """
        Este é o "cérebro" do guarda, executado a cada turno (ou frame) do jogo.
        Ele decide o que fazer com base no estado atual e na posição do jogador.
        """
        distancia_para_jogador = calcular_distancia(self.posicao, pos_jogador)
        
        # Lógica de Decisão (transição entre estados) baseada na percepção (distância)
        if self.estado == 'PATRULHANDO':
            if distancia_para_jogador < self.raio_visao:
                self.estado = 'PERSEGUINDO'
        elif self.estado == 'PERSEGUINDO':
            if distancia_para_jogador > self.raio_visao:
                self.estado = 'INVESTIGANDO'
        # ... (e assim por diante para os outros estados)

        # Lógica de Ação (o que fazer em cada estado)
        if self.estado == 'PATRULHANDO':
            self.mover_em_direcao_a(self.alvo_atual)
        elif self.estado == 'PERSEGUINDO':
            self.mover_em_direcao_a(pos_jogador)
        # ... etc.
            
    def mover_em_direcao_a(self, alvo):
        """Move o guarda 1 passo na direção do alvo."""
        if self.posicao.x < alvo.x: self.posicao.x += self.velocidade
        elif self.posicao.x > alvo.x: self.posicao.x -= self.velocidade
        if self.posicao.y < alvo.y: self.posicao.y += self.velocidade
        elif self.posicao.y > alvo.y: self.posicao.y -= self.velocidade

# Função principal que roda a simulação
def main():
    agente_g = Guarda("Agente G", Posicao(0, 0))
    jogador = Posicao(20, 10)

    for turno in range(1, 25):
        print(f"\n====== TURNO {turno} ======")
        print(f"Guarda está em ({agente_g.posicao.x:.1f}, {agente_g.posicao.y:.1f}) | Estado: {agente_g.estado}")
        
        # Movimento simulado do jogador
        if 5 <= turno < 15:
            jogador.x -= 1.5
        
        resultado = agente_g.atualizar(jogador)
        if resultado == 'CAPTURADO':
            break

if __name__ == "__main__":
    main()