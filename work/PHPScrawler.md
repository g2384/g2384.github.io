###使用file_get_contents [源码](https://gist.github.com/g2384/10582934)
<pre>
  $url = “http://www.xxx.com/”; 
  $contents = file_get_contents($url); // $contents现在保存了网页源码
</pre>
###过滤内容(方法一)
<pre>
// 使用正则表达式，获取指定内容
eregi("<head>(.*)</ head>", $contents, $head); // 所有匹配项保存在$head，数组

// 使用strpos判断字符是否包含想要的内容
if(strpos($str, “广告”)==false){ // 若不包含“广告”
 	$result .= $str; // 追加到$result
}
if(strpos($contents, “想要的内容”)){ // 若包含“想要的内容”
	// do something
}
</pre>
###过滤内容(方法二)
<pre>
// 使用 loadHTML，解析网页内容，然后使用getElementsByTagName过滤
$DOM = new DOMDocument();
$DOM->loadHTML($str);
foreach ($DOM->getElementsByTagName('tr') as $node) { // 例如，只想要<tr>的标签
$array[] = $DOM->saveHTML($node); // $array 包含所有的<tr>标签
}
</pre>
###调试方法
<pre>
echo $contents; // 显示成网页形式
print_r($contents); // 以数组形式输出
</pre>
###中文乱码
<pre>
//如果出现中文乱码使用下面代码
$getcontent = iconv("gb2312", "utf-8" ,file_get_contents($url));  
</pre>
###输出保存
<pre>
$f = fopen("result.txt", 'a'); // 追加到文本
fwrite($f, $result);
fclose($f);
</pre>
###定时获取
<pre>
sleep(10); // 等待10秒

<meta http-equiv="refresh" content="10"> // 写在文件开头，网页每10秒自动刷新
<?
$i   = file_get_contents("count"); // 使用count文本文件，记录执行到第几个
// do something
file_put_contents("count", ++$i); // 保存count
?>
</pre>
