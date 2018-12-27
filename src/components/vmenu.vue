<template>
	<div>
		<el-menu 
	        :default-active="activeIndex"
	        class="el-menu-demo"
	        mode="horizontal"
	        @select="handleSelect">
	        <el-menu-item index="1"><a href="/">首页</a></el-menu-item>
	        <el-menu-item index="2"><a href="/#/hello">电影大全</a></el-menu-item>    
	    </el-menu>
	</div>
</template>

<script>
	export default {
		name:"VMenu",
		data() {
			return {
				activeIndex:'1'
			};
		},
		methods: {
			handleSelect(key,keyPath) {
				console.log(key,keyPath);
			}
		}
	}
</script>
