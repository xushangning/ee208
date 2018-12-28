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