article_outdated

:   True

# Binary serialization API {#doc_binary_serialization_api}

## Introduction

Godot has a serialization API based on Variant. It\'s used for
converting data types to an array of bytes efficiently. This API is
exposed via the global
`bytes_to_var() <class_@GlobalScope_method_bytes_to_var>`{.interpreted-text
role="ref"} and
`var_to_bytes() <class_@GlobalScope_method_var_to_bytes>`{.interpreted-text
role="ref"} functions, but it is also used in the `get_var` and
`store_var` methods of `class_FileAccess`{.interpreted-text role="ref"}
as well as the packet APIs for `class_PacketPeer`{.interpreted-text
role="ref"}. This format is *not* used for binary scenes and resources.

## Full Objects vs Object instance IDs

If a variable is serialized with `full_objects = true`, then any Objects
contained in the variable will be serialized and included in the result.
This is recursive.

If `full_objects = false`, then only the instance IDs will be serialized
for any Objects contained in the variable.

## Packet specification

The packet is designed to be always padded to 4 bytes. All values are
little-endian-encoded. All packets have a 4-byte header representing an
integer, specifying the type of data.

The lowest value two bytes are used to determine the type, while the
highest value two bytes contain flags:

    base_type = val & 0xFFFF;
    flags = val >> 16;

| Type | Value         |
|------|---------------|
| 0    | null          |
| 1    | bool          |
| 2    | integer       |
| 3    | float         |
| 4    | string        |
| 5    | vector2       |
| 6    | rect2         |
| 7    | vector3       |
| 8    | transform2d   |
| 9    | plane         |
| 10   | quaternion    |
| 11   | aabb          |
| 12   | basis         |
| 13   | transform3d   |
| 14   | color         |
| 15   | node path     |
| 16   | rid           |
| 17   | object        |
| 18   | dictionary    |
| 19   | array         |
| 20   | raw array     |
| 21   | int32 array   |
| 22   | int64 array   |
| 23   | float32 array |
| 24   | float64 array |
| 25   | string array  |
| 26   | vector2 array |
| 27   | vector3 array |
| 28   | color array   |
| 29   | max           |

Following this is the actual packet contents, which varies for each type
of packet. Note that this assumes Godot is compiled with
single-precision floats, which is the default. If Godot was compiled
with double-precision floats, the length of \"Float\" fields within data
structures should be 8, and the offset should be `(offset - 4) * 2 + 4`.
The \"float\" type itself always uses double precision.

### 0: null {#null}

### 1: `bool<class_bool>`{.interpreted-text role="ref"} {#boolclass_bool}

| Offset | Len | Type    | Description             |
|--------|-----|---------|-------------------------|
| 4      | 4   | Integer | 0 for False, 1 for True |

### 2: `int<class_int>`{.interpreted-text role="ref"} {#intclass_int}

If no flags are set (flags == 0), the integer is sent as a 32 bit
integer:

| Offset | Len | Type    | Description           |
|--------|-----|---------|-----------------------|
| 4      | 4   | Integer | 32-bit signed integer |

If flag `ENCODE_FLAG_64` is set (`flags & 1 == 1`), the integer is sent
as a 64-bit integer:

| Offset | Len | Type    | Description           |
|--------|-----|---------|-----------------------|
| 4      | 8   | Integer | 64-bit signed integer |

### 3: `float<class_float>`{.interpreted-text role="ref"} {#floatclass_float}

If no flags are set (flags == 0), the float is sent as a 32 bit single
precision:

| Offset | Len | Type  | Description                     |
|--------|-----|-------|---------------------------------|
| 4      | 4   | Float | IEEE 754 single-precision float |

If flag `ENCODE_FLAG_64` is set (`flags & 1 == 1`), the float is sent as
a 64-bit double precision number:

| Offset | Len | Type  | Description                     |
|--------|-----|-------|---------------------------------|
| 4      | 8   | Float | IEEE 754 double-precision float |

### 4: `String<class_string>`{.interpreted-text role="ref"} {#stringclass_string}

| Offset | Len | Type    | Description              |
|--------|-----|---------|--------------------------|
| 4      | 4   | Integer | String length (in bytes) |
| 8      | X   | Bytes   | UTF-8 encoded string     |

