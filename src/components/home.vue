<template>
	<div id="whole" :style="bg">
	    <el-container>
	      <el-header height="61px">
	        <el-col :span="24">
	        	<vmenu :activeIndex="index" :items="items"></vmenu>
	        </el-col>
	        <el-col :span="1" id="info1"><info1></info1></el-col>
	        <el-col :span="1" id="time1"><time1></time1></el-col>
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
				const path = 'http://localhost:5000/';
				var data;
		    	this.$http.get(path)
		        .then((res) => {
		        	 data= res.data;
		        })
		        .catch((error) => {
		          // eslint-disable-next-line
		        	console.error(error);
		     	});
			return {
				index: "/",
				items: [
					{id: 1,index: "/",name: "首页"},
				],
				movies: data,
				bg: {
					width: '100%',
    				height: '100%',
					backgroundImage: "url("+require("../assets/bg.gif")+")",
					backgroundSize: '100% 100%',
					overflow: 'hidden'
				},
				tp: {
					typ: 'info',
					imgurl: require("../assets/button.png")
				}
			}
		}
	}
</script>

<style>
	html,body {
    height: 100%;
    margin: 0;
	}
	a{text-decoration : none}
	.whole {
	    width:100%;
	    height: 100%;
	}
	#app {
		height:100%;
	}
	.el-header, .el-footer {
	    background-color: rgba(0,0,0,0);
	    color: #333;
	    text-align: center;
	    line-height: 60px;
	}
	.el-main {
	    color: #333;
	}
	  
	body > .el-container {
	    margin-bottom: 40px;
	}
	.el-container.is-vertical {
	    width: 90%;
	    margin-left: auto;
	    margin-right: auto;
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
		top: 0px;
		left: 90%;
	}
	#info1 {
		position: absolute;
		top: 0px;
		left: 87%;
	}
</style>