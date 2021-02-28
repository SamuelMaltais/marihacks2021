<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MariHacks</title>
    <link rel="stylesheet" href="Styles/style.css">
    <script src="index.js"></script>
</head>
<body>
<?php
// define variables and set to empty values
$itemErr = $fbErr = "";
$quantity = $item = $fb = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["fb"])) {
    $fbErr = "FB is required";
  } else {
    $fb = test_input($_POST["fb"]);
  }

  if (empty($_POST["item"])) {
    $itemErr = "Item is required";
  } else {
    $item = test_input($_POST["item"]);
  }
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>
    <header>
        <nav>
            <ul>
                <li><a href="index.php"><b>Home</b></a></li>
                <li><a href="#"><b>Editor</b></a></li>
                <li><a href="inventory.php"><b>Inventory</b></a></li>
            </ul>
        </nav>
    </header>
    <section>        
        <div id="item">
            <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
                <p>Please Select The Food Bank:</p>
                    <input type="radio" name="fb" <?php if (isset($fb) && $fb=="FB 1") echo "checked";?> value="FB 1">FB 1<br>
                    <input type="radio" name="fb" <?php if (isset($fb) && $fb=="FB 2") echo "checked";?> value="FB 2">FB 2<br>
                    <input type="radio" name="fb" <?php if (isset($fb) && $fb=="FB 3") echo "checked";?> value="FB 3">FB 3<br>
                    <span class="error">* <?php echo $fbErr;?></span>
                    <!-- add <a> for each different food bank -->
                    <br><br>
                    Please Select The Item:
                    <input type="radio" name="item" <?php if (isset($item) && $item=="Item 1") echo "checked";?> value="Item 1">Item 1<br>
                    <input type="radio" name="item" <?php if (isset($item) && $item=="Item 2") echo "checked";?> value="Item 2">Item 2<br>
                    <input type="radio" name="item" <?php if (isset($item) && $item=="Item 3") echo "checked";?> value="Item 3">Item 3<br>
                    <span class="error">* <?php echo $itemrErr;?></span>
                    <br>
                    <input type="submit" name="submit" value="Submit">  
                  <!-- </form> -->
                    <br>
                    <input type="text" id="newitemh" name="newitem">
                    <div id="newitems"></div>
                    <button onclick="myFunction(newitem)">Add Item</button>                    
                    <br><br>
                <label for="quantity" id="spacing">New item quantity:</label>
                <input type="number" id="quantity" name="quantity" min="0" value="$quantity">
                <input type="submit">                    
            </form>
        </div>
    </section>
      <?php
      json_encode($item)
      json_encode($fb)
      ?>
    <footer>
        <p>Felix, Liam & Samuel</p>
    </footer>
</body>
</html>