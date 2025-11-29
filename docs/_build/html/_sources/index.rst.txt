ADCTP2 - Documentação
======================

Conteúdo
========

.. toctree::
   :maxdepth: 2
   :caption: Módulos

   modules

Descrição do Projeto
====================

Este projeto consiste no desenvolvimento de um sistema **CRUD** (Create, Read, Update, Delete) aplicado ao universo da **Fórmula 1**, utilizando ficheiros **JSON** como método principal de armazenamento de dados.  
O sistema permite gerir de forma simples e organizada várias entidades relacionadas com a modalidade, incluindo:

- Utilizadores e permissões  
- Equipas  
- Pilotos  
- Chefes de equipa  
- Membros de equipa  
- Carros  
- Corridas  
- Pistas  

A aplicação funciona através de um **menu interativo no terminal**, que adapta as opções disponíveis consoante o nível de permissão do utilizador autenticado.  
As permissões possíveis são:

- ``admin``  
- ``chefe de corrida``  
- ``FIA``  
- ``utilizador``  

Todos os dados criados, atualizados ou apagados são guardados em ficheiros JSON localizados na diretoria ``src/jsons``.  
Esta abordagem permite uma forma simples, leve e legível de manter persistência de dados, sem necessidade de bases de dados externas.

Objetivos principais
--------------------

O projeto foi desenvolvido com foco em:

- **Simplicidade de utilização**  
- **Estrutura modular do código**, separando funcionalidades por categorias (creates, lists, edits, deletes)  
- **Controlo eficaz de permissões**  
- **Persistência de dados acessível e organizada**  
- **Facilidade de manutenção e expansão futura**