This field is padded to 4 bytes.

### 5: `Vector2<class_vector2>`{.interpreted-text role="ref"} {#vector2class_vector2}

| Offset | Len | Type  | Description  |
|--------|-----|-------|--------------|
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |

### 6: `Rect2<class_rect2>`{.interpreted-text role="ref"} {#rect2class_rect2}

| Offset | Len | Type  | Description  |
|--------|-----|-------|--------------|
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |
| 12     | 4   | Float | X size       |
| 16     | 4   | Float | Y size       |

### 7: `Vector3<class_vector3>`{.interpreted-text role="ref"} {#vector3class_vector3}

| Offset | Len | Type  | Description  |
|--------|-----|-------|--------------|
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |
| 12     | 4   | Float | Z coordinate |

### 8: `Transform2D<class_transform2d>`{.interpreted-text role="ref"} {#transform2dclass_transform2d}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Float | The X component of the X column vector, accessed via \[0\]\[0\] |
| 8 | 4 | Float | The Y component of the X column vector, accessed via \[0\]\[1\] |
| 12 | 4 | Float | The X component of the Y column vector, accessed via \[1\]\[0\] |
| 16 | 4 | Float | The Y component of the Y column vector, accessed via \[1\]\[1\] |
| 20 | 4 | Float | The X component of the origin vector, accessed via \[2\]\[0\] |
| 24 | 4 | Float | The Y component of the origin vector, accessed via \[2\]\[1\] |

### 9: `Plane<class_plane>`{.interpreted-text role="ref"} {#planeclass_plane}

| Offset | Len | Type  | Description |
|--------|-----|-------|-------------|
| 4      | 4   | Float | Normal X    |
| 8      | 4   | Float | Normal Y    |
| 12     | 4   | Float | Normal Z    |
| 16     | 4   | Float | Distance    |

### 10: `Quaternion<class_quaternion>`{.interpreted-text role="ref"} {#quaternionclass_quaternion}

| Offset | Len | Type  | Description |
|--------|-----|-------|-------------|
| 4      | 4   | Float | Imaginary X |
| 8      | 4   | Float | Imaginary Y |
| 12     | 4   | Float | Imaginary Z |
| 16     | 4   | Float | Real W      |

### 11: `AABB<class_aabb>`{.interpreted-text role="ref"} {#aabbclass_aabb}

| Offset | Len | Type  | Description  |
|--------|-----|-------|--------------|
| 4      | 4   | Float | X coordinate |
| 8      | 4   | Float | Y coordinate |
| 12     | 4   | Float | Z coordinate |
| 16     | 4   | Float | X size       |
| 20     | 4   | Float | Y size       |
| 24     | 4   | Float | Z size       |

### 12: `Basis<class_basis>`{.interpreted-text role="ref"} {#basisclass_basis}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Float | The X component of the X column vector, accessed via \[0\]\[0\] |
| 8 | 4 | Float | The Y component of the X column vector, accessed via \[0\]\[1\] |
| 12 | 4 | Float | The Z component of the X column vector, accessed via \[0\]\[2\] |
| 16 | 4 | Float | The X component of the Y column vector, accessed via \[1\]\[0\] |
| 20 | 4 | Float | The Y component of the Y column vector, accessed via \[1\]\[1\] |
| 24 | 4 | Float | The Z component of the Y column vector, accessed via \[1\]\[2\] |
| 28 | 4 | Float | The X component of the Z column vector, accessed via \[2\]\[0\] |
| 32 | 4 | Float | The Y component of the Z column vector, accessed via \[2\]\[1\] |
| 36 | 4 | Float | The Z component of the Z column vector, accessed via \[2\]\[2\] |

