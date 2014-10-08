/*global println*/

// --------
// Hello.js
// --------

// https://developer.mozilla.org/en-US/docs/Web/JavaScript
// http://www.jslint.com

println("Nothing to be done.");

/*
Developed in 1995 by Brendan Eich, who cofounded Mozilla and recently resigned as CEO.
Javascript is procedural, object-oriented, dynamically typed, and garbage collected.



% jrunscript -help
Usage: jrunscript [options] [arguments...]

where [options] include:
  -classpath <path>    Specify where to find user class files
  -cp <path>           Specify where to find user class files
  -D<name>=<value>     Set a system property
  -J<flag>             Pass <flag> directly to the runtime system
  -l <language>        Use specified scripting language
  -e <script>          Evaluate given script
  -encoding <encoding> Specify character encoding used by script files
  -f <script file>     Evaluate given script file
  -f -                 Interactive mode, read script from standard input
                       If this is used, this should be the last -f option
  -help                Print this usage message and exit
  -?                   Print this usage message and exit
  -q                   List all scripting engines available and exit

If [arguments..] are present and if no -e or -f option is used, then first
argument is script file and the rest of the arguments, if any, are passed
as script arguments. If [arguments..] and -e or -f option is used, then all
[arguments..] are passed as script arguments. If [arguments..], -e, -f are
missing, then interactive mode is used.



% jrunscript -f Hello.js
Nothing to be done.
*/
