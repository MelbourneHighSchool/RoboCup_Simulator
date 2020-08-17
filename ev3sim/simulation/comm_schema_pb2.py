# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ev3sim/simulation/comm_schema.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ev3sim/simulation/comm_schema.proto',
  package='serverComm',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#ev3sim/simulation/comm_schema.proto\x12\nserverComm\" \n\x0cRobotRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\"=\n\tRobotData\x12\x0c\n\x04tick\x18\x01 \x01(\x05\x12\x11\n\ttick_rate\x18\x02 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"E\n\nRobotWrite\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x16\n\x0e\x61ttribute_path\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x1d\n\x0bWriteResult\x12\x0e\n\x06result\x18\x01 \x01(\x08\"@\n\rServerRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\"+\n\x0cServerResult\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t\"@\n\rClientRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\"B\n\x0c\x43lientResult\x12\x15\n\rhost_robot_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\x0b\n\x03msg\x18\x03 \x01(\t\"_\n\x0bSendRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\t\x12\x11\n\tclient_id\x18\x05 \x01(\t\")\n\nSendResult\x12\x0e\n\x06result\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t\"Q\n\x0bRecvRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\"7\n\nRecvResult\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\x0b\n\x03msg\x18\x03 \x01(\t\"C\n\x10GetClientRequest\x12\x10\n\x08robot_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\"A\n\x0fGetClientResult\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\x08\x12\x0b\n\x03msg\x18\x03 \x01(\t2\x87\x04\n\x10SimulationDealer\x12I\n\x12RequestTickUpdates\x12\x18.serverComm.RobotRequest\x1a\x15.serverComm.RobotData\"\x00\x30\x01\x12\x42\n\rSendWriteInfo\x12\x16.serverComm.RobotWrite\x1a\x17.serverComm.WriteResult\"\x00\x12\x46\n\rRequestServer\x12\x19.serverComm.ServerRequest\x1a\x18.serverComm.ServerResult\"\x00\x12G\n\x0eRequestConnect\x12\x19.serverComm.ClientRequest\x1a\x18.serverComm.ClientResult\"\x00\x12@\n\x0bRequestSend\x12\x17.serverComm.SendRequest\x1a\x16.serverComm.SendResult\"\x00\x12@\n\x0bRequestRecv\x12\x17.serverComm.RecvRequest\x1a\x16.serverComm.RecvResult\"\x00\x12O\n\x10RequestGetClient\x12\x1c.serverComm.GetClientRequest\x1a\x1b.serverComm.GetClientResult\"\x00\x62\x06proto3'
)




_ROBOTREQUEST = _descriptor.Descriptor(
  name='RobotRequest',
  full_name='serverComm.RobotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.RobotRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=83,
)


_ROBOTDATA = _descriptor.Descriptor(
  name='RobotData',
  full_name='serverComm.RobotData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tick', full_name='serverComm.RobotData.tick', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tick_rate', full_name='serverComm.RobotData.tick_rate', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='serverComm.RobotData.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=146,
)


_ROBOTWRITE = _descriptor.Descriptor(
  name='RobotWrite',
  full_name='serverComm.RobotWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.RobotWrite.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribute_path', full_name='serverComm.RobotWrite.attribute_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='serverComm.RobotWrite.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=217,
)


_WRITERESULT = _descriptor.Descriptor(
  name='WriteResult',
  full_name='serverComm.WriteResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.WriteResult.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=248,
)


_SERVERREQUEST = _descriptor.Descriptor(
  name='ServerRequest',
  full_name='serverComm.ServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.ServerRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='serverComm.ServerRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='serverComm.ServerRequest.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=314,
)


_SERVERRESULT = _descriptor.Descriptor(
  name='ServerResult',
  full_name='serverComm.ServerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.ServerResult.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='serverComm.ServerResult.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=359,
)


_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='serverComm.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.ClientRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='serverComm.ClientRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='serverComm.ClientRequest.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=361,
  serialized_end=425,
)


_CLIENTRESULT = _descriptor.Descriptor(
  name='ClientResult',
  full_name='serverComm.ClientResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_robot_id', full_name='serverComm.ClientResult.host_robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.ClientResult.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='serverComm.ClientResult.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=427,
  serialized_end=493,
)


_SENDREQUEST = _descriptor.Descriptor(
  name='SendRequest',
  full_name='serverComm.SendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.SendRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='serverComm.SendRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='serverComm.SendRequest.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='serverComm.SendRequest.data', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='serverComm.SendRequest.client_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=590,
)


_SENDRESULT = _descriptor.Descriptor(
  name='SendResult',
  full_name='serverComm.SendResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.SendResult.result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='serverComm.SendResult.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=592,
  serialized_end=633,
)


_RECVREQUEST = _descriptor.Descriptor(
  name='RecvRequest',
  full_name='serverComm.RecvRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.RecvRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='serverComm.RecvRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='serverComm.RecvRequest.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='serverComm.RecvRequest.client_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=635,
  serialized_end=716,
)


_RECVRESULT = _descriptor.Descriptor(
  name='RecvResult',
  full_name='serverComm.RecvResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='serverComm.RecvResult.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.RecvResult.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='serverComm.RecvResult.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=773,
)


_GETCLIENTREQUEST = _descriptor.Descriptor(
  name='GetClientRequest',
  full_name='serverComm.GetClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='serverComm.GetClientRequest.robot_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='serverComm.GetClientRequest.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='serverComm.GetClientRequest.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=775,
  serialized_end=842,
)


_GETCLIENTRESULT = _descriptor.Descriptor(
  name='GetClientResult',
  full_name='serverComm.GetClientResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='serverComm.GetClientResult.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='serverComm.GetClientResult.result', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='serverComm.GetClientResult.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=844,
  serialized_end=909,
)

