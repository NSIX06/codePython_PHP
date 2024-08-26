<?php
$i = 0;
$tam = 5;
$vet = array(); // Inicialize o array vazio

for ($i = 0; $i < $tam; $i++) {
    echo "O valor de i: $i</br>";
}

// Agora, vamos preencher o array com zeros
for ($i = 0; $i < $tam; $i++) {
    $vet[$i] = 0;
}

// Agora, vamos exibir os valores do array
for ($i = 0; $i < $tam; $i++) {
    echo "O valor da pos. $i: {$vet[$i]} </br>";
}
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

</body>

</html>