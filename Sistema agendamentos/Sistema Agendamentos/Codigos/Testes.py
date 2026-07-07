import unittest
from Codigos.sistema_tickets import Database, Ticket, Supervisor, Atendente


# ============================================================
# Resetar o Singleton entre cada teste
# ============================================================

def resetar_banco():
    Database._instancia = None


# ============================================================
# TESTES — Database.salvar_ticket
# ============================================================

class TesteSalvarTicket(unittest.TestCase):

    def setUp(self):
        resetar_banco()
        self.db = Database()

    # Cenário de sucesso — ticket salvo corretamente
    def test_ticket_salvo_na_lista(self):
        ticket = Ticket("João Silva", "Rua das Flores, 123", "manutenção")
        self.db.salvar_ticket(ticket)
        self.assertIn(ticket, self.db.listar_tickets())

    # Cenário de borda — salvar múltiplos tickets
    def test_multiplos_tickets_salvos(self):
        t1 = Ticket("João Silva", "Rua A, 1", "manutenção")
        t2 = Ticket("Maria Lima", "Rua B, 2", "limpeza")
        t3 = Ticket("Carlos Souza", "Rua C, 3", "monitoramento")
        self.db.salvar_ticket(t1)
        self.db.salvar_ticket(t2)
        self.db.salvar_ticket(t3)
        self.assertEqual(len(self.db.listar_tickets()), 3)

    # Cenário de borda — Singleton compartilha os mesmos dados
    def test_singleton_compartilha_dados(self):
        ticket = Ticket("João Silva", "Rua das Flores, 123", "manutenção")
        self.db.salvar_ticket(ticket)
        outro_banco = Database()
        self.assertIn(ticket, outro_banco.listar_tickets())


# ============================================================
# TESTES — Ticket.atualizar_status
# ============================================================

class TesteAtualizarStatus(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket("Maria Lima", "Av. Central, 456", "limpeza")

    # Cenário de sucesso — status atualizado corretamente
    def test_status_atualizado(self):
        self.ticket.atualizar_status("concluído")
        self.assertEqual(self.ticket.status, "concluído")

    # Cenário de falha — status inicial é sempre agendado
    def test_status_inicial_e_agendado(self):
        self.assertNotEqual(self.ticket.status, "concluído")
        self.assertEqual(self.ticket.status, "agendado")

    # Cenário de borda — observer notificado ao atualizar status
    def test_observer_notificado(self):
        notificados = []

        class ObserverFake:
            def notificar(self, ticket):
                notificados.append(ticket.status)

        self.ticket.adicionar_observer(ObserverFake())
        self.ticket.atualizar_status("concluído")
        self.assertIn("concluído", notificados)


# ============================================================

if __name__ == "__main__":
    unittest.main(verbosity=2)