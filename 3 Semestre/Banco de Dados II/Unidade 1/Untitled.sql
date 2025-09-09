CREATE TABLE `produtos` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `descricao` varchar(80),
  `valor` float,
  `ativo` int
);

CREATE TABLE `clientes` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(80),
  `endereco` varchar(150),
  `ativo` int
);

CREATE TABLE `pedidosClientesProdutos` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `cliente_id` int,
  `produtos_id` int,
  `qtd` float,
  `situacao` int
);

ALTER TABLE `pedidosClientesProdutos` ADD FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`);

ALTER TABLE `pedidosClientesProdutos` ADD FOREIGN KEY (`produtos_id`) REFERENCES `produtos` (`id`);
