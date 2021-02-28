
<!DOCTYPE html>
<html lang="en">
<style>
    *{
    padding: 0;
    margin: 0;  
    box-sizing: border-box;  
}
body{
    background-color: #f8f9fa;
}
#map{
    margin: 2rem auto;
    width: 70%;
    height: 100%;
}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
}  
  li {
    float: left;
  }
  
  li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }
  li a:hover {
    background-color: #111;
  }  
#locations{
    display: block;
    text-align: center;
    padding: 1rem;
}
#locations div{
    font-size: 1.5rem;
    margin: 1rem auto;
    width: 60%;
    color: #fff;
    background-color: #333;
    padding: 2rem;
}
#first{
  margin: 1rem;
}
.dropbtn {
  background-color: #333;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {background-color: #ddd;}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {display: block;}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {background-color: rgb(80, 80, 80);}

#submit a{
  display: inline-block;
  text-decoration: none;
  color: #fff;
  margin: 10rem 1rem 1rem 1rem;
  padding: 1em;
  border-radius: 10px;
  background-color: #333;
}
#item{
  display: inline-block;
  color: #fff;
  background-color: #333;
  padding: 2rem;
  margin: 2rem 0 0 2%;
}
form p{
  margin-bottom: 0.5rem;
}
footer{
    color: #fff;
    background-color: #333;
    text-align: center;
    padding: 0.5em;
    bottom: 0;
    position: absolute;
}
</style>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MariHacks</title>
    <link rel="stylesheet" href="Styles/style.css">
    <script src="index.js"></script>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href=""><b>Home</b></a></li>
                <li><a href="editor"><b>Editor</b></a></li>
                <li><a href="#"><b>Inventory</b></a></li>
            </ul>
        </nav>
    </header>
    <section>
        {%for item in items%}
        <div class="container">
            <P>
            item: {{item.item}}
            amount: {{item.amount}}
            </P>
        </div>
        {%endfor%}
    </section>
    <footer>
        <p>Felix, Liam & Samuel</p>
    </footer>
</body>
</html>