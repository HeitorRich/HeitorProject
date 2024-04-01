from django.db import models

# Create your models here.
class Fornecedor(models.Model):
    nome = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    estados = [
        ('RJ', 'RJ'),
        ('SP', 'SP'),
        ('MG', 'MG'),
        ('BA', 'BAHIA'),
        ('GO', 'GOIAS'),
        ('PR', 'PARANÁ'),
        ('RS', 'RS'),
        ('OUTRA', 'OUTRA')
    ]

    estado = models.CharField(max_length=6, choices=estados)

    class Meta:
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome_da_categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_da_categoria

class Produto(models.Model):

    CORES = [
        ('BRC', 'Branco'),
        ('PRT', 'Preto'),
        ('AMA', 'Amarelo'),
        ('VRD', 'Verde'),
        ('VML', 'Vermelho'),
        ('AZL', 'Azul'),
        ('ROS', 'Rosa')
    ]

    nome_do_produto = models.CharField(max_length=50)
    descricao = models.TextField(max_length=8000, verbose_name="Descrição")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    estoque = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField()
    data_de_validade = models.DateField(blank=True, null=True)
    cor = models.CharField(max_length=3,blank=True, null=True, choices=CORES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    fornecedor = models.ManyToManyField(Fornecedor, null=True, blank=True)

    def __str__(self):
        return self.nome_do_produto