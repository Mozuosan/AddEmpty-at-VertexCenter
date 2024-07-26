import bpy

bl_info = {
    "name": "AddEmpty at VertexCenter",
    "author": "mozuo",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Object > AddEmpty at VertexCenter",
    "description": "選択されたふたつの頂点の中央の座標を記憶しEmptyを配置します。Emptyの配置はオブジェクトモードで行います",
    "category": "Object",
}

class VertexCenterEmptyOperator(bpy.types.Operator):
    bl_idname = "object.vertex_center_empty"
    bl_label = "AddEmpty at VertexCenter"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the selected vertices
        selected_verts = [v for v in bpy.context.active_object.data.vertices if v.select]

        if len(selected_verts) == 2:
            # Calculate the center point in global coordinates
            center = (selected_verts[0].co + selected_verts[1].co) / 2
            center_global = bpy.context.active_object.matrix_world @ center

            # Create an Empty object
            bpy.ops.object.empty_add(location=center_global)

            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "ふたつの頂点を選択した状態でオブジェクトモードに戻ってください")
            return {'CANCELLED'}

def menu_func(self, context):
    self.layout.operator(VertexCenterEmptyOperator.bl_idname)

def register():
    bpy.utils.register_class(VertexCenterEmptyOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(VertexCenterEmptyOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()