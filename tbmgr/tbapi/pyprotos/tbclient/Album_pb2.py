# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/Album.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import ConcernUser_pb2 as tbclient_dot_ConcernUser__pb2
from tbclient import High_pb2 as tbclient_dot_High__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/Album.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x14tbclient/Album.proto\x12\x08tbclient\x1a\x1atbclient/ConcernUser.proto\x1a\x13tbclient/High.proto\"\xbd\x02\n\x05\x41lbum\x12\x10\n\x08\x61lbum_id\x18\x01 \x01(\x04\x12\x12\n\nalbum_name\x18\x08 \x01(\t\x12+\n\x0c\x63oncern_user\x18\x0c \x03(\x0b\x32\x15.tbclient.ConcernUser\x12\x13\n\x0b\x63reate_time\x18\x03 \x01(\r\x12\x10\n\x08\x64istance\x18\n \x01(\r\x12\x10\n\x08\x65nd_time\x18\x05 \x01(\r\x12\x1c\n\x04high\x18\x0b \x03(\x0b\x32\x0e.tbclient.High\x12\x10\n\x08location\x18\t \x01(\t\x12\x10\n\x08num_join\x18\x06 \x01(\r\x12\x10\n\x08num_user\x18\r \x01(\r\x12\x10\n\x08portrait\x18\x0f \x01(\t\x12\x12\n\nstart_time\x18\x04 \x01(\r\x12\x0b\n\x03uid\x18\x02 \x01(\x04\x12\x11\n\tuser_name\x18\x0e \x01(\t\x12\x0e\n\x06weight\x18\x07 \x01(\r')
  ,
  dependencies=[tbclient_dot_ConcernUser__pb2.DESCRIPTOR,tbclient_dot_High__pb2.DESCRIPTOR,])




_ALBUM = _descriptor.Descriptor(
  name='Album',
  full_name='tbclient.Album',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='album_id', full_name='tbclient.Album.album_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='album_name', full_name='tbclient.Album.album_name', index=1,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='concern_user', full_name='tbclient.Album.concern_user', index=2,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='tbclient.Album.create_time', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distance', full_name='tbclient.Album.distance', index=4,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='tbclient.Album.end_time', index=5,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='tbclient.Album.high', index=6,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='tbclient.Album.location', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_join', full_name='tbclient.Album.num_join', index=8,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_user', full_name='tbclient.Album.num_user', index=9,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.Album.portrait', index=10,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='tbclient.Album.start_time', index=11,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='tbclient.Album.uid', index=12,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.Album.user_name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tbclient.Album.weight', index=14,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=84,
  serialized_end=401,
)

_ALBUM.fields_by_name['concern_user'].message_type = tbclient_dot_ConcernUser__pb2._CONCERNUSER
_ALBUM.fields_by_name['high'].message_type = tbclient_dot_High__pb2._HIGH
DESCRIPTOR.message_types_by_name['Album'] = _ALBUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Album = _reflection.GeneratedProtocolMessageType('Album', (_message.Message,), dict(
  DESCRIPTOR = _ALBUM,
  __module__ = 'tbclient.Album_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Album)
  ))
_sym_db.RegisterMessage(Album)


# @@protoc_insertion_point(module_scope)
