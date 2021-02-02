# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from shape_msgs/Mesh.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import shape_msgs.msg

class Mesh(genpy.Message):
  _md5sum = "1ffdae9486cd3316a121c578b47a85cc"
  _type = "shape_msgs/Mesh"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Definition of a mesh

# list of triangles; the index values refer to positions in vertices[]
MeshTriangle[] triangles

# the actual vertices that make up the mesh
geometry_msgs/Point[] vertices

================================================================================
MSG: shape_msgs/MeshTriangle
# Definition of a triangle's vertices
uint32[3] vertex_indices

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['triangles','vertices']
  _slot_types = ['shape_msgs/MeshTriangle[]','geometry_msgs/Point[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       triangles,vertices

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Mesh, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.triangles is None:
        self.triangles = []
      if self.vertices is None:
        self.vertices = []
    else:
      self.triangles = []
      self.vertices = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.triangles)
      buff.write(_struct_I.pack(length))
      for val1 in self.triangles:
        buff.write(_get_struct_3I().pack(*val1.vertex_indices))
      length = len(self.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.vertices:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.triangles is None:
        self.triangles = None
      if self.vertices is None:
        self.vertices = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.triangles = []
      for i in range(0, length):
        val1 = shape_msgs.msg.MeshTriangle()
        start = end
        end += 12
        val1.vertex_indices = _get_struct_3I().unpack(str[start:end])
        self.triangles.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.vertices.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.triangles)
      buff.write(_struct_I.pack(length))
      for val1 in self.triangles:
        buff.write(val1.vertex_indices.tostring())
      length = len(self.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.vertices:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.triangles is None:
        self.triangles = None
      if self.vertices is None:
        self.vertices = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.triangles = []
      for i in range(0, length):
        val1 = shape_msgs.msg.MeshTriangle()
        start = end
        end += 12
        val1.vertex_indices = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
        self.triangles.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.vertices.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
