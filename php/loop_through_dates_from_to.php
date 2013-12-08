<?php
/*
PHP: Loop through dates (from date to date) with strtotime() function
This is very easy way loop through dates (from date to date) with PHP strtotime() function. This example only echo dates, but of course this model can be used more complicated situations.
*/

        // Set timezone
        date_default_timezone_set('UTC');
 
        // Start date
        $date = '2009-12-06';
        // End date
        $end_date = '2020-12-31';
 
        while (strtotime($date) <= strtotime($end_date)) {
                echo "$date\n";
                $date = date ("Y-m-d", strtotime("+1 day", strtotime($date)));
        }
 

//Note: All different PHP strtotime() function syntaxes can be used.

 
        // Set timezone
        date_default_timezone_set('UTC');
 
        echo strtotime("now") . "\n";
        echo strtotime("10 October 2010") . "\n";
        echo strtotime("next Friday") . "\n";
        echo strtotime("last Tuesday"), "\n";
 
?>