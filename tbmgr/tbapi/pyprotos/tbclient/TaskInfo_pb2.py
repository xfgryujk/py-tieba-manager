# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/TaskInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/TaskInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/TaskInfo.proto\x12\x08tbclient\"\xc6\x01\n\x08TaskInfo\x12\r\n\x05\x62gimg\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x06 \x01(\x03\x12\x10\n\x08\x66orum_id\x18\x08 \x01(\x03\x12\x12\n\nforum_name\x18\t \x01(\t\x12\x0e\n\x06obj_id\x18\n \x01(\t\x12\x12\n\nstart_time\x18\x05 \x01(\x03\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x11\n\tthread_id\x18\x02 \x01(\x03\x12\x12\n\nthread_img\x18\x04 \x01(\t\x12\x17\n\x0fthread_img_size\x18\x07 \x01(\t')
)




_TASKINFO = _descriptor.Descriptor(
  name='TaskInfo',
  full_name='tbclient.TaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bgimg', full_name='tbclient.TaskInfo.bgimg', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='tbclient.TaskInfo.end_time', index=1,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='tbclient.TaskInfo.forum_id', index=2,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum_name', full_name='tbclient.TaskInfo.forum_name', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obj_id', full_name='tbclient.TaskInfo.obj_id', index=4,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='tbclient.TaskInfo.start_time', index=5,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='task_id', full_name='tbclient.TaskInfo.task_id', index=6,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='tbclient.TaskInfo.thread_id', index=7,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_img', full_name='tbclient.TaskInfo.thread_img', index=8,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_img_size', full_name='tbclient.TaskInfo.thread_img_size', index=9,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=236,
)

DESCRIPTOR.message_types_by_name['TaskInfo'] = _TASKINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskInfo = _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), dict(
  DESCRIPTOR = _TASKINFO,
  __module__ = 'tbclient.TaskInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.TaskInfo)
  ))
_sym_db.RegisterMessage(TaskInfo)


# @@protoc_insertion_point(module_scope)
