# ============================================================
# Sistema de Agendamento de Visitas Técnicas
# Padrões utilizados: Singleton e Observer
# ============================================================


# ============================================================
# PADRÃO SINGLETON — Banco de Dados
# Garante uma única instância de dados no sistema (H1)
# ============================================================

class Database:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.tickets = []
        return cls._instancia

    def salvar_ticket(self, ticket):
        self.tickets.append(ticket)
        print(f"[DB] Ticket salvo: {ticket}")

    def listar_tickets(self):
        return self.tickets


# ============================================================
# PADRÃO OBSERVER — Notificação de status
# Notifica automaticamente os interessados quando o
# status de um ticket é atualizado (H3)
# ============================================================

class Observer:
    def notificar(self, ticket):
        pass


class Supervisor(Observer):
    def notificar(self, ticket):
        print(f"[Supervisor] Status atualizado → {ticket}")


class Atendente(Observer):
    def notificar(self, ticket):
        print(f"[Atendente] Visita atualizada → {ticket}")


# ============================================================
# TICKET — Subject do Observer
# ============================================================

class Ticket:
    def __init__(self, cliente, endereco, tipo):
        self.cliente = cliente
        self.endereco = endereco
        self.tipo = tipo
        self.status = "agendado"
        self._observers = []

    def adicionar_observer(self, observer):
        self._observers.append(observer)

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"\n[Técnico] Atualizando status para '{novo_status}'...")
        for obs in self._observers:
            obs.notificar(self)

    def __str__(self):
        return f"Cliente: {self.cliente} | Tipo: {self.tipo} | Status: {self.status}"


# ============================================================
# SIMULAÇÃO
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print(" SISTEMA DE AGENDAMENTO DE VISITAS TÉCNICAS")
    print("=" * 55)

    # Singleton — mesma instância do banco em qualquer lugar
    db1 = Database()
    db2 = Database()
    print(f"\n[Singleton] db1 é db2? {db1 is db2}")  # True

    # H1 — Atendente registra um agendamento
    print("\n--- H1: Atendente registra visita ---")
    ticket = Ticket(
        cliente="João Silva",
        endereco="Rua das Flores, 123",
        tipo="manutenção"
    )

    supervisor = Supervisor()
    atendente = Atendente()
    ticket.adicionar_observer(supervisor)
    ticket.adicionar_observer(atendente)

    db1.salvar_ticket(ticket)

    # H3 — Técnico atualiza o status da visita
    print("\n--- H3: Técnico atualiza status ---")
    ticket.atualizar_status("concluído")

    print("\n--- Listando todos os tickets ---")
    for t in db1.listar_tickets():
        print(f" → {t}")