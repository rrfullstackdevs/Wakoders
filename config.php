<?php 
	include 'Uri.php';
	include 'SphinxConfiguration.py';

	$url = 'teste' #Uri::base();
	$host = Uri::host();

	echo shell_exec("C:\Users\Victor\Anaconda3\share\jupyter\kernels\python3 D:\Hackton\Sphinx\SphinxConfiguration.py".$url);

	echo '<script language="javascript">';
	echo 'alert("message successfully sent")';
	echo '</script>';

	

?>