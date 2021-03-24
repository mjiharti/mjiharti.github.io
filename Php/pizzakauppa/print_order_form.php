<!DOCTYPE html>
<html>

<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>PIZZA LIST</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
</head>

<body>

    <form action="handle_order.php" method="post">
        
        <?php

        /**
         * Simple exercise to read a CSV file, print a form and store some session data 
         */

         session_start();
        $file_name = "data/pizzalist.txt";
        if (file_exists($file_name)) {
            $myfile = fopen($file_name, "r") or die("Unable to open pizza file!");
        } else {
            die("Unable to open pizza file!");
        }
        $pizzas = array();
        $session_on = false;
        if (isset($_SESSION["selected_pizza_nrs"])) {
            $session_on = true;
        }

        while (!feof($myfile)) {            
            $row = fgets($myfile);            
            $sub_strings = explode(',', $row);
            $pizza = array($sub_strings[0], $sub_strings[1], $sub_strings[2]);
            
            foreach ($sub_strings as $counter => $item) {
                if ($counter == 0) {
                    echo '<br><input type="checkbox" name="selected_pizza[]"' . (($session_on && in_array($item, $_SESSION["selected_pizza_nrs"]))? ' checked ' : '') . 'value="', $item, '">';
                } elseif ($counter == 1) {
                    echo $item;
                } elseif ($counter == 2) {
                    echo ', ' . $item . ' €';
                } else {
                    $pizza[] = $item;
                    echo ', ' . $item;
                }
                $counter++;
            } // foreach   

            $pizzas[] = $pizza;            

        } // while
        
        fclose($myfile);
        $_SESSION["pizzas"] = $pizzas;

        ?> 

        <br>
        <input type="submit" value="Tilaa">
    </form>

</body>

</html>