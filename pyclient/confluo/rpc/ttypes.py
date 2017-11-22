#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class rpc_storage_mode(object):
    RPC_IN_MEMORY = 0
    RPC_DURABLE_RELAXED = 1
    RPC_DURABLE = 2

    _VALUES_TO_NAMES = {
        0: "RPC_IN_MEMORY",
        1: "RPC_DURABLE_RELAXED",
        2: "RPC_DURABLE",
    }

    _NAMES_TO_VALUES = {
        "RPC_IN_MEMORY": 0,
        "RPC_DURABLE_RELAXED": 1,
        "RPC_DURABLE": 2,
    }


class rpc_data_type(object):
    RPC_NONE = 0
    RPC_BOOL = 1
    RPC_CHAR = 2
    RPC_SHORT = 3
    RPC_INT = 4
    RPC_LONG = 5
    RPC_FLOAT = 6
    RPC_DOUBLE = 7
    RPC_STRING = 8
    RPC_RECORD = 9
    RPC_ALERT = 10

    _VALUES_TO_NAMES = {
        0: "RPC_NONE",
        1: "RPC_BOOL",
        2: "RPC_CHAR",
        3: "RPC_SHORT",
        4: "RPC_INT",
        5: "RPC_LONG",
        6: "RPC_FLOAT",
        7: "RPC_DOUBLE",
        8: "RPC_STRING",
        9: "RPC_RECORD",
        10: "RPC_ALERT",
    }

    _NAMES_TO_VALUES = {
        "RPC_NONE": 0,
        "RPC_BOOL": 1,
        "RPC_CHAR": 2,
        "RPC_SHORT": 3,
        "RPC_INT": 4,
        "RPC_LONG": 5,
        "RPC_FLOAT": 6,
        "RPC_DOUBLE": 7,
        "RPC_STRING": 8,
        "RPC_RECORD": 9,
        "RPC_ALERT": 10,
    }


class rpc_iterator_type(object):
    RPC_ADHOC = 0
    RPC_PREDEF = 1
    RPC_COMBINED = 2
    RPC_ALERTS = 3

    _VALUES_TO_NAMES = {
        0: "RPC_ADHOC",
        1: "RPC_PREDEF",
        2: "RPC_COMBINED",
        3: "RPC_ALERTS",
    }

    _NAMES_TO_VALUES = {
        "RPC_ADHOC": 0,
        "RPC_PREDEF": 1,
        "RPC_COMBINED": 2,
        "RPC_ALERTS": 3,
    }


