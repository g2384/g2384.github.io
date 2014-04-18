<?
/*
This work is designed by g2384, on 2014.Apr.18
Based on: https://github.com/faceair/zhihudaily (@faceair)
*/
?>

<!DOCTYPE html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>知乎日报</title>
<link rel="stylesheet" href="style.css">
</head>

<body>
<div class="main-wrap content-wrap">
	<div class="headline">
<?php
if(empty($_GET["before"])){
  $webcode = file_get_contents("http://news.at.zhihu.com/api/1.2/news/latest");
}else{
  $webcode = file_get_contents("http://news.at.zhihu.com/api/1.2/news/before/" . $_GET["before"]);
}

 $data = json_decode($webcode,true);
 $day = $data['date'];
 $news = $data['news'];
$weekarray = array("日","一","二","三","四","五","六");
$display_date = date('Y.m.d',strtotime($day)) . " 星期".$weekarray[date("w",strtotime($day))];
echo "<div class=headline>$display_date</div>";


for($i=0;$i<count($news);$i++){
echo '<div class="list"><a href="' .$news[$i]['share_url']. '" target="_blank" class="list-link">'.$news[$i]['title'].'</a></div>';
}

?>

</div>
<div class="list">
<?php echo '<a target="_self" href="./index.php?before=' .date('Ymd',strtotime($day)). '" class="list-link"><< 前一天</a>';?>
</div>

</body>
</html>
