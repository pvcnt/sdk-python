# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/query/v1/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.common.v1 import (
    message_pb2 as temporal_dot_api_dot_common_dot_v1_dot_message__pb2,
)
from temporalio.api.enums.v1 import (
    query_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_query__pb2,
)
from temporalio.api.enums.v1 import (
    workflow_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_workflow__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#temporal/api/query/v1/message.proto\x12\x15temporal.api.query.v1\x1a!temporal/api/enums/v1/query.proto\x1a$temporal/api/enums/v1/workflow.proto\x1a$temporal/api/common/v1/message.proto"\x89\x01\n\rWorkflowQuery\x12\x12\n\nquery_type\x18\x01 \x01(\t\x12\x34\n\nquery_args\x18\x02 \x01(\x0b\x32 .temporal.api.common.v1.Payloads\x12.\n\x06header\x18\x03 \x01(\x0b\x32\x1e.temporal.api.common.v1.Header"\x9b\x01\n\x13WorkflowQueryResult\x12;\n\x0bresult_type\x18\x01 \x01(\x0e\x32&.temporal.api.enums.v1.QueryResultType\x12\x30\n\x06\x61nswer\x18\x02 \x01(\x0b\x32 .temporal.api.common.v1.Payloads\x12\x15\n\rerror_message\x18\x03 \x01(\t"O\n\rQueryRejected\x12>\n\x06status\x18\x01 \x01(\x0e\x32..temporal.api.enums.v1.WorkflowExecutionStatusB\x84\x01\n\x18io.temporal.api.query.v1B\x0cMessageProtoP\x01Z!go.temporal.io/api/query/v1;query\xaa\x02\x17Temporalio.Api.Query.V1\xea\x02\x1aTemporalio::Api::Query::V1b\x06proto3'
)


_WORKFLOWQUERY = DESCRIPTOR.message_types_by_name["WorkflowQuery"]
_WORKFLOWQUERYRESULT = DESCRIPTOR.message_types_by_name["WorkflowQueryResult"]
_QUERYREJECTED = DESCRIPTOR.message_types_by_name["QueryRejected"]
WorkflowQuery = _reflection.GeneratedProtocolMessageType(
    "WorkflowQuery",
    (_message.Message,),
    {
        "DESCRIPTOR": _WORKFLOWQUERY,
        "__module__": "temporal.api.query.v1.message_pb2",
        # @@protoc_insertion_point(class_scope:temporal.api.query.v1.WorkflowQuery)
    },
)
_sym_db.RegisterMessage(WorkflowQuery)

WorkflowQueryResult = _reflection.GeneratedProtocolMessageType(
    "WorkflowQueryResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _WORKFLOWQUERYRESULT,
        "__module__": "temporal.api.query.v1.message_pb2",
        # @@protoc_insertion_point(class_scope:temporal.api.query.v1.WorkflowQueryResult)
    },
)
_sym_db.RegisterMessage(WorkflowQueryResult)

QueryRejected = _reflection.GeneratedProtocolMessageType(
    "QueryRejected",
    (_message.Message,),
    {
        "DESCRIPTOR": _QUERYREJECTED,
        "__module__": "temporal.api.query.v1.message_pb2",
        # @@protoc_insertion_point(class_scope:temporal.api.query.v1.QueryRejected)
    },
)
_sym_db.RegisterMessage(QueryRejected)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\030io.temporal.api.query.v1B\014MessageProtoP\001Z!go.temporal.io/api/query/v1;query\252\002\027Temporalio.Api.Query.V1\352\002\032Temporalio::Api::Query::V1"
    _WORKFLOWQUERY._serialized_start = 174
    _WORKFLOWQUERY._serialized_end = 311
    _WORKFLOWQUERYRESULT._serialized_start = 314
    _WORKFLOWQUERYRESULT._serialized_end = 469
    _QUERYREJECTED._serialized_start = 471
    _QUERYREJECTED._serialized_end = 550
# @@protoc_insertion_point(module_scope)
