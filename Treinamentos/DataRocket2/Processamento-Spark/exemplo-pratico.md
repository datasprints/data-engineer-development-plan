Imaginemos uma base de dados onde temos dados de cadastro de clientes. Os dados são cadastrados de forma manual pelo time comercial, mas por falta de um processo bem definido, temos dados faltantes e duplicados. O time de engenharia utiliza uma aplicação Python para disponibilizar os dados crus na camada raw do Data Lake. Precisamos desenvolver um código para tratar esses dados e disponibilizar na zona staged do nosso Data Lake.
O que nós temos para resolver o problema por enquanto:
- Base de dados dos clientes na zona raw;
- Precisamos deduplicar os dados;
- Precisamos preencher dados faltantes;
