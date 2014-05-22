<?
$max = 100; // max number of news to display
$file = 'hnews.txt'; // Must exist before using. a file to save all data
$items = array_reverse(explode("\n", file_get_contents($file)));
$i = 0;

foreach($items as $a)
	{
	$item[$i] = explode("<%>", $a);
	//$item[$i][0] => rank, $item[$i][1] => title, $item[$i][2] => comment number, $item[$i][3] => id_number
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
		$str = trim(preg_replace('/\s+/', ' ', $a)); // remove \r\n
		$str = str_replace('</td> </tr>', '', $str);
		if ($b)
			{ // titles
			$str = substr($str, $b);
			$original = array('<td class="title">', ' rel="nofollow"', 'item?id=');
			$new   = array('', '', 'https://news.ycombinator.com/item?id=');
			$str = str_replace($original, $new, $str);
			$arr[] = $str;
			}
		  else
		if (strpos($str, 'class="subtext"'))
			{ // comments
			preg_match_all('/[0-9]+( comments)?/', substr($str, strpos($str, '<a href="item')), $match);
			$id[]=$match[0][0];
			$comm[] = $match[0][1]?$match[0][1]:'discuss';
			}
		}
	}
$l = count($arr) - 1;
$append = $i;

for ($k = 0; $k < $l; $k++)
	{
	for ($j = 0; $j < $i; $j++)
		{ //[0] => rank, [1] => title, [2] => comment number, $item[$i][3] => id_number
		if ($item[$j][3] == $id[$k])
			{
			$item[$j][2] = $comm[$k]; // update "comment number"
			$item[$j][1] = $arr[$k]; // update "title"
			if ($item[$j][0] > $k)
				{
				$item[$j][0] = $k; // update "rank"
				}
			$j = $i; // break the for loop
			}
		}
//if matched, $j = $i+1
	if ($j == $i) // if not matched, append this item
		{
		$item[$append] = array(
			$k,
			$arr[$k],
			$comm[$k],
			$id[$k]
		);
		$append++;
		}
	}

for ($i = 0; $i < $append; $i++)
	{
	$items[$i] = implode("<%>", $item[$i]);
	}

$items = array_slice(array_reverse($items) , 0, $max); //reverse and slice the array. Now, the newest is at the top
file_put_contents($file, implode("\n", $items));

// -------------------------------------
// generate the index.html static webpage

$len = count($items);
$list = '';

for ($i = 0; $i < $len; $i++)
	{
	$item = explode('<%>', $items[$i]);
	$rank = $item[0] < 9 ? ' class=rank' : '';
	$comment = strpos($item[1], 'item?id=') ? '' : '<a class=comm href="https://news.ycombinator.com/item?id='.$item[3].'">'.$item[2].'</a>'; // some news don't have discussion page
	$list = $list . "<div class=list><span$rank>" . ($item[0] + 1) . '</span>' . $item[1] . " $comment</div>\n";
	}

$webpage = '<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"><head><style>body{font-family:Arial,Helvetica,Sans-serif;font-size:16px;color:#999;margin:0}.wrap{max-width:960px;margin:0 auto}.list{width:100%;margin:0;padding:0}.list .comm{font-size:14px;color:#999}.rank{background-color:#ddd;padding-left:9px}a{display:inline-block;position:relative;text-decoration:none;line-height:200%;font-size:18px;color:#555;padding-left:5px}a:visited{color:#999}.list:hover,.list a:hover,.list .comm:hover{color:#000}@media max-width 855px {a{display:inline;line-height:100%}.list{margin-bottom:10px}}</style><script>function load(){var e=document.cookie;var t=document.getElementsByClassName("list");var n=t.length;var r=t[0].innerHTML.replace(/<[ a-z"=]+>[0-9]+<\/span>/g,"");r=r.substring(0,50);for(i=0;i<n;i++){if(t[i].innerHTML.match(e)&&e){t[i].innerHTML="<hr>"+t[i].innerHTML;i=n+1}}document.cookie=r}</script></head><body onload="load()"><div class=wrap>Last update: ' . date('Y M d (D), H:i:s', time()) . " <a href=hackernews.php>update now!</a><br /><br />$list</div></body>";
$fp = fopen('index.html', 'w');
fwrite($fp, $webpage);
fclose($fp);
?>
