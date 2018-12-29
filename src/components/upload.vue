<template>
	<div>
		<el-popover
		  width="380"
		  trigger="click">
			<el-upload
				class="upload-demo"
				drag
				action="#"
				:auto-upload="false">
				<i class="el-icon-upload"></i>
				<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
			</el-upload>
		  	<i slot="reference" class="el-icon-picture"></i>
		</el-popover>
	</div>
</template>

<script>
	export default {
		name:"Upload"
	}
</script>
<style type="text/css">
	.el-popover {
		background: rgba(0,0,0,0);
		border: 0px;
		color: hsla(220, 3%, 85%, 1);
	}
	.el-upload-dragger {
		background: rgba(100,100,100,0.7);
		border: 0px;
	}
	.el-upload-dragger .el-upload__text {
		color: hsla(220, 3%, 85%, 1);
	}
</style>