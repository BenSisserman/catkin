// Auto-generated. Do not edit!

// (in-package motor_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class IntList {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.wheel = null;
      this.arm = null;
      this.hopper = null;
      this.bucket = null;
    }
    else {
      if (initObj.hasOwnProperty('wheel')) {
        this.wheel = initObj.wheel
      }
      else {
        this.wheel = [];
      }
      if (initObj.hasOwnProperty('arm')) {
        this.arm = initObj.arm
      }
      else {
        this.arm = [];
      }
      if (initObj.hasOwnProperty('hopper')) {
        this.hopper = initObj.hopper
      }
      else {
        this.hopper = [];
      }
      if (initObj.hasOwnProperty('bucket')) {
        this.bucket = initObj.bucket
      }
      else {
        this.bucket = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IntList
    // Serialize message field [wheel]
    bufferOffset = _arraySerializer.int32(obj.wheel, buffer, bufferOffset, null);
    // Serialize message field [arm]
    bufferOffset = _arraySerializer.int32(obj.arm, buffer, bufferOffset, null);
    // Serialize message field [hopper]
    bufferOffset = _arraySerializer.int32(obj.hopper, buffer, bufferOffset, null);
    // Serialize message field [bucket]
    bufferOffset = _arraySerializer.int32(obj.bucket, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IntList
    let len;
    let data = new IntList(null);
    // Deserialize message field [wheel]
    data.wheel = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [arm]
    data.arm = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [hopper]
    data.hopper = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [bucket]
    data.bucket = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.wheel.length;
    length += 4 * object.arm.length;
    length += 4 * object.hopper.length;
    length += 4 * object.bucket.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'motor_controller/IntList';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4e62f442e2d55a264cd175bb6226f3c7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] wheel
    int32[] arm
    int32[] hopper
    int32[] bucket
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IntList(null);
    if (msg.wheel !== undefined) {
      resolved.wheel = msg.wheel;
    }
    else {
      resolved.wheel = []
    }

    if (msg.arm !== undefined) {
      resolved.arm = msg.arm;
    }
    else {
      resolved.arm = []
    }

    if (msg.hopper !== undefined) {
      resolved.hopper = msg.hopper;
    }
    else {
      resolved.hopper = []
    }

    if (msg.bucket !== undefined) {
      resolved.bucket = msg.bucket;
    }
    else {
      resolved.bucket = []
    }

    return resolved;
    }
};

module.exports = IntList;
