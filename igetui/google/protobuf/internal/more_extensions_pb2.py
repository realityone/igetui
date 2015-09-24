# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/more_extensions.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/more_extensions.proto',
  package='google.protobuf.internal',
  serialized_pb='\n.google/protobuf/internal/more_extensions.proto\x12\x18google.protobuf.internal\"P\n\x0fTopLevelMessage\x12=\n\nsubmessage\x18\x01 \x01(\x0b\x32).google.protobuf.internal.ExtendedMessage\"\x1b\n\x0f\x45xtendedMessage*\x08\x08\x01\x10\x80\x80\x80\x80\x02\"-\n\x0e\x46oreignMessage\x12\x1b\n\x13\x66oreign_message_int\x18\x01 \x01(\x05:I\n\x16optional_int_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x01 \x01(\x05:w\n\x1aoptional_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x02 \x01(\x0b\x32(.google.protobuf.internal.ForeignMessage:I\n\x16repeated_int_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x03 \x03(\x05:w\n\x1arepeated_message_extension\x12).google.protobuf.internal.ExtendedMessage\x18\x04 \x03(\x0b\x32(.google.protobuf.internal.ForeignMessage')


OPTIONAL_INT_EXTENSION_FIELD_NUMBER = 1
optional_int_extension = _descriptor.FieldDescriptor(
  name='optional_int_extension', full_name='google.protobuf.internal.optional_int_extension', index=0,
  number=1, type=5, cpp_type=1, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
OPTIONAL_MESSAGE_EXTENSION_FIELD_NUMBER = 2
optional_message_extension = _descriptor.FieldDescriptor(
  name='optional_message_extension', full_name='google.protobuf.internal.optional_message_extension', index=1,
  number=2, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
REPEATED_INT_EXTENSION_FIELD_NUMBER = 3
repeated_int_extension = _descriptor.FieldDescriptor(
  name='repeated_int_extension', full_name='google.protobuf.internal.repeated_int_extension', index=2,
  number=3, type=5, cpp_type=1, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
REPEATED_MESSAGE_EXTENSION_FIELD_NUMBER = 4
repeated_message_extension = _descriptor.FieldDescriptor(
  name='repeated_message_extension', full_name='google.protobuf.internal.repeated_message_extension', index=3,
  number=4, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_TOPLEVELMESSAGE = _descriptor.Descriptor(
  name='TopLevelMessage',
  full_name='google.protobuf.internal.TopLevelMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='submessage', full_name='google.protobuf.internal.TopLevelMessage.submessage', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=76,
  serialized_end=156,
)


_EXTENDEDMESSAGE = _descriptor.Descriptor(
  name='ExtendedMessage',
  full_name='google.protobuf.internal.ExtendedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(1, 536870912), ],
  serialized_start=158,
  serialized_end=185,
)


_FOREIGNMESSAGE = _descriptor.Descriptor(
  name='ForeignMessage',
  full_name='google.protobuf.internal.ForeignMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='foreign_message_int', full_name='google.protobuf.internal.ForeignMessage.foreign_message_int', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=187,
  serialized_end=232,
)

_TOPLEVELMESSAGE.fields_by_name['submessage'].message_type = _EXTENDEDMESSAGE
DESCRIPTOR.message_types_by_name['TopLevelMessage'] = _TOPLEVELMESSAGE
DESCRIPTOR.message_types_by_name['ExtendedMessage'] = _EXTENDEDMESSAGE
DESCRIPTOR.message_types_by_name['ForeignMessage'] = _FOREIGNMESSAGE

class TopLevelMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TOPLEVELMESSAGE

  # @@protoc_insertion_point(class_scope:google.protobuf.internal.TopLevelMessage)

class ExtendedMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXTENDEDMESSAGE

  # @@protoc_insertion_point(class_scope:google.protobuf.internal.ExtendedMessage)

class ForeignMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FOREIGNMESSAGE

  # @@protoc_insertion_point(class_scope:google.protobuf.internal.ForeignMessage)

ExtendedMessage.RegisterExtension(optional_int_extension)
optional_message_extension.message_type = _FOREIGNMESSAGE
ExtendedMessage.RegisterExtension(optional_message_extension)
ExtendedMessage.RegisterExtension(repeated_int_extension)
repeated_message_extension.message_type = _FOREIGNMESSAGE
ExtendedMessage.RegisterExtension(repeated_message_extension)

# @@protoc_insertion_point(module_scope)
