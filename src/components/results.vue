<template>
	<div id="whole" :style="bg">
	    <el-container>
	      <el-header height='61px'>
	        <el-row>
	          <el-col :span="21" id="vmenu-header">
	          	<vmenu :activeIndex='index' :items='items'></vmenu>
	          </el-col>
	          <el-col :span="6" id="search">
	          	<vform :tp='tp'></vform>
	          </el-col>
	          <el-col :span='1' id='info1'><info1></info1></el-col>
	          <el-col :span="1" id="time1"><time1></time1></el-col>
	        </el-row>
	      </el-header>
	      <el-main>
	      	<movie-card v-for="result in results"
	      				:movie="result"
	      				:key="result.id"></movie-card>
	      </el-main>
	    </el-container>
	  </div>
</template>

<script>
	import VMenu from './vmenu.vue';
	import Time1 from './time1.vue';
	import VForm from './form.vue'; 
	import Carousel from './carousel.vue';
	import Info1 from './info1.vue';
	import MovieCard from './moviecard.vue';
	export default {
		components:{
			'vmenu': VMenu,
			'time1': Time1,
			'vform': VForm,
			'carousel': Carousel,
			'info1': Info1,
			'movie-card': MovieCard,
		},
		data() {
			var url = decodeURI(location.search);
			var req = url.split('=')[1];
			const path = 'http://localhost:5000/results?name=' + req;
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
				index: '/results',
				items: [
					{id: 1,index: '/',name: '首页'},
					{id: 2,index: '/results',name: '搜索结果'}
				],
				bg: {
					width: '100%',
					backgroundImage: "url("+require("../assets/staticbg.png")+")",
					backgroundSize: '100% 100%',
					backgroundAttachment: 'fixed',
				},
				results: data,
				tp: {
					typ: 'info',
					imgurl: require("../assets/button.png")
				}
			}
		}
	}
</script>

<style> 
	::-webkit-scrollbar {  /* 滚动条整体部分 */
	    width:10px;
	    margin-right:2px
	}
	::-webkit-scrollbar-button { /* 滚动条两端的按钮 */
	    width:10px;
	    background-color: #202020;
	}
	::-webkit-scrollbar:horizontal {
	    height:10px;
	    margin-bottom:2px
	}
	::-webkit-scrollbar-track {  /* 外层轨道 */
	    background-color: #202020;
	}
	::-webkit-scrollbar-track-piece {  /*内层轨道，滚动条中间部分 */
	    background-color: #202020;
	    border-radius: 5px;
	}
	::-webkit-scrollbar-thumb {  /* 滑块 */
	    width:10px;
	    border-radius: 5px;
	    background: #606266;
	}
	::-webkit-scrollbar-corner { /* 边角 */
	    width: 10px;
	}
	::-webkit-scrollbar-thumb:hover { /* 鼠标移入滑块 */
	    background: #707070;
	}
	.demo {
	    width: 400px;
	    height: 200px;
	    overflow: auto;
	}
	html,body {
    margin: 0;
    height:100%;
	}
	a{text-decoration : none}
	#app {
		height:100%;
	}
	.whole {
	    width:100%;
	    height: 100%;
	}
	.el-header, .el-footer {
	    background-color: rgba(0,0,0,0);
	    line-height: 60px;
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
	#vmenu-header {
		position:fixed;
		top: 0px;
	}
	#time1 {
		position:fixed;
		top: 0px;
		left: 90%;
	}
	#info1 {
		position: fixed;
		top: 0px;
		left: 86.5%;
	}
	#search {
		position:fixed;
		top:10px;
		left: 57%;
	}
</style>