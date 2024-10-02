<html lang="pt-br">
  <head>
    <title>PHP Test</title>
  </head>
  <body>
    <?php 
    
      $color = "vermelho";
      echo "Meu carro é " . $color . "<br>"."<br>";

      $Color = "Verde";
      echo "Meu carro é " . $Color . "<br>"."<br>";
   
      $COLOR = "AZUL";
      echo "Meu carro é " . $COLOR . "<br>"."<br>";

      
      //*$x = 5; // inteiro (números inteiros)
      //*$y = 4; // string(texto), float(decimal), booleano(verdadeiro/falso), array(lista, objetos)
      //*echo $x + $y ."<br>"."<br>";

    //*a função var_dump() retorna o tipo de variável e seu valor;
    //*$x = 5;
    //*var_dump($x);
    //* '' a variável se torna texto

    

      $nome = "Olá CAVALO";

      echo "CAVALO" ."<br>"."<br>";
      echo strlen($nome)."<br>"."<br>";//* Conta quantas letras tem na variável
      echo str_word_count($nome)."<br>"."<br>";//* Conta quantas palavras tem na variável
      echo strpos($nome, "CAVALO") ."<br>"."<br>"; //* Ele busca a variável e retorna a posição da palavra
      echo strtoupper($nome)."<br>"."<br>";//* Transforma em letras maiúsculas
      echo strtolower($nome)."<br>"."<br>";//* Transforma em letras minúsculas
      echo str_replace("CAVALO", "Cavalo", $nome)."<br>"."<br>"; //* Substitui a palavra
      echo trim($nome)."<br>"."<br>"; //* Remove espaços em branco
      $x = "Queijo ralado";//* Separa as palavras por espaço  
      $y = explode(" ", $x);
      echo $y[0]."<br>"."<br>";
    
    ?> 

    

</html>