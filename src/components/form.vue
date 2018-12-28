<template>
	<div>
		<el-form ref="form" :model="form">        
	        <el-form-item>
	            <el-col :span="23">
	            	<el-input
				   	placeholder="请输入电影名称"
				    v-model="form.name"
				    size="large"
				    clearable>
				    <upload id="up" slot="suffix"></upload>
				    </el-input>
	            </el-col>
<!-- 	            <el-col :span='1'>
	              <upload></upload>
	            </el-col> -->
	            <el-col :span="1">
	              		<el-button 
							:type="tp" 
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
		props: {
			tp: {
				type: String,
				required: true
			}
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
<style>
	#up{
		margin-right: 10px;
		cursor: pointer;
	}
	.el-input__inner {
		background-color: rgba(100,100,100,0.5);
	}
</style>