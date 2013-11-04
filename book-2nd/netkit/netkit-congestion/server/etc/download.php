
<?php
/*
 * 
 *
 */ 

  $file = fopen("10Mo.zero","r");
  $length = filesize($file);


  header('HTTP/1.1 200 OK');
  header('Status: 200 OK');
  header("Cache-Control: no-store, no-cache, must-revalidate");
  header("Cache-Control: post-check=0, pre-check=0", false);
  header("Pragma: no-cache");
  header("Expires: ".gmdate("D, d M Y H:i:s", mktime(date("H")+2,
  date("i"), date("s"), date("m"), date("d"), date("Y")))." GMT");

  header("Last-Modified: ".gmdate("D, d M Y H:i:s")." GMT");
  header('Accept-Ranges: bytes');
  header('Content-Transfer-Encoding: Binary');
 // header('Content-Type: application/force-download');
  header('Content-Type: application/octet-stream');
//header('Content-Disposition: attachment; filename="'.$filename.'"');
////header("Content-Disposition: inline; filename=$name");
  header('Content-Length: '.$length);
  


  while(!feof($file)){
    print(fread($file,150000);
    sleep(1);
  } 
?>
