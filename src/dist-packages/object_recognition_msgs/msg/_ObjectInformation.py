# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from object_recognition_msgs/ObjectInformation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import sensor_msgs.msg
import shape_msgs.msg
import std_msgs.msg

class ObjectInformation(genpy.Message):
  _md5sum = "921ec39f51c7b927902059cf3300ecde"
  _type = "object_recognition_msgs/ObjectInformation"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """############################################## VISUALIZATION INFO ######################################################
################### THIS INFO SHOULD BE OBTAINED INDEPENDENTLY FROM THE CORE, LIKE IN AN RVIZ PLUGIN ###################

# The human readable name of the object
string name

# The full mesh of the object: this can be useful for display purposes, augmented reality ... but it can be big
# Make sure the type is MESH
shape_msgs/Mesh ground_truth_mesh

# Sometimes, you only have a cloud in the DB
# Make sure the type is POINTS
sensor_msgs/PointCloud2 ground_truth_point_cloud

================================================================================
MSG: shape_msgs/Mesh
# Definition of a mesh

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

================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field
"""
  __slots__ = ['name','ground_truth_mesh','ground_truth_point_cloud']
  _slot_types = ['string','shape_msgs/Mesh','sensor_msgs/PointCloud2']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       name,ground_truth_mesh,ground_truth_point_cloud

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectInformation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.name is None:
        self.name = ''
      if self.ground_truth_mesh is None:
        self.ground_truth_mesh = shape_msgs.msg.Mesh()
      if self.ground_truth_point_cloud is None:
        self.ground_truth_point_cloud = sensor_msgs.msg.PointCloud2()
    else:
      self.name = ''
      self.ground_truth_mesh = shape_msgs.msg.Mesh()
      self.ground_truth_point_cloud = sensor_msgs.msg.PointCloud2()

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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.ground_truth_mesh.triangles)
      buff.write(_struct_I.pack(length))
      for val1 in self.ground_truth_mesh.triangles:
        buff.write(_get_struct_3I().pack(*val1.vertex_indices))
      length = len(self.ground_truth_mesh.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.ground_truth_mesh.vertices:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_3I().pack(_x.ground_truth_point_cloud.header.seq, _x.ground_truth_point_cloud.header.stamp.secs, _x.ground_truth_point_cloud.header.stamp.nsecs))
      _x = self.ground_truth_point_cloud.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.ground_truth_point_cloud.height, _x.ground_truth_point_cloud.width))
      length = len(self.ground_truth_point_cloud.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.ground_truth_point_cloud.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_get_struct_B2I().pack(_x.ground_truth_point_cloud.is_bigendian, _x.ground_truth_point_cloud.point_step, _x.ground_truth_point_cloud.row_step))
      _x = self.ground_truth_point_cloud.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.ground_truth_point_cloud.is_dense
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.ground_truth_mesh is None:
        self.ground_truth_mesh = shape_msgs.msg.Mesh()
      if self.ground_truth_point_cloud is None:
        self.ground_truth_point_cloud = sensor_msgs.msg.PointCloud2()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ground_truth_mesh.triangles = []
      for i in range(0, length):
        val1 = shape_msgs.msg.MeshTriangle()
        start = end
        end += 12
        val1.vertex_indices = _get_struct_3I().unpack(str[start:end])
        self.ground_truth_mesh.triangles.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ground_truth_mesh.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.ground_truth_mesh.vertices.append(val1)
      _x = self
      start = end
      end += 12
      (_x.ground_truth_point_cloud.header.seq, _x.ground_truth_point_cloud.header.stamp.secs, _x.ground_truth_point_cloud.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ground_truth_point_cloud.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.ground_truth_point_cloud.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.ground_truth_point_cloud.height, _x.ground_truth_point_cloud.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ground_truth_point_cloud.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
        self.ground_truth_point_cloud.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.ground_truth_point_cloud.is_bigendian, _x.ground_truth_point_cloud.point_step, _x.ground_truth_point_cloud.row_step,) = _get_struct_B2I().unpack(str[start:end])
      self.ground_truth_point_cloud.is_bigendian = bool(self.ground_truth_point_cloud.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.ground_truth_point_cloud.data = str[start:end]
      start = end
      end += 1
      (self.ground_truth_point_cloud.is_dense,) = _get_struct_B().unpack(str[start:end])
      self.ground_truth_point_cloud.is_dense = bool(self.ground_truth_point_cloud.is_dense)
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
      _x = self.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.ground_truth_mesh.triangles)
      buff.write(_struct_I.pack(length))
      for val1 in self.ground_truth_mesh.triangles:
        buff.write(val1.vertex_indices.tostring())
      length = len(self.ground_truth_mesh.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.ground_truth_mesh.vertices:
        _x = val1
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_get_struct_3I().pack(_x.ground_truth_point_cloud.header.seq, _x.ground_truth_point_cloud.header.stamp.secs, _x.ground_truth_point_cloud.header.stamp.nsecs))
      _x = self.ground_truth_point_cloud.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.ground_truth_point_cloud.height, _x.ground_truth_point_cloud.width))
      length = len(self.ground_truth_point_cloud.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.ground_truth_point_cloud.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_IBI().pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_get_struct_B2I().pack(_x.ground_truth_point_cloud.is_bigendian, _x.ground_truth_point_cloud.point_step, _x.ground_truth_point_cloud.row_step))
      _x = self.ground_truth_point_cloud.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.Struct('<I%sB'%length).pack(length, *_x))
      else:
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.ground_truth_point_cloud.is_dense
      buff.write(_get_struct_B().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.ground_truth_mesh is None:
        self.ground_truth_mesh = shape_msgs.msg.Mesh()
      if self.ground_truth_point_cloud is None:
        self.ground_truth_point_cloud = sensor_msgs.msg.PointCloud2()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ground_truth_mesh.triangles = []
      for i in range(0, length):
        val1 = shape_msgs.msg.MeshTriangle()
        start = end
        end += 12
        val1.vertex_indices = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=3)
        self.ground_truth_mesh.triangles.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ground_truth_mesh.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        self.ground_truth_mesh.vertices.append(val1)
      _x = self
      start = end
      end += 12
      (_x.ground_truth_point_cloud.header.seq, _x.ground_truth_point_cloud.header.stamp.secs, _x.ground_truth_point_cloud.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.ground_truth_point_cloud.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.ground_truth_point_cloud.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.ground_truth_point_cloud.height, _x.ground_truth_point_cloud.width,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.ground_truth_point_cloud.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _get_struct_IBI().unpack(str[start:end])
        self.ground_truth_point_cloud.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.ground_truth_point_cloud.is_bigendian, _x.ground_truth_point_cloud.point_step, _x.ground_truth_point_cloud.row_step,) = _get_struct_B2I().unpack(str[start:end])
      self.ground_truth_point_cloud.is_bigendian = bool(self.ground_truth_point_cloud.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.ground_truth_point_cloud.data = str[start:end]
      start = end
      end += 1
      (self.ground_truth_point_cloud.is_dense,) = _get_struct_B().unpack(str[start:end])
      self.ground_truth_point_cloud.is_dense = bool(self.ground_truth_point_cloud.is_dense)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
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
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B2I = None
def _get_struct_B2I():
    global _struct_B2I
    if _struct_B2I is None:
        _struct_B2I = struct.Struct("<B2I")
    return _struct_B2I
_struct_IBI = None
def _get_struct_IBI():
    global _struct_IBI
    if _struct_IBI is None:
        _struct_IBI = struct.Struct("<IBI")
    return _struct_IBI
