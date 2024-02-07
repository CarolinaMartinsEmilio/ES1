import unittest
from src.main import Aves

class TestAvesMethods(unittest.TestCase):
    def setUp(self):
        self.viveiro = Aves()

    def test_criar_ave_erro_passando_nome_como_number(self):
        with self.assertRaises(ValueError):
            self.viveiro.criar_ave(30, "Passeriforme", 30)

    def test_criar_ave(self):
        self.viveiro.criar_ave("Canarinho", "Passeriforme", 30)
        self.assertEqual(len(self.viveiro.aves), 1)
        self.assertEqual(self.viveiro.aves[0]["nome"], "Canarinho")

    def test_atualizar_ave(self):
        self.viveiro.criar_ave("Canarinho", "Passeriforme", 30)
        self.viveiro.atualizar_ave("Canarinho", "Pardal", 35)
        self.assertEqual(self.viveiro.aves[0]["especie"], "Pardal")
        self.assertEqual(self.viveiro.aves[0]["peso"], 35)

    def test_deletar_ave(self):
        self.viveiro.criar_ave("Canarinho", "Passeriforme", 30)
        self.viveiro.deletar_ave("Canarinho")
        self.assertEqual(len(self.viveiro.aves), 0)

    def test_listar_aves(self):
        self.viveiro.criar_ave("Canarinho", "Passeriforme", 30)
        self.viveiro.criar_ave("Arara", "Psitacídeo", 1500)

        # Redireciona a saída padrão para um buffer
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.viveiro.listar_aves()

        # Obtém a saída do buffer
        output = sys.stdout.getvalue()

        # Restaura a saída padrão
        sys.stdout = original_stdout

        # Verifica se as aves estão na saída
        self.assertIn("Canarinho", output)
        self.assertIn("Arara", output)

if __name__ == "__main__":
    unittest.main()
