# Cabeleleila-Leila

Teste para estagio Dsin 
Sistema desenvolvido em Python


        Tela Inicial como sistema de login

![image](https://github.com/LucasMatheus144/Cabeleleila-Leila/assets/79222732/2a470257-aa9d-4854-ab0e-488cecd61c6b)


1 - Login do Usuario
  Verifica se existe o login e a senha no banco de dados, caso exista ela leva a tela de usuarios
  caso nao exista, leva a tela de Cadastro ou tentar novamente fazer o login
  cadastrado no banco -> Adminstrador -->  Login: Admin1  ,  Senha: admin1
  
2 - Cadastro do Usuario
  Pede um login e uma senha, depois pede as informaçoes do usuario como Nome Completo, telefone, 
  endereço, email e rg. Depois salva no banco de dados Usuario e Cliente
 
        Tela do Administrador
 
 ![image](https://github.com/LucasMatheus144/Cabeleleila-Leila/assets/79222732/ceffcb0f-c4a4-4ab8-bdde-f63222ca542d)
 
 
1 - Mudar algum agendamento dos cliente
  Pede o nome da pessoa que deseja alterar o agendamento, ele mostra a data antiga e pede uma nova
  data para mudar o agendamento
  
2 - Desmarcar algum agendamento
  Pede o nome do Cliente e pega o ID , e faz o update salvando como Sem Consulta no banco de dados do Cliente

3 - Deletar Cliente do Sistema
  Pega o nome e o ID do usuario e deleta do banco de danos Cliente e Usuario
  
4 - Mostrar os dados dos clientes
  Pegunta se quer saber de algum dado de cliente especifico e mostra todos os dados
  
        Tela do Cliente

![image](https://github.com/LucasMatheus144/Cabeleleila-Leila/assets/79222732/f5a515b1-4bd2-4b64-8616-e0e7f21f05ca)


1 - Marcar agendamento
  Pede o dia do agendamento e adiciona ao banco de dados
  
2 - Remarcar Agendamento
  Pega o dia marcado para o agendamento, compara com o dia atual, se o agendamento for marcado para menos de 2 dias,
  so conseguira remarcar fazendo o telefonema para o salao, caso ao contrario será pedido um novo dia e fazer o 
  Update no banco de dados
  
3 - Desmarcar Consulta
  Seleciona o ID do cliente e do Usuario e deleta de ambos os bancos
  
4 - Mostrar meus dados
  Seleciona o Id do cliente e mostra todos os dados existentes da conta
  
