<!DOCTYPE html>
<html>

<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>PIZZA LIST</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>

<body>

    <form action="confirm_order.php" method="post">

        <?php

        session_start();
        $pizza_list = $_SESSION["pizzas"];
        $pizzas = array();
        $total_price = 0;

        if (isset($_POST["selected_pizza"]) && is_array($_POST["selected_pizza"])) {
            $_SESSION["selected_pizza_nrs"] = $_POST["selected_pizza"];
            echo 'Tilaus:<br>';
            foreach ($pizza_list as $pizza) {

                if (in_array($pizza[0], $_POST["selected_pizza"])) {
                    $pizzas[] = $pizza;
                    foreach ($pizza as $item_nr => $value) {
                        if ($item_nr == 0) {
                            echo $value;
                        } elseif ($item_nr == 2) {
                                $total_price += $value;
                                echo ', ' . $value . ' €';
                        } else {
                            echo ', ' . $value;
                        }
                    }
                    echo '<br>';
                } // if

            } // foreach
            echo '<br>Kokonaishinta: ' . $total_price . ' €<br>';
        } // if

        // Client didn't choose anything so return back
        if (count($pizzas) == 0) {
            header('location: print_order_form.php');
        }
        $_SESSION["selected_pizzas"] = $pizzas;
        $_SESSION["total_price"] = $total_price;

        ?>

        <input type="submit" formaction="print_order_form.php" value="Muokkaa tilausta">
        <input type="submit" value="Vahvista tilaus">
    </form>
</body>

</html>