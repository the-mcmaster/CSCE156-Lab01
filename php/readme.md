
# PHP 

Only those in the Honors section need to complete this section on
PHP.

The project you checked out from GitHub contains a `php` folder 
which contains several PHP scripts.  To run these scripts you 
will need a PHP interpreter.  To do this, we will reclone the
project from the CSE command line.

1. Open Putty (https://putty.org/, Windows) or terminal (Mac) and 
login to the cse server using your CSE credentials.
2. Clone the project from github using the following command.  
`git clone https://github.com/cbourke/CSCE156-Lab01`
3. Open the file, `statistics.php` in the text editor of your choice.
If you are familiar with the command line, pico, emacs, or vi are 
good text editors.  Otherwise, you can review our BYOD setup video:  
https://www.youtube.com/watch?v=6UaJ2zFs7VQ&list=PL4IH6CVPpTZVkiEnCEOdGbYsFEdtKc5Bx
4. The script prompts the user to enter a number of integers 
and computes several statistics (minimum, maximum, average, sum) and 
outputs the results.  Most of the program's framework has been provided 
for you.  In this activity, you will write the remainder of the program.
5. To run the script from the command line, execute the following command.  
`php statistics.php`
6. Though the script runs, it does not output the correct values.  
To get it to work, you will need to implement the following two 
functions:
* `getMax($array)` - This method should return the maximum of the 
elements in the array.
* `getSum($array)` - This method should return the sum of the 
elements in the array.
7. Rerun your program to check that it works.

## Modifying The Script

The program you've completed is interactive in that it prompts the 
user for input.  You will now change the script to instead use 
command line arguments to read in the list of numbers directly 
from the command line.

PHP supports command line arguments by providing a built-in array, 
`$argv` which is 0-indexed.  Note: the first element in this array 
is the script's name, so you will need to process starting from 
index 1.  Once you have made the appropriate changes, you should 
be able to execute your script as follows:
`php statistics.php 10 20 30 40`

## PHP in a Dynamic Webpage

You will now utilize PHP in a dynamic, interactive web page.  The 
webserver is responsible for handling requests from clients 
(browsers), executing the proper PHP script(s) and returning the 
output (HTML) to the client.  This activity will have you finishing 
two PHP pages that reads a user's name and birthday and tells them 
how old they are.

1. The Apache webserver on CSE has been setup so that each user 
can place files into a `public_html` directory and these files will 
be available through a web browser.  To create this directory, use 
the following command:
`mkdir public_html`
2. Make sure your `public_html` directory world-executable using 
this command:
`chmod go+x public_html`
3. Copy the `birthday.php` and `birthday_result.php` files into 
your `public_html` directory and make them world-readable using 
the command:
`chmod o+r *.php`
3. Open a web browser using the URL, http://cse.unl.edu/~login/birthday.php
`login` replaced with your CSE login.	You will need to modify the 
scripts to get them working properly.  

The `birthday.php` page should render in your web browser without 
any problems.  However, it is incomplete.  Take these steps to get 
it in working order.

1. There are several months missing from the drop down menu.  Include 
them by modifying the code that builds the `$month` array.
2. Modify the code as indicated to populate the `Date` drop 
down menu so that dates 1 thru 31 appear.  Use the year drop 
down menu as a model.

The HyperText Transfer Protocol (HTTP) allows clients to 
`POST` data to another page for processing.  You'll notice that your 
HTML form in `birthday.php` is configured to post its results to 
`birthday_result.php`.  Parameters posted to this page are specified 
by the input elements in the HTML form using the name property.  In 
the result page, these parameters are available through the `$_POST`
array.  This is an associative array (indexed by strings).  You can 
get the posted values using the syntax: `$name = $_POST['name'];`
where `'name'` is replaced with the name of the form value.

1. Modify the result page to pull the values posted from the form page.
2. Also modify the script as indicated to print the appropriate message.  
If today is the user's birthday, print `Happy Birthday!`, otherwise print 
`Your friends have XX shopping days until your next birthday` where `XX` 
is the appropriate variable value.  Note: strings can be concatenated 
with variable values in PHP by using the period operator.  An example:
```php
print "This is PHP, version " . $version . ", have fun!";
```

## Submitting and Grading Your Program

Submit the `statistics.php` file to the webhandin and grade
yourself with the webgrader to complete your lab.

## Advanced Activity (Optional)

Enter an invalid birthdate into your web page and observe 
what happens.  Is this behavior ideal?  Think about some 
alternatives to handle invalid dates.

Most web pages utilize some JavaScript or JavaScript frameworks 
or libraries to make the web page dynamic.  Dates are usually 
entered by having a calendar-like popup appear and have the 
users click actual dates on the calendar.  This provides a 
much better user experience and has the added benefit of 
preventing invalid dates.  

Familiarize yourself with jQuery and in particular, the "Datepicker" 
jQuery UI plugin (http://jqueryui.com/demos/datepicker/#dropdown-month-year) 
and integrate it into your PHP page.  Note: changes will need 
to be made to both the input and the result page.