DESCRIPTOR.message_types_by_name['RobotRequest'] = _ROBOTREQUEST
DESCRIPTOR.message_types_by_name['RobotData'] = _ROBOTDATA
DESCRIPTOR.message_types_by_name['RobotWrite'] = _ROBOTWRITE
DESCRIPTOR.message_types_by_name['WriteResult'] = _WRITERESULT
DESCRIPTOR.message_types_by_name['ServerRequest'] = _SERVERREQUEST
DESCRIPTOR.message_types_by_name['ServerResult'] = _SERVERRESULT
DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['ClientResult'] = _CLIENTRESULT
DESCRIPTOR.message_types_by_name['SendRequest'] = _SENDREQUEST
DESCRIPTOR.message_types_by_name['SendResult'] = _SENDRESULT
DESCRIPTOR.message_types_by_name['RecvRequest'] = _RECVREQUEST
DESCRIPTOR.message_types_by_name['RecvResult'] = _RECVRESULT
DESCRIPTOR.message_types_by_name['GetClientRequest'] = _GETCLIENTREQUEST
DESCRIPTOR.message_types_by_name['GetClientResult'] = _GETCLIENTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RobotRequest = _reflection.GeneratedProtocolMessageType('RobotRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTREQUEST,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RobotRequest)
  })
_sym_db.RegisterMessage(RobotRequest)

RobotData = _reflection.GeneratedProtocolMessageType('RobotData', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTDATA,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RobotData)
  })
_sym_db.RegisterMessage(RobotData)

RobotWrite = _reflection.GeneratedProtocolMessageType('RobotWrite', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTWRITE,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RobotWrite)
  })
_sym_db.RegisterMessage(RobotWrite)

WriteResult = _reflection.GeneratedProtocolMessageType('WriteResult', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESULT,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.WriteResult)
  })
_sym_db.RegisterMessage(WriteResult)

ServerRequest = _reflection.GeneratedProtocolMessageType('ServerRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVERREQUEST,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.ServerRequest)
  })
_sym_db.RegisterMessage(ServerRequest)

ServerResult = _reflection.GeneratedProtocolMessageType('ServerResult', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESULT,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.ServerResult)
  })
_sym_db.RegisterMessage(ServerResult)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTREQUEST,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.ClientRequest)
  })
_sym_db.RegisterMessage(ClientRequest)

ClientResult = _reflection.GeneratedProtocolMessageType('ClientResult', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTRESULT,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.ClientResult)
  })
_sym_db.RegisterMessage(ClientResult)

SendRequest = _reflection.GeneratedProtocolMessageType('SendRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDREQUEST,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.SendRequest)
  })
_sym_db.RegisterMessage(SendRequest)

SendResult = _reflection.GeneratedProtocolMessageType('SendResult', (_message.Message,), {
  'DESCRIPTOR' : _SENDRESULT,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.SendResult)
  })
_sym_db.RegisterMessage(SendResult)

RecvRequest = _reflection.GeneratedProtocolMessageType('RecvRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECVREQUEST,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RecvRequest)
  })
_sym_db.RegisterMessage(RecvRequest)

RecvResult = _reflection.GeneratedProtocolMessageType('RecvResult', (_message.Message,), {
  'DESCRIPTOR' : _RECVRESULT,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.RecvResult)
  })
_sym_db.RegisterMessage(RecvResult)

GetClientRequest = _reflection.GeneratedProtocolMessageType('GetClientRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTREQUEST,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.GetClientRequest)
  })
_sym_db.RegisterMessage(GetClientRequest)

GetClientResult = _reflection.GeneratedProtocolMessageType('GetClientResult', (_message.Message,), {
  'DESCRIPTOR' : _GETCLIENTRESULT,
  '__module__' : 'ev3sim.simulation.comm_schema_pb2'
  # @@protoc_insertion_point(class_scope:serverComm.GetClientResult)
  })
_sym_db.RegisterMessage(GetClientResult)



_SIMULATIONDEALER = _descriptor.ServiceDescriptor(
  name='SimulationDealer',
  full_name='serverComm.SimulationDealer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=912,
  serialized_end=1431,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestTickUpdates',
    full_name='serverComm.SimulationDealer.RequestTickUpdates',
    index=0,
    containing_service=None,
    input_type=_ROBOTREQUEST,
    output_type=_ROBOTDATA,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendWriteInfo',
    full_name='serverComm.SimulationDealer.SendWriteInfo',
    index=1,
    containing_service=None,
    input_type=_ROBOTWRITE,
    output_type=_WRITERESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestServer',
    full_name='serverComm.SimulationDealer.RequestServer',
    index=2,
    containing_service=None,
    input_type=_SERVERREQUEST,
    output_type=_SERVERRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestConnect',
    full_name='serverComm.SimulationDealer.RequestConnect',
    index=3,
    containing_service=None,
    input_type=_CLIENTREQUEST,
    output_type=_CLIENTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestSend',
    full_name='serverComm.SimulationDealer.RequestSend',
    index=4,
    containing_service=None,
    input_type=_SENDREQUEST,
    output_type=_SENDRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestRecv',
    full_name='serverComm.SimulationDealer.RequestRecv',
    index=5,
    containing_service=None,
    input_type=_RECVREQUEST,
    output_type=_RECVRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RequestGetClient',
    full_name='serverComm.SimulationDealer.RequestGetClient',
    index=6,
    containing_service=None,
    input_type=_GETCLIENTREQUEST,
    output_type=_GETCLIENTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SIMULATIONDEALER)

DESCRIPTOR.services_by_name['SimulationDealer'] = _SIMULATIONDEALER

# @@protoc_insertion_point(module_scope)
