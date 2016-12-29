/**
 * Strings are immutable
 * */

/**
 * Concatenation (use StringBuilder instead for more efficiency)
 */
String a = "foo";
a = a + "man";

/**
 * Formatting. 
 * Use String.format(value,variable) as C'style
 */
double x = 1.344;
String t = String.format("%.2f",x) //2 decimal points