class rpc_column(object):
    """
    Attributes:
     - type_id
     - type_size
     - name
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type_id', None, None, ),  # 1
        (2, TType.I32, 'type_size', None, None, ),  # 2
        (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
    )

    def __init__(self, type_id=None, type_size=None, name=None,):
        self.type_id = type_id
        self.type_size = type_size
        self.name = name

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type_size = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_column')
        if self.type_id is not None:
            oprot.writeFieldBegin('type_id', TType.I32, 1)
            oprot.writeI32(self.type_id)
            oprot.writeFieldEnd()
        if self.type_size is not None:
            oprot.writeFieldBegin('type_size', TType.I32, 2)
            oprot.writeI32(self.type_size)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.type_id is None:
            raise TProtocolException(message='Required field type_id is unset!')
        if self.type_size is None:
            raise TProtocolException(message='Required field type_size is unset!')
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_iterator_descriptor(object):
    """
    Attributes:
     - id
     - type
     - data_type
     - handler_id
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'id', None, None, ),  # 1
        (2, TType.I32, 'type', None, None, ),  # 2
        (3, TType.I32, 'data_type', None, None, ),  # 3
        (4, TType.I32, 'handler_id', None, None, ),  # 4
    )

    def __init__(self, id=None, type=None, data_type=None, handler_id=None,):
        self.id = id
        self.type = type
        self.data_type = data_type
        self.handler_id = handler_id

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.data_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.handler_id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_iterator_descriptor')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.data_type is not None:
            oprot.writeFieldBegin('data_type', TType.I32, 3)
            oprot.writeI32(self.data_type)
            oprot.writeFieldEnd()
        if self.handler_id is not None:
            oprot.writeFieldBegin('handler_id', TType.I32, 4)
            oprot.writeI32(self.handler_id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        if self.data_type is None:
            raise TProtocolException(message='Required field data_type is unset!')
        if self.handler_id is None:
            raise TProtocolException(message='Required field handler_id is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_iterator_handle(object):
    """
    Attributes:
     - desc
     - data
     - num_entries
     - has_more
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'desc', (rpc_iterator_descriptor, rpc_iterator_descriptor.thrift_spec), None, ),  # 1
        (2, TType.STRING, 'data', 'BINARY', None, ),  # 2
        (3, TType.I32, 'num_entries', None, None, ),  # 3
        (4, TType.BOOL, 'has_more', None, None, ),  # 4
    )

    def __init__(self, desc=None, data=None, num_entries=None, has_more=None,):
        self.desc = desc
        self.data = data
        self.num_entries = num_entries
        self.has_more = has_more

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.desc = rpc_iterator_descriptor()
                    self.desc.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.data = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.num_entries = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.has_more = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_iterator_handle')
        if self.desc is not None:
            oprot.writeFieldBegin('desc', TType.STRUCT, 1)
            self.desc.write(oprot)
            oprot.writeFieldEnd()
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.STRING, 2)
            oprot.writeBinary(self.data)
            oprot.writeFieldEnd()
        if self.num_entries is not None:
            oprot.writeFieldBegin('num_entries', TType.I32, 3)
            oprot.writeI32(self.num_entries)
            oprot.writeFieldEnd()
        if self.has_more is not None:
            oprot.writeFieldBegin('has_more', TType.BOOL, 4)
            oprot.writeBool(self.has_more)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.desc is None:
            raise TProtocolException(message='Required field desc is unset!')
        if self.data is None:
            raise TProtocolException(message='Required field data is unset!')
        if self.num_entries is None:
            raise TProtocolException(message='Required field num_entries is unset!')
        if self.has_more is None:
            raise TProtocolException(message='Required field has_more is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_record_block(object):
    """
    Attributes:
     - time_block
     - data
     - nrecords
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'time_block', None, None, ),  # 1
        (2, TType.STRING, 'data', 'BINARY', None, ),  # 2
        (3, TType.I64, 'nrecords', None, None, ),  # 3
    )

    def __init__(self, time_block=None, data=None, nrecords=None,):
        self.time_block = time_block
        self.data = data
        self.nrecords = nrecords

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.time_block = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.data = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.nrecords = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_record_block')
        if self.time_block is not None:
            oprot.writeFieldBegin('time_block', TType.I64, 1)
            oprot.writeI64(self.time_block)
            oprot.writeFieldEnd()
        if self.data is not None:
            oprot.writeFieldBegin('data', TType.STRING, 2)
            oprot.writeBinary(self.data)
            oprot.writeFieldEnd()
        if self.nrecords is not None:
            oprot.writeFieldBegin('nrecords', TType.I64, 3)
            oprot.writeI64(self.nrecords)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.time_block is None:
            raise TProtocolException(message='Required field time_block is unset!')
        if self.data is None:
            raise TProtocolException(message='Required field data is unset!')
        if self.nrecords is None:
            raise TProtocolException(message='Required field nrecords is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_record_batch(object):
    """
    Attributes:
     - blocks
     - nrecords
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'blocks', (TType.STRUCT, (rpc_record_block, rpc_record_block.thrift_spec), False), None, ),  # 1
        (2, TType.I64, 'nrecords', None, None, ),  # 2
    )

    def __init__(self, blocks=None, nrecords=None,):
        self.blocks = blocks
        self.nrecords = nrecords

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.blocks = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = rpc_record_block()
                        _elem5.read(iprot)
                        self.blocks.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.nrecords = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_record_batch')
        if self.blocks is not None:
            oprot.writeFieldBegin('blocks', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.blocks))
            for iter6 in self.blocks:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.nrecords is not None:
            oprot.writeFieldBegin('nrecords', TType.I64, 2)
            oprot.writeI64(self.nrecords)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.blocks is None:
            raise TProtocolException(message='Required field blocks is unset!')
        if self.nrecords is None:
            raise TProtocolException(message='Required field nrecords is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_atomic_multilog_info(object):
    """
    Attributes:
     - id
     - schema
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'id', None, None, ),  # 1
        (2, TType.LIST, 'schema', (TType.STRUCT, (rpc_column, rpc_column.thrift_spec), False), None, ),  # 2
    )

    def __init__(self, id=None, schema=None,):
        self.id = id
        self.schema = schema

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.schema = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = rpc_column()
                        _elem12.read(iprot)
                        self.schema.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_atomic_multilog_info')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.schema is not None:
            oprot.writeFieldBegin('schema', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.schema))
            for iter13 in self.schema:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_management_exception(TException):
    """
    Attributes:
     - msg
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
    )

    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_management_exception')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class rpc_invalid_operation(TException):
    """
    Attributes:
     - msg
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'msg', 'UTF8', None, ),  # 1
    )

    def __init__(self, msg=None,):
        self.msg = msg

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.msg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('rpc_invalid_operation')
        if self.msg is not None:
            oprot.writeFieldBegin('msg', TType.STRING, 1)
            oprot.writeString(self.msg.encode('utf-8') if sys.version_info[0] == 2 else self.msg)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
