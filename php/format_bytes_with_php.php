 /*
Format bytes with PHP – B, KB, MB, GB, TB, PB, EB, ZB, YB converter

Simple PHP function that formats the bytes to the desired form. Possible unit options are:
Byte (B) 
Kilobyte (KB) 
Megabyte (MB) 
Gigabyte (GB)  -->Terabyte (TB) 
Petabyte (PB) 
Exabyte (EB) 
Zettabyte (ZB) 
Yottabyte (YB) 
Function takes three parameter: (bytes mandatory, unit optional, decimals optional)
PHP byteFormat function for formatting bytes
*/
<?php
 
  function byteFormat($bytes, $unit = "", $decimals = 2) {
        $units = array('B' => 0, 'KB' => 1, 'MB' => 2, 'GB' => 3, 'TB' => 4, 
                        'PB' => 5, 'EB' => 6, 'ZB' => 7, 'YB' => 8);
 
        $value = 0;
        if ($bytes > 0) {
                // Generate automatic prefix by bytes 
                // If wrong prefix given
                if (!array_key_exists($unit, $units)) {
                        $pow = floor(log($bytes)/log(1024));
                        $unit = array_search($pow, $units);
                }
 
                // Calculate byte value by prefix
                $value = ($bytes/pow(1024,floor($units[$unit])));
        }
 
        // If decimals is not numeric or decimals is less than 0 
        // then set default value
        if (!is_numeric($decimals) || $decimals < 0) {
                $decimals = 2;
        }
 
        // Format output
        return sprintf('%.' . $decimals . 'f '.$unit, $value);
  }
 
?>
/*
Example usage
echo byteFormat(4096, "B") ."\n";
echo byteFormat(8, "B", 2) . "\n";
echo byteFormat(1, "KB", 5) . "\n";
echo byteFormat(1073741824, "B", 0) . "\n";
echo byteFormat(1073741824, "KB", 0) . "\n";
echo byteFormat(1073741824, "MB") . "\n";
echo byteFormat(1073741824) . "\n";
echo byteFormat(1073741824, "TB", 10) . "\n";
echo byteFormat(1099511627776, "PB", 6) . "\n";
Prints
4096.00 B
8.00 B
0.00098 KB
1073741824 B
1048576 KB
1024.00 MB
1.00 GB
0.0009765625 TB
0.000977 PB
*/