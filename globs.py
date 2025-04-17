import importlib
import site
import sys

import bpy

sys.path.insert(0, site.getusersitepackages())

pil_exist = True

is_blender_2_79_or_older = bpy.app.version < (2, 80, 0)
is_blender_2_80_or_newer = bpy.app.version >= (2, 80, 0)
is_blender_2_92_or_newer = bpy.app.version >= (2, 92, 0)
is_blender_3_or_newer = bpy.app.version >= (3, 0, 0)

smc_pi = False

CL_OBJECT = 0
CL_MATERIAL = 1
CL_SEPARATOR = 2
