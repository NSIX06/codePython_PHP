<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IMC</title>
</head>
<body>

<form action="">
    <label for="altura">Altura</label>
    <input type="text" name = "altura">
    <label for="peso">Peso</label>
    <input type="text" name = "peso">
    <label for="genero">Gênero</label>
    <input type="text" name = "genero">
    <input type="submit" value = "Verificar">
</form>

    <?php
    

        if (isset($_GET["altura"])) && (isset($_GET["genero"])){


            $altura = $_GET["altura"];
            $genero = $_GET["genero";]

            if ($genero == "M"){

                $peso = (72.7 * $altura) - 58;
            }

            else{

                $peso = (62.1 * $altura) - 44.;
            }
            
            echo "Você informou o seu gênero é $genero e $altura, então seu peso ideal é $peso"
        }
    
    
    
    
    ?>

</body>
</html>