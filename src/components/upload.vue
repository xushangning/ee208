<template>
	<div>
		<el-popover
		  width="380"
		  trigger="click">
			<el-upload
				class="upload-demo"
				drag
				action="#"
				:auto-upload="false"
				:on-change="change">
				<i class="el-icon-upload"></i>
				<div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
			</el-upload>
			<el-switch
				v-model="choice"
				active-color="#dcdfe6"
				active-text="海报"
				inactive-text="宣传片截图">
			</el-switch>
		  	<i slot="reference" class="el-icon-picture"></i>
		</el-popover>
	</div>
</template>

<script>
	import axios from 'axios';
	export default {
		name:"Upload",
		data (){
			return{
				choice:true
			} 
		},
		methods: {
			change(file) {
				console.log(file)
				if(this.choice)
				{

					const path = 'http://localhost:5000/result1';
				}
				else
				{
					const path = 'http://localhost:5000/result2';
				}
				let data = new FormData();
				data.append('file',file)
				let config = {
            		headers:{'Content-Type':'multipart/form-data'}
          		};
				axios.post(path,data,config)
					.then((res) => {
		        	 data= res.data.name;
		        	 window.location.href='result?name='+ data;
		        	})
		        .catch((error) => {
		          // eslint-disable-next-line
		        	console.error(error);
		     		});
			}
		}
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