<?php
	/*
	 * PHP has large number of predefined constants. This HOWTO will present the seven most important, most practical and most useful PHP Magic Constants.
__FILE__ – The full path and filename of the file. 
__DIR__ – The directory of the file. 
__FUNCTION__ – The function name. 
__CLASS__ – The class name. 
__METHOD__ – The class method name. 
__LINE__ – The current line number of the file. 
__NAMESPACE__ – The name of the current namespace 
This is example PHP script with comments, which demonstrate howto use all previously mentioned PHP Magic Constants.
	 */ 
        // Set namespace (works only with PHP 5.3)
        namespace TestProject;
 
        // This prints file full path and name
        echo "This file full path and file name is '" . __FILE__ . "'.\n";
 
        // This prints file full path, without file name
        echo "This file full path is '" . __DIR__ . "'.\n";
 
        // This prints current line number on file
        echo "This is line number " . __LINE__ . ".\n";
 
        // Really simple basic test function
        function test_function_magic_constant() {
                echo "This is from '" . __FUNCTION__ . "' function.\n";
        }
 
        // Prints function and used namespace
        test_function_magic_constant();
 
        // Really simple class for testing magic constants
        class TestMagicConstants {
                // Prints class name
                public function printClassName() {
                        echo "This is " . __CLASS__ . " class.\n";
                }
 
                // Prints class and method name
                public function printMethodName() {
                        echo "This is " . __METHOD__ . " method.\n";
                }
 
                // Prints function name
                public function printFunction() {
                        echo "This is function '" . __FUNCTION__ . "' inside class.\n";
                }
 
                // Prints namespace name (works only with PHP 5.3)
                public function printNamespace() {
                        echo "Namespace name is '" . __NAMESPACE__ . "'.\n";
                }
        }
 
        // Create new TestMagicConstants class
        $test_magic_constants = new TestMagicConstants;
 
        // This prints class name and used namespace
        $test_magic_constants->printClassName();
 
        // This prints method name and used namespace
        $test_magic_constants->printMethodName();
 
        // This prints function name inside class and used namespace
        // same as method name, but without class
        $test_magic_constants->printFunction();
 
        // This prints namespace name (works only with PHP 5.3)
        $test_magic_constants->printNamespace();
 
 /*Output
This file full path and file name is '/tmp/magic_constants/magic.php'.
This file full path is '/tmp/magic_constants'.
This is line number 13.
This is from 'TestProject\test_function_magic_constant' function.
This is TestProject\TestMagicConstants class.
This is TestProject\TestMagicConstants::printMethodName method.
This is function 'printFunction' inside class.
Namespace name is 'TestProject'.
  */
?>
