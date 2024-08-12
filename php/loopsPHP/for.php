<?php

    $i = 0;
    $tam = 5;
    $vet = [$tam]

    for($i=0; $i < $tam; $i++)
    {
        echo"O valor de i: $i</br>";
    }
    ///////////////////////////////////

    for($i=0; $i < $tam; $i++)
    {
        $vet = [$i] = 0;
    }

    

    for($i=0; $i < $tam; $i++)
    {
        $vet = [$i] = 0;        
        echo"O valor da pos. $i : $vet[$i] </br>";
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