### 13: `Transform3D<class_transform3d>`{.interpreted-text role="ref"} {#transform3dclass_transform3d}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Float | The X component of the X column vector, accessed via \[0\]\[0\] |
| 8 | 4 | Float | The Y component of the X column vector, accessed via \[0\]\[1\] |
| 12 | 4 | Float | The Z component of the X column vector, accessed via \[0\]\[2\] |
| 16 | 4 | Float | The X component of the Y column vector, accessed via \[1\]\[0\] |
| 20 | 4 | Float | The Y component of the Y column vector, accessed via \[1\]\[1\] |
| 24 | 4 | Float | The Z component of the Y column vector, accessed via \[1\]\[2\] |
| 28 | 4 | Float | The X component of the Z column vector, accessed via \[2\]\[0\] |
| 32 | 4 | Float | The Y component of the Z column vector, accessed via \[2\]\[1\] |
| 36 | 4 | Float | The Z component of the Z column vector, accessed via \[2\]\[2\] |
| 40 | 4 | Float | The X component of the origin vector, accessed via \[3\]\[0\] |
| 44 | 4 | Float | The Y component of the origin vector, accessed via \[3\]\[1\] |
| 48 | 4 | Float | The Z component of the origin vector, accessed via \[3\]\[2\] |

### 14: `Color<class_color>`{.interpreted-text role="ref"} {#colorclass_color}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Float | Red (typically 0..1, can be above 1 for overbright colors) |
| 8 | 4 | Float | Green (typically 0..1, can be above 1 for overbright colors) |
| 12 | 4 | Float | Blue (typically 0..1, can be above 1 for overbright colors) |
| 16 | 4 | Float | Alpha (0..1) |

### 15: `NodePath<class_nodepath>`{.interpreted-text role="ref"} {#nodepathclass_nodepath}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Integer | String length, or new format (val&0x80000000!=0 and NameCount=val&0x7FFFFFFF) |

### For old format:

| Offset | Len | Type  | Description          |
|--------|-----|-------|----------------------|
| 8      | X   | Bytes | UTF-8 encoded string |

Padded to 4 bytes.

### For new format:

| Offset | Len | Type    | Description                   |
|--------|-----|---------|-------------------------------|
| 4      | 4   | Integer | Sub-name count                |
| 8      | 4   | Integer | Flags (absolute: val&1 != 0 ) |

For each Name and Sub-Name

| Offset | Len | Type    | Description          |
|--------|-----|---------|----------------------|
| X+0    | 4   | Integer | String length        |
| X+4    | X   | Bytes   | UTF-8 encoded string |

Every name string is padded to 4 bytes.

### 16: `RID<class_rid>`{.interpreted-text role="ref"} (unsupported) {#ridclass_rid-unsupported}

### 17: `Object<class_object>`{.interpreted-text role="ref"} {#objectclass_object}

An Object could be serialized in three different ways: as a null value,
with `full_objects = false`, or with `full_objects = true`.

#### A null value

| Offset | Len | Type    | Description                  |
|--------|-----|---------|------------------------------|
| 4      | 4   | Integer | Zero (32-bit signed integer) |

#### `full_objects` disabled

| Offset | Len | Type    | Description                                    |
|--------|-----|---------|------------------------------------------------|
| 4      | 8   | Integer | The Object instance ID (64-bit signed integer) |

#### `full_objects` enabled

| Offset | Len | Type    | Description                                  |
|--------|-----|---------|----------------------------------------------|
| 4      | 4   | Integer | Class name (String length)                   |
| 8      | X   | Bytes   | Class name (UTF-8 encoded string)            |
| X+8    | 4   | Integer | The number of properties that are serialized |

For each property:

| Offset | Len | Type         | Description                            |
|--------|-----|--------------|----------------------------------------|
| Y      | 4   | Integer      | Property name (String length)          |
| Y+4    | Z   | Bytes        | Property name (UTF-8 encoded string)   |
| Y+4+Z  | W   | \<variable\> | Property value, using this same format |

> [!NOTE]
> Not all properties are included. Only properties that are configured
> with the
> `PROPERTY_USAGE_STORAGE<class_@GlobalScope_constant_PROPERTY_USAGE_STORAGE>`{.interpreted-text
> role="ref"} flag set will be serialized. You can add a new usage flag
> to a property by overriding the
> `_get_property_list<class_Object_private_method__get_property_list>`{.interpreted-text
> role="ref"} method in your class. You can also check how property
> usage is configured by calling `Object._get_property_list` See
> `PropertyUsageFlags<enum_@GlobalScope_PropertyUsageFlags>`{.interpreted-text
> role="ref"} for the possible usage flags.

