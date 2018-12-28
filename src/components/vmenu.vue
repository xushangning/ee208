<template>
	<div>
		<el-menu 
	        :default-active="activeIndex"
	        class="el-menu-demo"
	        mode="horizontal"
	        active-text-color="#fff"
	        background-color=rgba(255,255,255,0)
	        @select="handleSelect"
	        :router=true>
	        <el-menu-item index=""><span class='logo-container'><a href='/'><img :src="imgurl" id="logo"></a></span></el-menu-item>
	        <el-menu-item v-for='item in items'
	        			  :key='item.id'
	        			  :index='item.index'>
	        			{{item.name}}
	        </el-menu-item>
<!-- 	        <el-menu-item index="/">首页</el-menu-item>
	        <el-menu-item index="hello">电影大全</el-menu-item>     -->
	    </el-menu>
	</div>
</template>

<script>
	export default {
		name:"VMenu",
		props:{
			activeIndex:{
				type: String,
				required: true
			},
			items:{
				type: Array,
				required: true
			}
		},
		data() {
			return {
				imgurl:require('../assets/logo.png'),
			};
		},
		methods: {
			handleSelect(key,keyPath) {
				console.log(key,keyPath);
			}
		}
	}
</script>
<style>
	#logo {
		position:absolute;
		top:6px;
		left: 0px;
		height:50px;
		width:50px;
	}
	.logo-container {
		margin:10px;
	}
</style>