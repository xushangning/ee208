<template>
	<div>
		<el-form ref="form" :model="form">        
	        <el-form-item>
	            <el-col :span="10">
	            	<el-input
				   	placeholder="请输入电影名称"
				    v-model="form.name"
				    size="large"
				    clearable>
				    </el-input>
	            </el-col>
	            <el-col :span='1'>
	              <upload></upload>
	            </el-col>
	            <el-col :span="1">
	              		<el-button 
							type="primary" 
							@click="Submit" 
							icon="el-icon-search">
						</el-button>
	            </el-col>
	          </el-form-item>
	    </el-form>
	</div>
</template>

<script>
	import Upload from './upload.vue';
	export default {
		name:"VForm",
		components:{
			'upload':Upload
		},
		data (){
			return {
				form: {
		        	name: ''
		        }
			}
		},
		methods: {
			Submit() {
				console.log("submit!");
			}
		}
	}
</script>
