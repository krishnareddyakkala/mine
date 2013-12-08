<?php
/*
Method 1 – PHP: Remove Last Character from String using substr and mb_substr
substr and mb_substr commands usage
substr($string, 0, -1);
mb_substr($string, 0, -1);
substr and mb_substr example:
$string = "This is test string..";
echo $string . "\n";
 */
// substr function
echo "substr: " . substr($string, 0, -1);
 
echo "\n";
 
// mb_substr multibyte version
echo "mb_substr: " . mb_substr($string, 0, -1);
 
echo "\n";
/*
Example output:
This is test string..
This is test string.
This is test string.
*/
/*
Method 2 – PHP: Remove Last Character from String using substr_replace
substr_replace command usage
 */
substr_replace($string ,"",-1);
//substr_replace example:
$string = "This is test string..";
echo $string . "\n";
 
// substr_replace function
echo "substr_replace: " . substr_replace($string ,"",-1);
 
echo "\n";
/*
Example output:
This is test string..
This is test string.
 */
/*
Method 3 – PHP: Remove Last Character from String using rtrim
Note: rtrim function is not working exactly same way as substr and substr_replace, but it is of course useful some cases. Rtrim function trims all specified characters from end of the string.
rtrim command usage
rtrim($string,'x');
 */
//rtrim example:
$string = "This is test string..";
echo $string . "\n";
 
// rtrim function
echo "rtrim: " . rtrim($string, ".");
 
echo "\n";
/*
Example output:
This is test string..
This is test string
 * 
 */
?>
