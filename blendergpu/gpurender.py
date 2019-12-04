import bpy
bpy.context.user_preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
bpy.context.user_preferences.addons['cycles'].preferences.compute_device = 'CUDA_MULTI_2'
