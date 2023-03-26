import bpy
import random

# Create a cube object
bpy.ops.mesh.primitive_cube_add(size=2)

# Create a new physics simulation
bpy.ops.object.select_all(action='SELECT')
bpy.ops.rigidbody.objects_add(type='ACTIVE')

# Set up a random force for each face of the cube
cube = bpy.context.active_object
for face in cube.data.polygons:
    force = (random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10))
    face.use_smooth = True
    face.use_collision = True
    face.normal *= 2.0
    face.material_index = 0
    face.use_dynamic_paint = True
    face.vertex_colors.new()
    face.vertex_colors[0].name = "Force"
    for vert_idx, loop_idx in zip(face.vertices, face.loop_indices):
        face.vertex_colors[0].data[loop_idx].color = force

# Run the simulation for a few frames
bpy.context.scene.rigidbody_world.point_cache.frame_start = 1
bpy.context.scene.rigidbody_world.point_cache.frame_end = 50
bpy.context.scene.frame_set(1)

# Destroy the cube by setting its scale to 0
bpy.context.object.scale = (0, 0, 0)
