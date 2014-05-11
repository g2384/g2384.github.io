$max = 100; // max number of news to display
$file = 'hnews.txt'; // Must exist before using. a file to store all data
$items = array_reverse(explode("\n", file_get_contents($file)));
$i = 0;

foreach($items as $a)
	{
	$item[$i] = explode("<%>", $a);
	//$item[$i][0] => rank, $item[$i][1] => title, $item[$i][2] => commments
	$i++;
	}

$contents = file_get_contents("https://news.ycombinator.com/"); // get the webpage contents
$contents = mb_convert_encoding($contents, 'HTML-ENTITIES', 'UTF-8');
$DOM = new DOMDocument();
$DOM->loadHTML($contents); // parse the contents

foreach($DOM->getElementsByTagName('tr') as $node)
	{ // get <tr> elements
	$array[] = $DOM->saveHTML($node);
	}

foreach($array as $a)
	{
	$b = strpos($a, '<td class="title"'); // find all the news
	if (strlen($a) < 1500)
		{
		$str = trim(preg_replace('/\s+/', ' ', $a));
		$str = str_replace('</td> </tr>', '', $str);
		if ($b)
			{
			$str = substr($str, $b);
			$str = str_replace('<td class="title">', '', $str);
			$str = str_replace(' rel="nofollow"', '', $str);
			$str = str_replace('item?id=', 'https://news.ycombinator.com/item?id=', $str);
			$arr[] = $str;
			}
		  else
		if (strpos($str, 'class="subtext"'))
			{
			$str = substr($str, strpos($str, '<a href="item?id'));
			$str = str_replace('<a href="item?id', '<a class=comm href="https://news.ycombinator.com/item?id=', $str);
			$comm[] = $str;
			}
		}
	}

$temp = count($arr) - 1;
$append = $i;

for ($k = 0; $k < $temp; $k++)
	{
	$matched = 0;
	for ($j = 0; $j < $i; $j++)
		{ //[0] => rank, [1] => title, [2] => commments
		if ($item[$j][1] == $arr[$k])
			{
			$item[$j][2] = $comm[$k]; // update the comment number
			$matched = 1;
			if ($item[$j][0] > $k)
				{
				$item[$j][0] = $k;
				}
			}
		}

	if ($matched == 0) // if not matched, append this item
		{
		$item[$append] = array(
			$k,
			$arr[$k],
			$comm[$k]
		);
		$append++;
		}
	}

for ($i = 0; $i < $append; $i++)
	{
	$items[$i] = implode("<%>", $item[$i]);
	}

$items = array_slice(array_reverse($items) , 0, $max); //reverse and slice the array, now, the newest is at the top
file_put_contents($file, implode("\n", $items));

// -------------------------------------
// generate the index.html static webpage

$len = count($items);
$list = '';

for ($i = 0; $i < $len; $i++)
	{
	$item = explode('<%>', $items[$i]);
	$rank = $item[0] < 9 ? ' class=rank' : '';
	$comment = strpos($item[1], 'item?id=') ? '' : $item[2]; // some news don't have discussion page
	$list = $list . "<div class=list><span$rank>" . ($item[0] + 1) . '</span>' . $item[1] . " $comment</div>\n";
	}

$webpage = '<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"><head><style>body {font-family:Arial,Helvetica,Sans-serif;font-size:16px;margin:0 0;color:#999;}.wrap {max-width:960px;margin:0 auto;}.list {width:100%;margin:0;padding:0;}.comhead,.list .comm {font-size:14px;color:#999;}.rank {background-color:#ddd;padding-left:9px;}a {display:inline-block;position:relative;text-decoration:none;line-height:200%;font-size:18px;color:#555;padding-left:5px;}a:visited {color:#999;}.list:hover,.list a:hover,.list .comm:hover {color:#000;}@media (max-width: 855px) {   a {display:inline;line-height:100%;}.list{margin-bottom:10px;}}</style><script>function load(){var s=document.cookie;var a=document.getElementsByClassName("list");var l=a.length;for(i=0;i<l;i++){if(a[i].innerHTML.match(s)&&s){a[i].innerHTML="<hr>"+a[i].innerHTML;i=l+1}}if(i==l+2){str=a[0].innerHTML.replace(/<[ a-z"=]+>[0-9]+<\/span>/g,"");str=str.substring(0,50);document.cookie=str}}</script></head><body onload="load()"><div class=wrap>Last update: ' . date('Y M d (D), H:i:s', time()) . " <a href=hackernews.php>update now!</a><br /><br />$list</div></body>";
$fp = fopen('index.html', 'w');
fwrite($fp, $webpage);
fclose($fp);
