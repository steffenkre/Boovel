bl_info = {
    "name" : "Boovel 0.1a",
    "category": "Mesh",
    "author" : "Steffen Kressel"
}
import bpy

def add_bevel_modifier():
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].width = 0.03
    bpy.context.object.modifiers["Bevel"].segments = 6
    bpy.context.object.modifiers["Bevel"].limit_method = 'WEIGHT'
    bpy.context.object.modifiers["Bevel"].use_clamp_overlap = False

def resharp():
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.edges_select_sharp()
    bpy.ops.transform.edge_bevelweight(value=1)
    bpy.ops.object.editmode_toggle()

def fastbool(booltype = "INTERSECT"):
    targetobjectname = bpy.context.active_object.name
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.active_object.modifiers['Boolean'].operation = booltype
    #bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Plane"]
    objectnames = []
    for i in bpy.context.selected_objects:
        objectnames.append(i.name)
        
    objectnames.remove(targetobjectname)
    bpy.context.active_object.modifiers['Boolean'].object = bpy.data.objects[objectnames[0]]
    bpy.data.objects[objectnames[0]].draw_type = 'WIRE'
    bpy.ops.object.modifier_apply(modifier="Boolean")
    resharp()

class Unionbool(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.unionbool"
    bl_label = "Union"  
 
    def execute(self, context):
        #code here
        fastbool(booltype = 'UNION')
        return{'FINISHED'}
    
class Intersectbool(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.intersectbool"
    bl_label = "Intersect"  
 
    def execute(self, context):
        #code here
        fastbool()
        return{'FINISHED'}

class Differencebool(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.differencebool"
    bl_label = "Difference"  
 
    def execute(self, context):
        #code here
        fastbool(booltype = 'DIFFERENCE')
        return{'FINISHED'}
class BevelInit(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.bevelinit"
    bl_label = "Init Bevel"
 
    def execute(self, context):
        add_bevel_modifier()
        resharp()
        return{'FINISHED'} 
class ZeroWeight(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.zeroweight"
    bl_label = "-1"
 
    def execute(self, context):
        bpy.ops.transform.edge_bevelweight(value=-1)
        return{'FINISHED'}
class MaxWeight(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.maxweight"
    bl_label = "+1"
 
    def execute(self, context):
        bpy.ops.transform.edge_bevelweight(value=1)
        return{'FINISHED'}
class Symmetrize(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.symmetrize"
    bl_label = "Symmetrize"
 
    def execute(self, context):
        #code here
        bpy.ops.mesh.symmetrize()
        return{'FINISHED'}

class SelectSharp(bpy.types.Operator):
    #dont forget to register this class;)
    bl_idname = "boovel.selectsharp"
    bl_label = "Select Sharp Edges"
 
    def execute(self, context):
        #code here
        bpy.ops.mesh.edges_select_sharp()
        return{'FINISHED'}

class Boovel(bpy.types.Panel):
    bl_label = "Boovel 0.01"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    #bl_context = "object"
 
    def draw(self, context):
        layout =  self.layout
        row = layout.row()#use this also for a new line
        row.label("Bools:")
        row = layout.row()
        row.operator("boovel.unionbool")#add a operatorclass for costum functions
        row = layout.row()
        row.operator("boovel.intersectbool")
        row = layout.row()
        row.operator("boovel.differencebool")
        row = layout.row()
        row.label("Beveltools:")
        row = layout.row()
        row.operator("boovel.bevelinit")
        row = layout.row()
        row.prop(bpy.context.active_object.modifiers['Bevel'], "width")
        row = layout.row()
        row.prop(bpy.context.active_object.modifiers['Bevel'], "segments")
        row = layout.row()
        row.operator("boovel.zeroweight")
        row.operator("boovel.maxweight")
        row = layout.row()
        row.operator("boovel.symmetrize")
        row = layout.row()
        row.operator("boovel.selectsharp")
        
def register():
    bpy.utils.register_class(Boovel)
    bpy.utils.register_class(Unionbool)
    bpy.utils.register_class(Intersectbool)
    bpy.utils.register_class(Differencebool)
    bpy.utils.register_class(BevelInit)
    bpy.utils.register_class(ZeroWeight)
    bpy.utils.register_class(MaxWeight)
    bpy.utils.register_class(Symmetrize)
    bpy.utils.register_class(SelectSharp)

def unregister():
    bpy.utils.unregister_class(Boovel)
    bpy.utils.unregister_class(Unionbool)
    bpy.utils.unregister_class(Intersectbool)
    bpy.utils.unregister_class(Differencebool)
    bpy.utils.unregister_class(BevelInit)
    bpy.utils.unregister_class(ZeroWeight)
    bpy.utils.unregister_class(MaxWeight)
    bpy.utils.unregister_class(Symmetrize)
    bpy.utils.unregister_class(SelectSharp)

if __name__ == '__main__':
    register()
