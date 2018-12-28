<template>
	<div id="whole">
	    <el-container>
	      <el-header height='61px'>
	        <el-row>
	          <el-col :span="24">
	          	<vmenu :activeIndex='index' :items='items'></vmenu>
	          </el-col>
	          <el-col :span="6" :offset="15" id="search">
	          	<vform :tp='tp'></vform>
	          </el-col>
	          <el-col :span='1' :offset='22' id='info1'><info1></info1></el-col>
	          <el-col :span="1" :offset="23" id="time1"><time1></time1></el-col>
	        </el-row>
	      </el-header>
	      <el-main>
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
	export default {
		components:{
			'vmenu': VMenu,
			'time1': Time1,
			'vform': VForm,
			'carousel': Carousel,
			'info1': Info1,
		},
		data() {
			return {
				index: '/results',
				items: [
					{id: 1,index: '/',name: '首页'},
					{id: 2,index: '/hello',name: '电影大全'},
					{id: 3,index: '/results',name: '搜索结果'}
				],
				tp: 'primary'
			}
		}
	}
</script>

<style>
	a{text-decoration : none}
	.whole {
	    width:100%;
	    height: 100%;
	    bottom:0pX;
	    position: absolute;
	}
	.el-header, .el-footer {
	    background-color: #ffffff;
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
	#search {
		position:absolute;
		top:10px;
	}
	#logo {
		position:absolute;
		top:6px;
		left: 0px;
		height:50px;
		width:50px;
	}
</style>