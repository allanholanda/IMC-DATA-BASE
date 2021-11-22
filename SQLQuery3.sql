-- Criando base de dados --
CREATE DATABASE Base_IMC

-- Alterando para a base Base_IMC --
USE Base_IMC

-- Criando tabelas --
CREATE TABLE Dados_Corporais (
	Id = 
	Nome varchar(50) not null,
	Idade int not null,
	Peso float not null,
	Altura float not null,
	Imc float not null,
)

select nome, imc from Dados_Corporais
select * from Dados_Corporais 

delete from Dados_Corporais

drop table Dados_Corporais
