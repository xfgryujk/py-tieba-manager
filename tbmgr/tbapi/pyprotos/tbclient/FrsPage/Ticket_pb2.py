# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/Ticket.proto

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
  name='tbclient/FrsPage/Ticket.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtbclient/FrsPage/Ticket.proto\x12\x10tbclient.FrsPage\"#\n\x06Ticket\x12\x0c\n\x04time\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t')
)




_TICKET = _descriptor.Descriptor(
  name='Ticket',
  full_name='tbclient.FrsPage.Ticket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='tbclient.FrsPage.Ticket.time', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.FrsPage.Ticket.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=51,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['Ticket'] = _TICKET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ticket = _reflection.GeneratedProtocolMessageType('Ticket', (_message.Message,), dict(
  DESCRIPTOR = _TICKET,
  __module__ = 'tbclient.FrsPage.Ticket_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.Ticket)
  ))
_sym_db.RegisterMessage(Ticket)


# @@protoc_insertion_point(module_scope)
