<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tilaus lähetetty</title>
</head>

<body>

    <?php

    session_start();
    $ordered_pizzas = $_SESSION["selected_pizzas"];    
    echo 'Tilasit:<br>';

    foreach ($ordered_pizzas as $pizza) {
        foreach ($pizza as $item_nr => $value) {
            if ($item_nr == 0) {
                echo $value;
            } else {
                echo ', ' . $value . (($item_nr == 2) ? ' €' : '');
            }
        } // foreach
        echo '<br>';
    } // foreach

    echo '<br>Kokonaishinta: ' . $_SESSION["total_price"] . ' €';
    // TODO insert data into the db

    unset($_SESSION["selected_pizzas"]);
    unset($_SESSION["selected_pizza_nrs"]);
    unset($_SESSION["total_price"]);

    ?>
    <form acction="#"><input type="submit" formaction="print_order_form.php" value="Palaa alkuun"></form>
</body>

</html>