<?php
/*
 * PHP mb_ucfirst Make a String’s First Character Uppercase-Multibyte (UTF-8) Function
 * PHP’s ucfirst function is very usefull when you want to change words first letters to uppercase and other letters to lowercase. Currently on PHP does not have a multibyte (UTF-8) version of ucfirst function. So I decided write my own multibyte mb_ucfirst function.
 * Perhaps the multibyte version of ucfirst function is added later on PHP, so that’s why is better add this function only if it does not already exist.
 */ 
  if (!function_exists('mb_ucfirst')) {
    function mb_ucfirst($str, $encoding = "UTF-8", $lower_str_end = false) {
      $first_letter = mb_strtoupper(mb_substr($str, 0, 1, $encoding), $encoding);
      $str_end = "";
      if ($lower_str_end) {
        $str_end = mb_strtolower(mb_substr($str, 1, mb_strlen($str, $encoding), $encoding), $encoding);
      }
      else {
        $str_end = mb_substr($str, 1, mb_strlen($str, $encoding), $encoding);
      }
      $str = $first_letter . $str_end;
      return $str;
    }
  }

/*
 Some mb_ucfirst function testing and comparison to PHP’s ucfirst function:
  $word = "tEst SOme tExT...";
  echo $word . "\n";
  echo ucfirst($word) . "\n";
  echo mb_ucfirst($word) . "\n";
  echo mb_ucfirst($word, "UTF-8", true) . "\n";
 
  $word = "MORE teSTing...";
  echo $word . "\n";
  echo ucfirst($word) . "\n";
  echo mb_ucfirst($word) . "\n";
  echo mb_ucfirst($word, "UTF-8", true) . "\n";
 
  $word = "YeT MORE teSTing...";
  echo $word . "\n";
  echo ucfirst($word) . "\n";
  echo mb_ucfirst($word) . "\n";
  echo mb_ucfirst($word, "UTF-8", true) . "\n";
 
  $word = "äåÖäÄåûüÜÛ";
  echo $word . "\n";
  echo ucfirst($word) . "\n";
  echo mb_ucfirst($word) . "\n";
  echo mb_ucfirst($word, "UTF-8", true) . "\n";
Tests output looks following:
tEst SOme tExT...
TEst SOme tExT...
TEst SOme tExT...
Test some text...
MORE teSTing...
MORE teSTing...
MORE teSTing...
More testing...
YeT MORE teSTing...
YeT MORE teSTing...
YeT MORE teSTing...
Yet more testing...
äåÖäÄåûüÜÛ
äåÖäÄåûüÜÛ
ÄåÖäÄåûüÜÛ
Äåöääåûüüû
 */
 
?>
