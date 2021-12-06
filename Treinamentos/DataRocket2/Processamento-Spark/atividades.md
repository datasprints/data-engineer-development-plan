1 Desenvolver a extração dos dados do exemplo prático. Imagine que os dados estejam em um RDS Postgres. Crie o RDS, popule com os dados que utilizamos no exemplo prático e faça a extração.
2 Construa uma OBT (One Big Table) na zona curated
- No mesmo RDS, crie uma tabela fato da seguinte forma
    Colunas: CPF_CLIENTE, PRODUTO, VALOR
    Popule com alguns dados aleatórios de compras
- Faça a extração da tabela para zona raw (csv)
- Faça as transformações necessárias para zona staged (parquet)
- Faça o join com a tabela customers para criação da OBT