### 18: `Dictionary<class_dictionary>`{.interpreted-text role="ref"} {#dictionaryclass_dictionary}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Integer | val&0x7FFFFFFF = elements, val&0x80000000 = shared (bool) |

Then what follows is, for amount of \"elements\", pairs of key and
value, one after the other, using this same format.

### 19: `Array<class_array>`{.interpreted-text role="ref"} {#arrayclass_array}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Integer | val&0x7FFFFFFF = elements, val&0x80000000 = shared (bool) |

Then what follows is, for amount of \"elements\", values one after the
other, using this same format.

### 20: `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} {#packedbytearrayclass_packedbytearray}

| Offset      | Len | Type    | Description          |
|-------------|-----|---------|----------------------|
| 4           | 4   | Integer | Array length (Bytes) |
| 8..8+length | 1   | Byte    | Byte (0..255)        |

The array data is padded to 4 bytes.

### 21: `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"} {#packedint32arrayclass_packedint32array}

| Offset         | Len | Type    | Description             |
|----------------|-----|---------|-------------------------|
| 4              | 4   | Integer | Array length (Integers) |
| 8..8+length\*4 | 4   | Integer | 32-bit signed integer   |

### 22: `PackedInt64Array<class_PackedInt64Array>`{.interpreted-text role="ref"} {#packedint64arrayclass_packedint64array}

| Offset         | Len | Type    | Description             |
|----------------|-----|---------|-------------------------|
| 4              | 8   | Integer | Array length (Integers) |
| 8..8+length\*8 | 8   | Integer | 64-bit signed integer   |

### 23: `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text role="ref"} {#packedfloat32arrayclass_packedfloat32array}

| Offset         | Len | Type    | Description                            |
|----------------|-----|---------|----------------------------------------|
| 4              | 4   | Integer | Array length (Floats)                  |
| 8..8+length\*4 | 4   | Integer | 32-bit IEEE 754 single-precision float |

### 24: `PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text role="ref"} {#packedfloat64arrayclass_packedfloat64array}

| Offset         | Len | Type    | Description                            |
|----------------|-----|---------|----------------------------------------|
| 4              | 4   | Integer | Array length (Floats)                  |
| 8..8+length\*8 | 8   | Integer | 64-bit IEEE 754 double-precision float |

### 25: `PackedStringArray<class_PackedStringArray>`{.interpreted-text role="ref"} {#packedstringarrayclass_packedstringarray}

| Offset | Len | Type    | Description            |
|--------|-----|---------|------------------------|
| 4      | 4   | Integer | Array length (Strings) |

For each String:

| Offset | Len | Type    | Description          |
|--------|-----|---------|----------------------|
| X+0    | 4   | Integer | String length        |
| X+4    | X   | Bytes   | UTF-8 encoded string |

Every string is padded to 4 bytes.

### 26: `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text role="ref"} {#packedvector2arrayclass_packedvector2array}

| Offset          | Len | Type    | Description  |
|-----------------|-----|---------|--------------|
| 4               | 4   | Integer | Array length |
| 8..8+length\*8  | 4   | Float   | X coordinate |
| 8..12+length\*8 | 4   | Float   | Y coordinate |

### 27: `PackedVector3Array<class_PackedVector3Array>`{.interpreted-text role="ref"} {#packedvector3arrayclass_packedvector3array}

| Offset           | Len | Type    | Description  |
|------------------|-----|---------|--------------|
| 4                | 4   | Integer | Array length |
| 8..8+length\*12  | 4   | Float   | X coordinate |
| 8..12+length\*12 | 4   | Float   | Y coordinate |
| 8..16+length\*12 | 4   | Float   | Z coordinate |

### 28: `PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"} {#packedcolorarrayclass_packedcolorarray}

| Offset | Len | Type | Description |
|----|----|----|----|
| 4 | 4 | Integer | Array length |
| 8..8+length\*16 | 4 | Float | Red (typically 0..1, can be above 1 for overbright colors) |
| 8..12+length\*16 | 4 | Float | Green (typically 0..1, can be above 1 for overbright colors) |
| 8..16+length\*16 | 4 | Float | Blue (typically 0..1, can be above 1 for overbright colors) |
| 8..20+length\*16 | 4 | Float | Alpha (0..1) |