<template>
	<div id="whole" :style="bg">
	    <el-container>
	      <el-header height="61px">
	        <el-row>
	          <el-col :span="24">
	          	<vmenu :activeIndex="index" :items="items"></vmenu>
	          </el-col>
	          <el-col :span="1" :offset="22" id="info1"><info1></info1></el-col>
	          <el-col :span="1" :offset="23" id="time1"><time1></time1></el-col>
	        </el-row>
	      </el-header>
	      <el-main>
	      	<el-row>
	      		<el-col :span="11">
	          		<vform :tp='tp'></vform>
	          	</el-col>
	          </el-row>
	        <el-row>
	        	<div class="grid-content">
	        	</div>
	        </el-row>
	        <el-row>
	        	<el-col :span="20" :offset="2">
	        		<carousel :movies="movies"></carousel>
	        	</el-col>
	        </el-row>
	      </el-main>
	    </el-container>
	  </div>
</template>

<script>
	import VMenu from "./vmenu.vue";
	import Time1 from "./time1.vue";
	import VForm from "./form.vue"; 
	import Carousel from "./carousel.vue";
	import Info1 from "./info1.vue";
	export default {
		components:{
			"vmenu": VMenu,
			"time1": Time1,
			"vform": VForm,
			"carousel": Carousel,
			"info1": Info1,
		},
		data() {
			return {
				index: "/",
				items: [
					{id: 1,index: "/",name: "首页"},
					{id: 2,index: "/hello",name: "电影大全"}
				],
				movies: [
					{id: 1,name:"蜘蛛侠3",img:"../../static/蜘蛛侠3.jpg"},
					{id: 2,name:"钢铁侠3",img:"../../static/钢铁侠3.jpg"},
					{id: 3,name:"X战警3：背水一战",img:"../../static/X战警3：背水一战.jpg"},
					{id: 4,name:"海王",img:"../../static/海王.jpg"},
					{id: 5,name:"蝙蝠侠大战超人：正义黎明",img:"../../static/蝙蝠侠大战超人：正义黎明.jpg"},
				],
				bg: {
					width: '100%',
    				height: '100%',
					backgroundImage: "url("+require("../assets/bg.gif")+")",
					backgroundSize: '100% 100%',
					overflow: 'hidden'
				},
				tp: 'info'
			}
		}
	}
</script>

<style>
	html,body {
    height: 100%;
    overflow: hidden;
    margin: 0;
	}
	a{text-decoration : none}
	.whole {
	    width:100%;
	    height: 100%;
	    bottom:0pX;
	    position: absolute;
	}
	.el-header, .el-footer {
	    background-color: rgba(0,0,0,0);
	    color: #333;
	    text-align: center;
	    line-height: 60px;
	}
	  
	.el-aside {
	    background-color: #D3DCE6;
	    color: #333;
	    text-align: center;
	    line-height: 200px;
	}

	.el-main {
	    color: #333;
	    text-align: center;
	    line-height: 160px;
	}
	  
	body > .el-container {
	    margin-bottom: 40px;
	}
	  
	.el-container:nth-child(5) .el-aside,
	.el-container:nth-child(6) .el-aside {
	    line-height: 260px;
	}
	  
	.el-container:nth-child(7) .el-aside {
	    line-height: 320px;
	}

	/*layout*/
	.el-row {
	    margin-bottom: 20px;
	    &:last-child {
	      margin-bottom: 0;
	    }
	}
	.grid-content {
		min-height: 40px;
	}
	#time1 {
		position:absolute;
		top:0px;
	}
	#info1 {
		position: absolute;
		top: 0px;
	}
</style>