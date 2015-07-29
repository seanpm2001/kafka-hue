#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def createTopic(self, zookeepers, replication, partitions, topic):
    """
    Parameters:
     - zookeepers
     - replication
     - partitions
     - topic
    """
    pass

  def showCurrentTimestamp(self, ):
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def createTopic(self, zookeepers, replication, partitions, topic):
    """
    Parameters:
     - zookeepers
     - replication
     - partitions
     - topic
    """
    self.send_createTopic(zookeepers, replication, partitions, topic)
    return self.recv_createTopic()

  def send_createTopic(self, zookeepers, replication, partitions, topic):
    self._oprot.writeMessageBegin('createTopic', TMessageType.CALL, self._seqid)
    args = createTopic_args()
    args.zookeepers = zookeepers
    args.replication = replication
    args.partitions = partitions
    args.topic = topic
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_createTopic(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = createTopic_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "createTopic failed: unknown result");

  def showCurrentTimestamp(self, ):
    self.send_showCurrentTimestamp()
    return self.recv_showCurrentTimestamp()

  def send_showCurrentTimestamp(self, ):
    self._oprot.writeMessageBegin('showCurrentTimestamp', TMessageType.CALL, self._seqid)
    args = showCurrentTimestamp_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_showCurrentTimestamp(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = showCurrentTimestamp_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "showCurrentTimestamp failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["createTopic"] = Processor.process_createTopic
    self._processMap["showCurrentTimestamp"] = Processor.process_showCurrentTimestamp

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_createTopic(self, seqid, iprot, oprot):
    args = createTopic_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = createTopic_result()
    result.success = self._handler.createTopic(args.zookeepers, args.replication, args.partitions, args.topic)
    oprot.writeMessageBegin("createTopic", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_showCurrentTimestamp(self, seqid, iprot, oprot):
    args = showCurrentTimestamp_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = showCurrentTimestamp_result()
    result.success = self._handler.showCurrentTimestamp()
    oprot.writeMessageBegin("showCurrentTimestamp", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class createTopic_args:
  """
  Attributes:
   - zookeepers
   - replication
   - partitions
   - topic
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'zookeepers', None, None, ), # 1
    (2, TType.I32, 'replication', None, None, ), # 2
    (3, TType.I32, 'partitions', None, None, ), # 3
    (4, TType.STRING, 'topic', None, None, ), # 4
  )

  def __init__(self, zookeepers=None, replication=None, partitions=None, topic=None,):
    self.zookeepers = zookeepers
    self.replication = replication
    self.partitions = partitions
    self.topic = topic

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.zookeepers = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.replication = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.partitions = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.topic = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createTopic_args')
    if self.zookeepers is not None:
      oprot.writeFieldBegin('zookeepers', TType.STRING, 1)
      oprot.writeString(self.zookeepers)
      oprot.writeFieldEnd()
    if self.replication is not None:
      oprot.writeFieldBegin('replication', TType.I32, 2)
      oprot.writeI32(self.replication)
      oprot.writeFieldEnd()
    if self.partitions is not None:
      oprot.writeFieldBegin('partitions', TType.I32, 3)
      oprot.writeI32(self.partitions)
      oprot.writeFieldEnd()
    if self.topic is not None:
      oprot.writeFieldBegin('topic', TType.STRING, 4)
      oprot.writeString(self.topic)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createTopic_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createTopic_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class showCurrentTimestamp_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('showCurrentTimestamp_args')
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class showCurrentTimestamp_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRING, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRING:
          self.success = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('showCurrentTimestamp_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRING, 0)
      oprot.writeString(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)