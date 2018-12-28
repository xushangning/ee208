<template>
	<div>
		<div>
			<el-popover
			    trigger="hover">
			    <p  id="timeShow" class="time1"></p>
			    <i slot="reference" class="el-icon-time" ></i>
			</el-popover>
		</div>
	</div>
</template>
<script>
	var t = null;
	t = setTimeout(time,1000);//开始执行
	function time()
	{
		clearTimeout(t);//清除定时器
		var dt = new Date();
		var y=dt.getYear()+1900;
		var mm=dt.getMonth()+1;
		var d=dt.getDate();
		var day=dt.getDay();
	   	var h=dt.getHours();
	   	var m=dt.getMinutes();
	 	var s=dt.getSeconds();
		if(h<10){h="0"+h;}
		if(m<10){m="0"+m;}
		if(s<10){s="0"+s;}
	   	document.getElementById("timeShow").innerHTML =  "当前时间："+y+"-"+mm+"-"+d+" "+h+":"+m+":"+s+"";
			   	t = setTimeout(time,1000); //设定定时器，循环执行           
	}
	export default {
		name:"Time1"
	}
</script>
<style>
.time1{
    width:100%; 
    text-align:center;
    color: #333;
}
.el-icon-time{
	color:#fff;
}
</style>