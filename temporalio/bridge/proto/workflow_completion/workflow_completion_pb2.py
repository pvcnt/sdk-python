# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/sdk/core/workflow_completion/workflow_completion.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.enums.v1 import (
    failed_cause_pb2 as temporal_dot_api_dot_enums_dot_v1_dot_failed__cause__pb2,
)
from temporalio.api.failure.v1 import (
    message_pb2 as temporal_dot_api_dot_failure_dot_v1_dot_message__pb2,
)
from temporalio.bridge.proto.common import (
    common_pb2 as temporal_dot_sdk_dot_core_dot_common_dot_common__pb2,
)
from temporalio.bridge.proto.workflow_commands import (
    workflow_commands_pb2 as temporal_dot_sdk_dot_core_dot_workflow__commands_dot_workflow__commands__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n?temporal/sdk/core/workflow_completion/workflow_completion.proto\x12\x1b\x63oresdk.workflow_completion\x1a%temporal/api/failure/v1/message.proto\x1a(temporal/api/enums/v1/failed_cause.proto\x1a%temporal/sdk/core/common/common.proto\x1a;temporal/sdk/core/workflow_commands/workflow_commands.proto"\xac\x01\n\x1cWorkflowActivationCompletion\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12:\n\nsuccessful\x18\x02 \x01(\x0b\x32$.coresdk.workflow_completion.SuccessH\x00\x12\x36\n\x06\x66\x61iled\x18\x03 \x01(\x0b\x32$.coresdk.workflow_completion.FailureH\x00\x42\x08\n\x06status"d\n\x07Success\x12<\n\x08\x63ommands\x18\x01 \x03(\x0b\x32*.coresdk.workflow_commands.WorkflowCommand\x12\x1b\n\x13used_internal_flags\x18\x06 \x03(\r"\x81\x01\n\x07\x46\x61ilure\x12\x31\n\x07\x66\x61ilure\x18\x01 \x01(\x0b\x32 .temporal.api.failure.v1.Failure\x12\x43\n\x0b\x66orce_cause\x18\x02 \x01(\x0e\x32..temporal.api.enums.v1.WorkflowTaskFailedCauseB.\xea\x02+Temporalio::Bridge::Api::WorkflowCompletionb\x06proto3'
)


_WORKFLOWACTIVATIONCOMPLETION = DESCRIPTOR.message_types_by_name[
    "WorkflowActivationCompletion"
]
_SUCCESS = DESCRIPTOR.message_types_by_name["Success"]
_FAILURE = DESCRIPTOR.message_types_by_name["Failure"]
WorkflowActivationCompletion = _reflection.GeneratedProtocolMessageType(
    "WorkflowActivationCompletion",
    (_message.Message,),
    {
        "DESCRIPTOR": _WORKFLOWACTIVATIONCOMPLETION,
        "__module__": "temporal.sdk.core.workflow_completion.workflow_completion_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_completion.WorkflowActivationCompletion)
    },
)
_sym_db.RegisterMessage(WorkflowActivationCompletion)

Success = _reflection.GeneratedProtocolMessageType(
    "Success",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUCCESS,
        "__module__": "temporal.sdk.core.workflow_completion.workflow_completion_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_completion.Success)
    },
)
_sym_db.RegisterMessage(Success)

Failure = _reflection.GeneratedProtocolMessageType(
    "Failure",
    (_message.Message,),
    {
        "DESCRIPTOR": _FAILURE,
        "__module__": "temporal.sdk.core.workflow_completion.workflow_completion_pb2",
        # @@protoc_insertion_point(class_scope:coresdk.workflow_completion.Failure)
    },
)
_sym_db.RegisterMessage(Failure)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\352\002+Temporalio::Bridge::Api::WorkflowCompletion"
    )
    _WORKFLOWACTIVATIONCOMPLETION._serialized_start = 278
    _WORKFLOWACTIVATIONCOMPLETION._serialized_end = 450
    _SUCCESS._serialized_start = 452
    _SUCCESS._serialized_end = 552
    _FAILURE._serialized_start = 555
    _FAILURE._serialized_end = 684
# @@protoc_insertion_point(module_scope)
