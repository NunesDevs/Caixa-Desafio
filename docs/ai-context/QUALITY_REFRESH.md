# Memória técnica — revisão de qualidade

Revisão: 2026-11-08. Este arquivo descreve o código validado nesta rodada; inventários automáticos anteriores registram estados históricos.

Núcleo cash.py compartilhado pelas três entradas históricas, todas com guarda main. Valores monetários usam Decimal e validação de finitude, limites e centavos. Busca exata limitada a 199 unidades corrige a escolha gulosa para R$6/R$8/R$101. Débito corresponde ao valor efetivamente entregue; saldo aleatório da versão 2 é simulado, sem acesso bancário. Cinco testes passaram em Python 3.12, incluindo referência de mínimo de cédulas até 600 e execução real das três entradas/EOF. Requer Python 3.10+ pela anotação de tipo; sem dependências externas. Distribuição em pacote MIT de scripts com checksum.

Validações: comandos de teste do README, execução local sem dados reais, git diff --check e revisão dos arquivos antes do commit. Push/integração/publicação têm autorização explícita do titular nesta sessão. Nenhuma migração, seed ou serviço de produção foi executado.
