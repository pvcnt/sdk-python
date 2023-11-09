# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: health/v1/health.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16health/v1/health.proto\x12\x17temporal.grpc.health.v1"%\n\x12HealthCheckRequest\x12\x0f\n\x07service\x18\x01 \x01(\t"\xb2\x01\n\x13HealthCheckResponse\x12J\n\x06status\x18\x01 \x01(\x0e\x32:.temporal.grpc.health.v1.HealthCheckResponse.ServingStatus"O\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x12\x13\n\x0fSERVICE_UNKNOWN\x10\x03\x32\xd2\x01\n\x06Health\x12\x62\n\x05\x43heck\x12+.temporal.grpc.health.v1.HealthCheckRequest\x1a,.temporal.grpc.health.v1.HealthCheckResponse\x12\x64\n\x05Watch\x12+.temporal.grpc.health.v1.HealthCheckRequest\x1a,.temporal.grpc.health.v1.HealthCheckResponse0\x01\x42\x61\n\x11io.grpc.health.v1B\x0bHealthProtoP\x01Z,google.golang.org/grpc/health/grpc_health_v1\xaa\x02\x0eGrpc.Health.V1b\x06proto3'
)


_HEALTHCHECKREQUEST = DESCRIPTOR.message_types_by_name["HealthCheckRequest"]
_HEALTHCHECKRESPONSE = DESCRIPTOR.message_types_by_name["HealthCheckResponse"]
_HEALTHCHECKRESPONSE_SERVINGSTATUS = _HEALTHCHECKRESPONSE.enum_types_by_name[
    "ServingStatus"
]
HealthCheckRequest = _reflection.GeneratedProtocolMessageType(
    "HealthCheckRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEALTHCHECKREQUEST,
        "__module__": "health.v1.health_pb2",
        # @@protoc_insertion_point(class_scope:temporal.grpc.health.v1.HealthCheckRequest)
    },
)
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckResponse = _reflection.GeneratedProtocolMessageType(
    "HealthCheckResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _HEALTHCHECKRESPONSE,
        "__module__": "health.v1.health_pb2",
        # @@protoc_insertion_point(class_scope:temporal.grpc.health.v1.HealthCheckResponse)
    },
)
_sym_db.RegisterMessage(HealthCheckResponse)

_HEALTH = DESCRIPTOR.services_by_name["Health"]
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\021io.grpc.health.v1B\013HealthProtoP\001Z,google.golang.org/grpc/health/grpc_health_v1\252\002\016Grpc.Health.V1"
    _HEALTHCHECKREQUEST._serialized_start = 51
    _HEALTHCHECKREQUEST._serialized_end = 88
    _HEALTHCHECKRESPONSE._serialized_start = 91
    _HEALTHCHECKRESPONSE._serialized_end = 269
    _HEALTHCHECKRESPONSE_SERVINGSTATUS._serialized_start = 190
    _HEALTHCHECKRESPONSE_SERVINGSTATUS._serialized_end = 269
    _HEALTH._serialized_start = 272
    _HEALTH._serialized_end = 482
# @@protoc_insertion_point(module_scope)
