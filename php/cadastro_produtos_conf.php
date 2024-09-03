<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
<!-- Início da página --> 
    <?php include 'menu.html';?>
<br>
      <br>

<!--Fim do menu -->
<?php

include 'conexao.php';
   

//Cadastra o Produto
$prod_nome = $_GET['prod_nome'];
$prod_valor = $_GET['prod_valor'];
$prod_qtde = $_GET['prod_qtde'];
$prod_volume = $_GET['prod_volume'];

if(isset($_GET['prod_nome'])) {
  // Criar a coneccao
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Verificar coneccao
  if ($conn->connect_error) {
    die("Coneccao falhou: " . $conn->connect_error);
  }

  $sql = "INSERT INTO tb_produtos (prod_nome, prod_valor, prod_qtde, prod_volume)
  VALUES ('$prod_nome', '$prod_valor', '$prod_qtde', '$prod_volume')";

  if ($conn->query($sql) === TRUE) {
    echo "Novo registro inserido";
  } else {
    echo "Erro: " . $sql . "<br>" . $conn->error;
  }

  $conn->close();
}

// FIM insere


?>
<br><br>

<a href="cadastro_produtos.php" class="btn btn-primary">Voltar para novo cadastro</a> <br> <br>
<a href="rel_produtos.php" class="btn btn-primary">Ver resultados</a>

</div>
</body>
</html>